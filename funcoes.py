from bs4 import BeautifulSoup, element
import os
import json
from PyPDF2 import PdfReader as pr
import mysql.connector
from datetime import datetime
from email import message, utils
from email.header import decode_header, make_header
from datetime import datetime, timedelta
import csv
import imaplib
import configparser

class EmailBuscado:
    def __init__(self, idEmail, assunto, anexos, remetente, data):
        self.idEmail = idEmail
        self.assunto = assunto
        self.anexos = anexos
        self.remetente = remetente
        self.data = data

    def criarZip():
        print("asjodhiosha")

c = configparser.ConfigParser()
c.sections()
c.read("config.ini")
host = c["mysql"]["host"]
user = c["mysql"]["user"]
senha = c["mysql"]["senha"]
database = c["mysql"]["database"]


def conectar():
    global host, user, senha, database
    conn = mysql.connector.connect(
        host= host,
        user= user,
        password= senha,
        database= database
    )

    return conn

user_imap = c["email"]["username"]
senha_imap = c["email"]["senha"]
imapserver = c["email"]["imapserver"]


def logar_imap():
    global imapserver, senha_imap, user_imap

    imap = imaplib.IMAP4_SSL(imapserver)

    imap.login(user_imap, senha_imap)

    return imap



def buscarTodas(conn: mysql.connector.connection.MySQLConnection, modo, **kwargs):
    cursor = conn.cursor()
    
    if modo == "notas":
        sql2 = '''SELECT idNota, remetente, assuntoEmail, dataEmail, emp.customNome, emp.nomeFantasia, emp.razaoSocial,
                numeroNota, valorTotalNota, op.descricao as cfop, dataEmissao, adicionadoEm, impresso
                    FROM notaFiscalEntrada
                        INNER JOIN empresas as emp on emp.idEmpresa = notaFiscalEntrada.empresa
                        INNER JOIN operacoes as op on notaFiscalEntrada.natOp = op.idOP
                            ORDER BY dataEmissao DESC'''
        
        cursor2 = conn.cursor()
        cursor2.execute(sql2)
        fetch2 = cursor2.fetchall()
        keys2 = cursor2.column_names

        print("LEN KEYS 2",len(keys2))
        print("LEN FETCH 2 0",len(fetch2[0]))

        d2 = [{k: l[num] for num, k in enumerate(keys2)} for l in fetch2]

        return d2
    
    elif modo == "unica_por_id":
        if isinstance(kwargs.get('id_nota'), int):
            sql = f'''SELECT
                        IFNULL(emp.customNome, "VAZIO") as nomeCustom,
                        IFNULL(emp.nomeFantasia, "VAZIO") as fantasia,
                        emp.razaoSocial, numeroNota, valorTotalNota,
                        op.descricao as cfop,
                        DATE_FORMAT(dataEmissao, "%d/%m/%Y %H:%i:%s") as emissao,
                        remetente,
                        assuntoEmail,
                        DATE_FORMAT(dataEmail, "%d/%m/%Y %H:%i:%s") as emailData,
                        impresso,
                        DATE_FORMAT(adicionadoEm, "%d/%m/%Y %H:%i:%s") as adic
                            FROM notaFiscalEntrada
                                INNER JOIN empresas as emp on emp.idEmpresa = notaFiscalEntrada.empresa
                                INNER JOIN operacoes as op on op.idOP = notaFiscalEntrada.natOp
                                    WHERE idNota = {kwargs.get('id_nota')}'''
            
            cursor.execute(sql)
            fetch = cursor.fetchone()
            return fetch

    elif modo == "duplicatas":
        sql = '''SELECT
        IF(nfe.customNome IS NOT NULL, nfe.customNome, nfe.nomeFantasia) AS nome,
        IF(numDuplicata <> "000", CONCAT(nfe.numeroNota, "-", numDuplicata), nfe.numeroNota) AS num,
        nfe.dataEmissao,
        idDuplicata,
        valor,
        venc,
        pago FROM
            duplicatas
            INNER JOIN notaFiscalEntrada AS nfe ON duplicatas.idNota = nfe.idNota
                ORDER BY venc DESC'''
        
        cursor.execute(sql)
        fetch = cursor.fetchall()
        keys = cursor.column_names

        todas = list(map(lambda a: {keys[i]: a[i] for i in range(0, len(a))}, fetch))

        return todas

def ultimoEmail(conn: mysql.connector.connection.MySQLConnection):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(idEmail) FROM notaFiscalEntrada")
    return cursor.fetchone()[0]

