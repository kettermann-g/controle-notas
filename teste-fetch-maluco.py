import imaplib
import email
from email.header import Header, decode_header, make_header
from email.parser import HeaderParser
from email import utils
import pytz
from datetime import datetime, timedelta


username = ""
senha = ""
imap_server = ""

imap = imaplib.IMAP4_SSL(imap_server)

imap.login(username, senha)

status, messages = imap.select("INBOX", readonly=True)


def verifica_anexos(a):
    res, struct = imap.fetch(f"{a}", "(BODYSTRUCTURE)")
    dec = struct[0].decode()
    pdf_xml = 'pdf' in dec.lower() and 'xml' in dec.lower()
    return True if pdf_xml else False

from funcoes import lancarBD, EmailBuscado, decoder, decodeAssunto, decodeRemetente, salvarNotaEntrada, conectar, salvarParcelasAgenda

c = 1
for a in range(int(messages[0]), 19100, -1):
    if verifica_anexos(a):
        res, msg = imap.fetch(str(a), "(RFC822)")
        msgDec = email.message_from_bytes(msg[0][1])

        assuntoE = decodeAssunto(msgDec)
        remetente = decodeRemetente(msgDec)
        print(f"VERIFICAR EMAIL | {assuntoE} - {remetente}")