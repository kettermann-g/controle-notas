import imaplib
import email
from email.header import decode_header, make_header
import os
import shutil
from bs4 import BeautifulSoup
from funcoes import EmailBuscado, decoder, decodeAssunto, decodeRemetente, salvarNotaEntrada, conectar, salvarParcelasAgenda, verifica_anexos, ultimoEmail, temBoleto, bosta, extrairProdutos, salvarProdutosNota, enviarImpressao
from coisa import extrairArquivos, moverZip, tratarXML_PDF
import time
from PyPDF2 import errors

emailsBuscados = []

conn = conectar()

username = ""
senha = ""
imap_server = ""

imap = imaplib.IMAP4_SSL(imap_server)

imap.login(username, senha)

status, messages = imap.select("INBOX", readonly=True)

numMessages = int(messages[0])

print(numMessages)

fim = ultimoEmail(conn) if ultimoEmail(conn) is not None else numMessages-200
fim2 = numMessages-30
fim3 = fim2 - 40

naosalvos = []
naosalvosF = open("./naosalvos.csv", "w", encoding="utf-8")
naosalvosF.write("ID;ASSUNTO;REMETENTE\n")

extensao = lambda s: str(s).rsplit(".")[-1]
contaKeyDict = lambda s, k: len([a.split(" ")[0].lower() for a in s if a.split(" ")[0].lower() == k.lower()])

for a in range(fim2, fim3, -1):
    if verifica_anexos(a, imap):
        inicio_time = time.perf_counter()

        res, msg = imap.fetch(str(a), "(RFC822)")
        msgDec = email.message_from_bytes(msg[0][1])

        assuntoE = decodeAssunto(msgDec)
        remetente = decodeRemetente(msgDec)
        print(f"VERIFICANDO EMAIL {a} | {assuntoE} - {remetente}")

        lowermsg = str(msgDec).lower()

        tem_pdf_e_xml_anexo = ".xml" in lowermsg and ".pdf" in lowermsg

        

        if tem_pdf_e_xml_anexo:
            print(len(msg[0]))
            print(str(make_header(decode_header(msgDec["Subject"]))))

            anexos = []

            print(assuntoE)

            vEmail = EmailBuscado(str(a), assuntoE, {}, remetente, decoder(msgDec["Date"]))

            for a in msgDec.walk():
                not_multipart = a.get_content_maintype().lower() != 'multipart'
                temFilename = True if a.get_filename() is not None else False
                if not_multipart and temFilename:
                    filename = a.get_filename().lower()
                    key = filename.rsplit(".")[-1]

                    cKeys = contaKeyDict(vEmail.anexos, key)

                    if cKeys > 0: key = f"{key} {cKeys+1}"
                    vEmail.anexos[key.lower()] = filename.lower()

                    if ".xml" in filename.lower() or ".pdf" in filename.lower():
                        fp2 = f"./tratar/{decoder(filename)}"
                        
                        if not os.path.isfile(fp2):
                            fp = open(fp2, 'wb')
                            fp.write(a.get_payload(decode=True))
                            fp.close()
                
            try:
                boleto = temBoleto("./tratar", os.listdir('./tratar'))
            except errors.PdfReadError:
                l = os.listdir("./tratar")
                for a in l:
                    os.remove(f"./tratar/{a}")
                continue

            if boleto != False:
                for a in boleto: os.remove(f'./tratar/{a}')

            xmlF = list(filter(lambda a: str(a.lower()).endswith(".xml"), os.listdir("./tratar")))[0]

            file = open(f"./tratar/{xmlF}", "r")
            soup = BeautifulSoup(bosta(file.read()), features="xml")
            file.close()

            try:
                idBancoNota = salvarNotaEntrada(soup, vEmail, conn)

                salvarParcelasAgenda(soup, idBancoNota, conn)

                tags = ["cProd", "cEAN", "xProd", "CFOP", "uCom", "qCom", "vUnCom", "vProd"]

                prods = soup.find_all("prod")
                if len(prods) > 0:
                    salvarProdutosNota(soup, idBancoNota, conn, tags)


                tratarXML_PDF(soup)

            except(ValueError):
                print("XML CAGADOOOOO VALUE ERROR")
                os.rename(f"./tratar/{xmlF}", f"./guardar/{xmlF}")
                for a in os.listdir("./tratar"):
                    os.remove(f"./tratar/{a}")
                naosalvos.append({"ID": vEmail.idEmail, "ASSUNTO": vEmail.assunto, "REMETENTE":vEmail.remetente, "DATA":vEmail.data, "ANEXOS":vEmail.anexos})
                naosalvosF.write(f"{vEmail.idEmail};{vEmail.assunto};{vEmail.remetente}\n")

        else:
            print("NAO TEM .XML NEM .PDF")
        
        fim_time = time.perf_counter()

        print(f"Tempo decorrido neste email: {fim_time - inicio_time}")

print(naosalvos)
naosalvosF.close()