def decoder(s):
    return str(make_header(decode_header(s)))


def temBoleto(path, filelist):
    nomesBoleto = []
    for file in filelist:
        if str(file).endswith('.pdf'):
            reader = pr(f"{path}/{file}")
            text = reader.pages[0].extract_text()
            if "bol" in file.lower():
                nomesBoleto.append(file)
            elif 'nf-e' not in text.lower() and\
                'nfe' not in text.lower():
                nomesBoleto.append(file)
        else:
            continue
    
    return nomesBoleto if len(nomesBoleto) > 0 else False

def decodeAssunto(msg: message):
    invalido = ''':'\\/"#<>$+%.'''

    ass = "".join(decoder(msg["Subject"]).splitlines())
    assuntoE = "".join(filter(lambda x: x not in invalido, ass))

    return assuntoE

def verifica_anexos(a, imap: imaplib.IMAP4_SSL):
    res, struct = imap.fetch(f"{a}", "(BODYSTRUCTURE)")
    dec = struct[0].decode()
    pdf_xml = '.pdf' in dec.lower() and '.xml' in dec.lower()
    return True if pdf_xml else False


def decodeRemetente(msg: message):
    df = decoder(msg["From"])
    if len(df.split(" ")) > 1: df = df.rsplit(" ")[-1]

    remetente = "".join(filter(lambda x: x not in '<>', df))
    return remetente


def trocarNome(nome):
    j = open("./nomes.json", "r", encoding="utf-8")
    nomes = json.loads(j.read())
    j.close()
    try:    
        return nomes[nome]
    except:
        return nome
    
def bosta(string):
    if "ï»¿" in string: return string[3:]
    else: return string

def manipularData(datestring, tipo):
    if tipo == "email":
        try:
            datetime_obj = utils.parsedate_to_datetime(datestring)
        except ValueError:
            if datestring is None:
                return "VAZIO"
            elif len(datestring.split(" ")) == 2 and datestring is not None:
                return datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
            else:
                string_canonica = repr(datestring)
                sp = string_canonica.split(" ", 1)
                lixo = string_canonica.split(" ", 1)[0]
                nova_string = sp[1].replace("'", "")

                datetime_obj = utils.parsedate_to_datetime(nova_string)

                return datetime_obj

        if "+00:00" in str(datetime_obj):
            
            datetime_obj = datetime_obj - timedelta(hours=3)
        datetime_obj = datetime.strptime(str(datetime_obj)[:19], "%Y-%m-%d %H:%M:%S")
        return datetime_obj
    elif tipo == "xml":
        dt_obj = datetime.strptime(datestring[:len(datestring)-6], "%Y-%m-%dT%H:%M:%S")
        return dt_obj

def verificarCFOP(cfop, conn: mysql.connector.connection.MySQLConnection):
    cursor = conn.cursor()
    cursor.execute(f"SELECT idOP FROM operacoes WHERE codigoOp = '{cfop}'")
    r = cursor.fetchone()
    if r is None:
        codigo = ""
        desc = ""
        with open("cfop.csv", encoding="utf-8", newline='') as f:
            reader = csv.reader(f, delimiter=";")
            for a in reader:
                if a[0] == cfop:
                    codigo = a[0]
                    desc = a[1]
                    break
        sql = f"INSERT INTO operacoes (codigoOp, descricao) VALUES ('{codigo}', '{desc}')"
        cursor.execute(sql)
        lastid = cursor.lastrowid
        conn.commit()
        return lastid
    else:
        return r[0]
    

#cProd, cEAN, xProd, CFOP, uCom, qCom, vProd
def extrairProdutos(soup: BeautifulSoup, lista: list[element.Tag], tags: list[str]):
    # try:
    lista_find = [{b: a.find(b).text for b in tags} for a in lista]
    return lista_find
    # except:
    #     return None

def salvarProdutosNota(soup: BeautifulSoup, idNota, conn: mysql.connector.connection.MySQLConnection, tags: list[str]):
    cursor = conn.cursor()
    prods = soup.find_all("prod")
    if len(prods) > 0:

        listaProdutos = extrairProdutos(soup, prods, tags)
        for a in listaProdutos:
            a["CFOP"] = verificarCFOP(a["CFOP"], conn)
            valores = [f"\'{a[b]}\'" if isinstance(a[b], str) else f"{a[b]}" for b in a]
            sql = f'''INSERT INTO produtos (idNota, {', '.join(tags)})
                VALUES (
                {idNota},
                {", ".join(valores)}
                )'''
            cursor.execute(sql)
        
        conn.commit()

