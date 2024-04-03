import time
from funcoes import logar_imap, verifica_anexos, decoder, manipularData
import email
from email.header import make_header, decode_header

def merda():
    inicio_login = time.perf_counter()
    imap = logar_imap()
    status, messages = imap.select("INBOX", readonly=True)
    numMessages = int(messages[0])
    fim_login = time.perf_counter()

    tempo_login = fim_login - inicio_login

    idemail = "19440"
    inicio_1 = time.perf_counter()
    res, struct = imap.fetch(idemail, "(BODYSTRUCTURE)")
    d = struct[0].decode()
    a = ".pdf" and ".xml" in d.lower()
    _, msg = imap.fetch(idemail, "BODY.PEEK[HEADER]")
    msgDec = email.message_from_bytes(msg[0][1])
    print(msgDec["From"])
    print(msgDec["Subject"])
    fim_1 = time.perf_counter()
    tempo_peek = fim_1 - inicio_1

    inicio_2 = time.perf_counter()
    res, struct = imap.fetch(idemail, "(BODYSTRUCTURE)")
    d = struct[0].decode()
    a = ".pdf" and ".xml" in d.lower()
    _, msg = imap.fetch(idemail, "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)])")
    msgDec = email.message_from_bytes(msg[0][1])
    print(msgDec["From"])
    print(msgDec["Subject"])
    fim_2 = time.perf_counter()

    tempo_peek_2 = fim_2 - inicio_2
    print(tempo_login)
    print(tempo_peek)
    print(tempo_peek_2)

def bosta():
    inicio_login = time.perf_counter()
    imap = logar_imap()
    status, messages = imap.select("INBOX", readonly=True)
    numMessages = int(messages[0])
    fim_login = time.perf_counter()

    tempo_login = fim_login - inicio_login

    id_maior = numMessages
    id_menor = id_maior-1000
    inicio_fetch_multiplo = time.perf_counter()
    range_fetch = f"{id_maior}:{id_menor}"
    _, msg = imap.fetch(range_fetch, "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE)] BODYSTRUCTURE)")

    lista_emails_agrupados = [[msg[a], msg[a+1]] for a in range(0, len(msg), 2)]

    emails_decoded = []
    emails_com_nota = []
    for a in lista_emails_agrupados:
        print("PRINT PRORA PRINT PORRA PRINT PORRA ")
        id_email = a[0][0].decode().split(" ", 1)[0]
        fields_header = email.message_from_bytes(a[0][1])
        print(id_email, fields_header['Date'])
        data_ = manipularData(fields_header['Date'], 'email')
        if data_ == "FUDEU":
            string_canonica = repr(fields_header['Date'])
            sp = string_canonica.split(" ", 1)
            lixo = string_canonica.split(" ", 1)[0]
            nova_string = sp[1].replace("'", "")
            print(nova_string)

            print(repr(fields_header['Date']))
            break
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

    fim_fm = time.perf_counter()
    print(f"QUANTIDADE DE EMAILS COM NOTA: {len(emails_com_nota)}")
    print(tempo_login)
    tempo_fm = fim_fm - inicio_fetch_multiplo
    print(tempo_fm)
    print(emails_decoded[0:3])

bosta()