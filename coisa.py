from zipfile import ZipFile
from funcoes import *
import os
import time
from PyPDF2 import PdfReader as pr
    
def extrairArquivos(arqzip):
    fileListZipFor = []
    with ZipFile(f"{arqzip}", "r") as file:
        PDF_ou_XML = lambda s: str(s).endswith((".xml", ".pdf"))
        for a in file.namelist():
            if PDF_ou_XML(a.lower()): fileListZipFor.append(a.lower())
        file.extractall("./tratar", members=(member for member in file.namelist() if PDF_ou_XML(member.lower())), pwd=None)

    todosAqui = False
    print("entrando sleep")
    while not todosAqui:
        if len(os.listdir('./tratar')) == len(fileListZipFor): todosAqui = True

    boleto = temBoleto("./tratar", os.listdir('./tratar'))

    if boleto != False:
        for a in boleto: os.remove(f'./tratar/{a}')
    

def tratarXML_PDF(soup: BeautifulSoup, diretorio="./tratar"):
    filenames = {
        "pdf": "",
        "xml": ""
    }

    for arq in os.listdir(diretorio):
        if ".xml" in arq.lower(): filenames["xml"] = arq
        if ".pdf" in arq.lower(): filenames["pdf"] = arq

    nome = trocarNome(buscarNome(soup))
    numero = buscarNumero(soup)

    novoFileName = f"{nome} {numero}"

    renomearArquivos(filenames, novoFileName)

    enviarImpressao()

def moverZip(arqzip):
    try:
        os.rename(f"./{arqzip}", f"./zipTratado/{arqzip}")
    except:
        print(arqzip.rsplit(" (", 1)[0])
        qnt = len([a for a in os.listdir("./zipTratado") if arqzip.rsplit(" (", 1)[0] in a])
        os.rename(f"./{arqzip}", f"./zipTratado/{arqzip.rsplit('.')[0]} ({qnt}).zip")