def buscar_id_empresa(dic_dados, conn: mysql.connector.connection.MySQLConnection):
    cursor = conn.cursor()
    cursor.execute(f"SELECT idEmpresa FROM empresas WHERE razaoSocial = '{dic_dados['xNome']}'")
    id_empresa = cursor.fetchone()

    if id_empresa is not None:
        return id_empresa[0]
    else:
        rs = f"'{dic_dados['xNome']}'"
        nfant = dic_dados['xFant']
        print(rs)
        print(nfant)
        sql = f"INSERT INTO empresas (nomeFantasia, razaoSocial) VALUES ({nfant}, {rs})"
        print(sql)
        cursor.execute(sql)
        conn.commit()
        return cursor.lastrowid

#coisas do xml: numero nota, nome fantasia, razao social, numero nota, natureza, data emissao
# coisas do email: idEmail, remetente, assunto, data 
def salvarNotaEntrada(soup: BeautifulSoup, email: EmailBuscado, conn: mysql.connector.connection.MySQLConnection):
    cursor = conn.cursor()
    dados = {"idEmail": email.idEmail,
                "remetente": email.remetente,
                "assuntoEmail": email.assunto,
                "dataEmail": email.data,
                "xFant": "",
                "xNome": "",
                "customNome": "",
                "CFOP": "",
                "dhRecbto": "",
                "numero": "",
                "vNF": ""}
    
    lista = ["xFant", "xNome", "CFOP", "dhRecbto"]
    for a in lista:
        try:
            dados[a] = soup.find(a).text
        except:
            dados[a] = ""
    
    dados["dataEmail"] = manipularData(dados["dataEmail"], "email")
    dados["dhRecbto"] = manipularData(dados["dhRecbto"], "xml")
    dados["CFOP"] = verificarCFOP(dados["CFOP"], conn)
    dados["numero"] = buscarNumero(soup)
    dados["vNF"] = buscarValorTotal(soup)
    
    fantExiste = dados["xFant"] != ""
    nomeAntes = dados["xFant"] if fantExiste else dados["xNome"]
    custom = trocarNome(dados["xFant"]) if fantExiste else trocarNome(dados["xNome"])
    dados["customNome"] = f"'{custom}'" if custom != nomeAntes else "NULL"

    fantasia = f"'{dados['xFant']}'" if fantExiste else "NULL"

    dados["xFant"] = fantasia
    
    id_empresa = buscar_id_empresa(dados, conn)

    sql = f'''INSERT INTO notaFiscalEntrada (idEmail, remetente, assuntoEmail, dataEmail, empresa, numeroNota, valorTotalNota, natOp, dataEmissao, adicionadoEm, impresso)
    VALUES (
    {dados["idEmail"]},
    '{dados["remetente"]}',
    '{dados["assuntoEmail"]}',
    '{dados["dataEmail"].strftime('%Y-%m-%d %H:%M:%S')}',
    {id_empresa},
    '{dados["numero"]}',
    {dados["vNF"]},
    '{dados["CFOP"]}',
    '{dados["dhRecbto"].strftime('%Y-%m-%d %H:%M:%S')}',
    '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}',
    0
    )'''

    cursor.execute(sql)
    lastid = cursor.lastrowid
    conn.commit()

    return lastid


def buscarNome(soup: BeautifulSoup):       
    try:
        return soup.find("xFant").text
    except:
        return soup.find("xNome").text
        
def buscarValorTotal(soup: BeautifulSoup):
    try: return f"'{soup.find('vNF').text}'"
    except: return "NULL"

def buscarNumero(soup: BeautifulSoup):
    l = ["nNF", "nCT"]
    if soup.find(l[0]) == None:
        num = soup.find(l[1]).text
    else:
        num = soup.find(l[0]).text
    return num

def renomearArquivos(dict, newfilename):
    pdf = dict["pdf"]
    xml = dict["xml"]
    os.rename(f"./tratar/{pdf}", f"./tratar/{newfilename}.pdf")
    os.rename(f"./tratar/{xml}", f"./tratar/{newfilename}.xml")

def zipTratado(filename):
    nome = str(filename).rsplit("/")[-1]
    try:
        os.rename(filename, f"./zipTratado/{nome}")
    except(FileExistsError):
        num = os.listdir("./zipTratado").count(nome)
        split = nome.rsplit(".", 1)
        os.rename(filename, f"./zipTratado/{split[0]} ({num}).{split[-1]}")

