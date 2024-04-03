import imaplib
from tkinter import ttk
from ttkthemes import ThemedTk
from functools import partial
import mysql.connector
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import time
import email
import os
import re
from funcoes import conectar, buscarTodas, logar_imap, ultimoEmail, verifica_anexos, decodeAssunto, decodeRemetente, decoder, EmailBuscado, temBoleto, bosta, salvarNotaEntrada, salvarParcelasAgenda, salvarProdutosNota, manipularData
from coisa import tratarXML_PDF
from PyPDF2 import errors


class GridBuscarAnexos(ttk.Frame):
    def __init__(self, container, conn: mysql.connector.connection.MySQLConnection):
        super().__init__(container)
        self.conn = conn
        self.imap = ""
        self.iniciando = True

        self.ultimo_email = ultimoEmail(self.conn)

        self.todos_ids = self.buscar_todos_ids()

        self.lista_emails = []

        self.lista_emails_com_nota = []

        self.lista_paginas = [[]]

        self.conta_pagina = 0

        self.email_selecionado = "VAZIO"

        self.criar_frame_emails()

        self.reconectar_email()

        self.update_idletasks()

    def criar_frame_emails(self):
        self.frame_emails = ttk.Frame(self)
        self.frame_emails.grid(row=0, column=0)
        self.frame_emails.grid_columnconfigure(0, weight=1)
        self.frame_emails.update_idletasks()

        self.frame_emails_2 = ttk.Frame(self)
        self.frame_emails_2.grid(row=1, column=0, sticky="nsew")
        for a in range(0,3): self.frame_emails_2.grid_columnconfigure(a, weight=1)
        self.frame_emails_2.update_idletasks()

        self.criar_tabela_emails()

        self.botao_ant = ttk.Button(self.frame_emails_2, text="Anterior", command=partial(self.troca_pagina_2, "-"))
        self.botao_ant.grid(column=0, row=0)
        self.botao_ant.update_idletasks()

        self.label_qnt = ttk.Label(self.frame_emails_2, text="XX-XX DE XX (PÁGINA X DE X)")
        self.label_qnt.grid(column=1, row=0)

        self.botao_prox = ttk.Button(self.frame_emails_2, text="Próximo", command=partial(self.troca_pagina_2, "+"))
        self.botao_prox.grid(column=2, row=0)
        self.botao_prox.update_idletasks()

        self.frame_emails_3 = ttk.Frame(self)
        self.frame_emails_3.grid(column=1, row=0, rowspan=2)

        self.botao_baixar_anexos = ttk.Button(self.frame_emails_3, text="BAIXAR", command=partial(self.fetch_email_inteiro))
        self.botao_baixar_anexos.grid(column=0, row=0)

    def buscar_todos_ids(self):
        cursor = self.conn.cursor()

        sql = "SELECT idEmail FROM notaFiscalEntrada"
        cursor.execute(sql)

        f = [a[0] for a in cursor.fetchall()]
        return f
    
    def criar_tabela_emails(self):
        self.botao_primeiros = ttk.Button(self.frame_emails, text="BUSCAR PRIMEIRA PAGINA DE EMAILS", command=partial(self.fetch_emails_2))
        self.botao_primeiros.grid(column=0, row= 0)
        self.col = ("NumeroCount", "idEmail", "assunto", "remetente", "data", "baixado")
        self.txt_col = (" ", "ID", "Assunto", "Remetente", "Data", "Baixado")
        self.size_col = (35, 80, 350, 350, 150, 45)
        self.tabela_emails = ttk.Treeview(self.frame_emails, columns=self.col, show="headings", height=14)
        for a, b, c in zip(self.col, self.txt_col, self.size_col):
            self.tabela_emails.heading(a, text= b)
            self.tabela_emails.column(a, width=c)

        self.tabela_emails.grid(column=0, row=1, sticky="nsew")

        self.tabela_emails.bind("<ButtonRelease-1>", self.selec_email)

        self.tabela_emails.update_idletasks()

    def reconectar_email(self):
        self.imap = logar_imap()
        self.status, self.messages = self.imap.select("INBOX", readonly=True)
        self.numMessages = int(self.messages[0])
        self.ultimo = self.numMessages + 1


    def verifica_email_conec(self):
        try:
            a = verifica_anexos(self.numMessages, self.imap)
        except imaplib.IMAP4.abort:
            self.reconectar_email()

    def verifica_bd_conec(self):
        try:
            _ = ultimoEmail(self.conn)
        except:
            self.conn = conectar()
    
    def selec_email(self, a):
        reg = self.tabela_emails.identify("region", a.x, a.y)
        if reg == "heading":
            return
        item = self.tabela_emails.item(self.tabela_emails.focus())['values']
        self.email_selecionado = item
        print(item)
        print(item[1])

    def fetch_email_inteiro(self):
        self.verifica_bd_conec()
        self.verifica_email_conec()
        if self.email_selecionado != "VAZIO":
            contaKeyDict = lambda s, k: len([a.split(" ")[0].lower() for a in s if a.split(" ")[0].lower() == k.lower()])

            values = self.email_selecionado
            id_email = self.email_selecionado[1]
            print(id_email)
            res, msg = self.imap.fetch(str(id_email), "(RFC822)")
            msgDec = email.message_from_bytes(msg[0][1])

            vEmail = EmailBuscado(str(id_email), values[2], {}, values[3], decoder(msgDec["Date"]))

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
                        filename_decoded = decoder(filename)
                        fd_split = filename_decoded.rsplit(".", 1)
                        extensao = fd_split[1]
                        nome = fd_split[0]

                        invalido = '''\\/.:=?'''

                        for char in invalido:
                            nome = nome.replace(char, "")

                        filename_decoded = f"{nome}.{extensao}"
                        fp2 = f"./tratar/{filename_decoded}"
                        
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
                return
            
            if boleto != False:
                for a in boleto: os.remove(f'./tratar/{a}')

            xmlF = list(filter(lambda a: str(a.lower()).endswith(".xml"), os.listdir("./tratar")))[0]

            file = open(f"./tratar/{xmlF}", "r")
            soup = BeautifulSoup(bosta(file.read()), features="xml")
            file.close()

            try:
                idBancoNota = salvarNotaEntrada(soup, vEmail, self.conn)

                salvarParcelasAgenda(soup, idBancoNota, self.conn)

                tags = ["cProd", "cEAN", "xProd", "CFOP", "uCom", "qCom", "vUnCom", "vProd"]

                prods = soup.find_all("prod")
                if len(prods) > 0:
                    salvarProdutosNota(soup, idBancoNota, self.conn, tags)


                tratarXML_PDF(soup)

                self.todos_ids = self.buscar_todos_ids()
                num_linha = values[0] - 1
                linha_mudar = self.lista_paginas[self.conta_pagina][num_linha]
                linha_mudar[5] = 1
                self.lista_paginas[self.conta_pagina][num_linha] = tuple(linha_mudar)
                self.jogar_na_tela()


            except(ValueError):
                print("XML CAGADOOOOO VALUE ERROR")
                os.rename(f"./tratar/{xmlF}", f"./guardar/{xmlF}")
                for a in os.listdir("./tratar"):
                    os.remove(f"./tratar/{a}")

    def fetch_emails_2(self):
        id_maior = self.numMessages
        id_menor = id_maior-1000

        range_fetch = f"{id_maior}:{id_menor}"

        _, msg = self.imap.fetch(range_fetch, "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE)] BODYSTRUCTURE)")

        lista_emails_agrupados = [[msg[a], msg[a+1]] for a in range(0, len(msg), 2)]

        emails_decoded = []
        emails_com_nota = []
        for a in lista_emails_agrupados:
            print("PRINT PORRA PRINT PORRA PRINT PORRA ")
            id_email = a[0][0].decode().split(" ", 1)[0]

            fields_header = email.message_from_bytes(a[0][1])
            print(id_email, fields_header['Date'])
            data_ = manipularData(fields_header['Date'], 'email')

            header_decodada = decoder(f'''{id_email}|{fields_header['Subject']}|{fields_header['From'].replace('"', '')}|{data_}''')

            if not isinstance(a[1], tuple): struct = a[1].decode()
            else: 
                string_byte = bytes("", encoding="utf-8")
                for byte_ in a[1]: string_byte += byte_
                try:
                    string_byte = string_byte.decode()
                except:
                    struct = str(string_byte)

            tem_pdf_e_xml = ".xml" in struct.lower() and ".pdf" in struct.lower()
            header_decodada = header_decodada.split("|")

            for num, a in enumerate(header_decodada): header_decodada[num] = a.strip()
            emails_decoded.append(header_decodada)
            if tem_pdf_e_xml:
                emails_com_nota.append(header_decodada)

        emails_decoded = emails_decoded[::-1]
        emails_com_nota = emails_com_nota[::-1]

        for numero, a in enumerate(emails_com_nota):
            a.insert(0, numero+1)
        
            bx = 1 if int(a[1]) in self.todos_ids else 0
            a.append(bx)

        self.lista_emails_com_nota = emails_com_nota
        self.paginar(emails_com_nota)
        self.jogar_na_tela()
        print(id1 := self.todos_ids[0])
        print(type(id1))
        print(id2 := emails_com_nota[0][1])
        print(type(id2))

    def paginar(self, lista):
        c = 0
        for num, a in enumerate(lista):
            if num % 15 == 0 and num > 0:
                self.lista_paginas.append([])
                c += 1
            self.lista_paginas[c].append(a)

    def jogar_na_tela(self):
        self.tabela_emails.delete(*self.tabela_emails.get_children())
        
        for num, a in enumerate(self.lista_paginas[self.conta_pagina]):
            self.tabela_emails.insert(parent='', index=num, values=tuple(a))

        texto_paginas = self.texto_paginas(self.conta_pagina+1, len(self.lista_emails_com_nota))
        self.label_qnt.config(text= texto_paginas)

    def texto_paginas(self, num, len_lista):
        numFinalLen = len(self.lista_paginas)
        return f"{(15*num) - 14} - {15*num if len_lista>num*15 else len_lista} DE {len_lista} (PAGINA {num} de {numFinalLen})"
    
    def incrementa_num_pag(self, limites, sinal_op):
        try:
            nv = eval(f"{self.conta_pagina} {sinal_op} 1")
            if nv < limites["menor"]: nv = limites["menor"]
            elif nv > limites["maior"]: nv = limites["maior"]

            if nv == self.conta_pagina:
                return False
            else:
                self.conta_pagina = nv
                return True
        except:
            return False
        
    def troca_pagina_2(self, sinal_op):
        limites = {"maior": len(self.lista_paginas)-1, "menor": 0}

        incrementou = self.incrementa_num_pag(limites, sinal_op)
        print(self.conta_pagina)
        if incrementou:
            self.jogar_na_tela()