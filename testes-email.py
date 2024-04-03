#arquivo pra testar se o codigo ta pegando todos os emails com xml e pdf
#com e sem a funçao que eu fiz que pega o bodystructure sem baixar o email todo

import imaplib
import email
from email.header import decode_header, make_header
import os
import shutil
from funcoes import EmailBuscado, decoder, decodeAssunto, decodeRemetente, salvarNotaEntrada, conectar, salvarParcelasAgenda, verifica_anexos
from coisa import extrairArquivos, moverZip, tratarXML_PDF
import time

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

fim = numMessages - 10

extensao = lambda s: str(s).rsplit(".")[-1]
contaKeyDict = lambda s, k: len([a.split(" ")[0].lower() for a in s if a.split(" ")[0].lower() == k.lower()])

filefunc = open("./testes_com_func.csv", "w", encoding="utf-8")
filefunc.write(f"NUM;ASSUNTO;REMETENTE\n")

inicio_time = time.perf_counter()

for a in range(numMessages, numMessages-300, -1):
    print(a)
    if verifica_anexos(a, imap):
        print(f"{a} - PASSOU")
        res, msg = imap.fetch(str(a), "(RFC822)")
        msgDec = email.message_from_bytes(msg[0][1])

        assuntoE = decodeAssunto(msgDec)
        remetente = decodeRemetente(msgDec)
        filefunc.write(f"{a};{assuntoE};{remetente}\n")
fim_time = time.perf_counter()

filefunc.write(f"#Tempo decorrido nos emais utilizando a função: {fim_time - inicio_time}")
filefunc.close()

print(f"Tempo decorrido nos emais utilizando a função: {fim_time - inicio_time}")
print("-"*35)
file = open("./testes_sem_func.csv", "w", encoding="utf-8")
file.write("NUM;ASSUNTO;REMETENTE\n")


inicio_time = time.perf_counter()

for a in range(numMessages, numMessages-300, -1):
    print(a)
    res, msg = imap.fetch(str(a), "(RFC822)")
    msgDec = email.message_from_bytes(msg[0][1])

    lowermsg = str(msgDec).lower()

    tem_pdf_e_xml_anexo = ".xml" in lowermsg and ".pdf" in lowermsg

    if tem_pdf_e_xml_anexo:
        print(f"{a} - PASSOU")

        assuntoE = decodeAssunto(msgDec)
        remetente = decodeRemetente(msgDec)
        file.write(f"{a};{assuntoE};{remetente}\n")

fim_time = time.perf_counter()
file.write(f"#Tempo decorrido nos emais sem utilizar a função: {fim_time - inicio_time}")
file.close()

print(f"Tempo decorrido nos emais sem utilizar a função: {fim_time - inicio_time}")