def enviarImpressao():
    listdir = os.listdir(f"./tratar")
    pathPDF = "./notas/pdf/imprimir"
    pathXML = "./notas/xml"
    for a in listdir:
        os.rename(f"./tratar/{a}", f"{pathPDF}/{a}") if ".pdf" in a else\
            os.rename(f"./tratar/{a}", f"{pathXML}/{a}")
        
def salvarParcelasAgenda(soup: BeautifulSoup, idNotaBanco, conn: mysql.connector.connection.MySQLConnection):
    dups = soup.find_all("dup")
    lDup = extrairDuplicatas(dups, ["nDup","dVenc","vDup"])
    if lDup is not None:
        for d in lDup:
            sql = f'''INSERT INTO duplicatas (idNota, numDuplicata, valor, venc, pago)
            VALUES (
            {idNotaBanco},
            '{d['nDup']}',
            '{d['vDup']}',
            '{d['dVenc']}',
            0
            )'''

            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

def extrairDuplicatas(lista: list[element.Tag], tags: list[str]):
    if len(lista) > 1: return [{b: a.find(b).text for b in tags} for a in lista]
    elif len(lista) == 1: return [{'nDup': '000', 'dVenc': lista[0].find('dVenc').text, 'vDup': lista[0].find('vDup').text}]
    else:
        return None


def lancarBD(email: EmailBuscado, fileNameFunction, conn: mysql.connector.connection.MySQLConnection):
    cursor = conn.cursor()

    with open(f"{fileNameFunction}", 'r') as f:
        data = f.read()

    if "ï»¿" in data[0:3]:
        data = data[3:]

    Bs_data = BeautifulSoup(data, "lxml-xml")
    Fantasia = Bs_data.find('xFant')
    if Fantasia is not None:
        xFant = Fantasia.text
    else:
        xFant = Bs_data.find('xNome').text

    # if xFant in listaNomesFantasia:
    #     xFant = listaTrocarNome[listaNomesFantasia.index(xFant)]

    xFant = trocarNome(xFant)

    nNF = Bs_data.find('nNF').text
    dup = Bs_data.findAll('dup')
    adicionadoEm = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(adicionadoEm)

    if len(dup) > 1:
        print (f"TEM {len(dup)} DUPLICATAS")
        for i in dup:
            nDup = i.findNext('nDup').text
            dVenc = i.findNext('dVenc').text
            vDup = i.findNext('vDup').text
            print(f"NUMERO DUPLICATA: {nDup} | VENCIMENTO: {dVenc} | VALOR DUPLICATA: {vDup}")

            sql = f'''INSERT INTO entrada (idEmail, nomeFantasia, remetente, dataEmail, numeroNota, duplicata, valor, venc, pago, adicionadoEm) VALUES (
                {email.idEmail},
                '{xFant}',
                '{email.remetente}',
                '{email.data}',
                '{nNF}',
                '{nDup}',
                '{vDup}',
                '{dVenc}',
                FALSE,
                '{adicionadoEm}')'''

            cursor.execute(sql)
            conn.commit()
    elif len(dup) == 1:
        print("TEM APENAS UMA OU NENHUMA DUPLICATA")
        valor = Bs_data.find('vDup').text
        venc = Bs_data.find('dVenc').text

        sql = f'''INSERT INTO entrada (idEmail, nomeFantasia, remetente, dataEmail, numeroNota, valor, venc, pago, adicionadoEm) VALUES (
                {email.idEmail},
                '{xFant}',
                '{email.remetente}',
                '{email.data}',
                '{nNF}',
                '{vDup}',
                '{dVenc}',
                FALSE,
                '{adicionadoEm}')'''

        cursor.execute(sql)
        conn.commit()
    else:
        if Bs_data.find('vLiq') is not None:
            valor = Bs_data.find('vLiq').text
        else:
            valor = Bs_data.find('vPag').text
        venc = Bs_data.find('dhEmi').text[:10]

        sql = f'''INSERT INTO entrada (idEmail, nomeFantasia, numeroNota, valor, venc, pago, adicionadoEm) VALUES (
                    {email.idEmail},
                    '{xFant}',
                    '{nNF}',
                    '{valor}',
                    '{venc}',
                    TRUE,
                    '{adicionadoEm}')'''

        cursor.execute(sql)
        conn.commit()