import os
from win32 import win32print, win32api
import time

umavez = ["SISTEM 32803.pdf",
          "UTILIDADES ELÉTRICAS 82280.pdf",
          "UTILIDADES ELÉTRICAS 82529.pdf",
          "UTILIDADES ELÉTRICAS 82530.pdf",
          ]

path = "C:/Users/Usuário/Desktop/script"
imprimir = f"{path}/notas/pdf/imprimir"
impressos = f"{path}/notas/pdf/impressos"
arquivos = os.listdir(f"{path}/notas/pdf/imprimir")
print(arquivos)

print(win32print.GetDefaultPrinter())

arquivosImpressos = []

print('ENTRANDO NO LOOP PRA ENVIAR ARQUIVOS PRA IMPRESSORA')
for a in range(0, 3):
    try:
        print(f"ITERAÇÃO {a}")
        print("ENVIANDO PRIMEIRA COPIA")
        win32api.ShellExecute(0, "print", f"{imprimir}/{arquivos[a]}", None, ".", 0)

        if arquivos[a] not in umavez:
            print("ENVIANDO SEGUNDA COPIA")
            win32api.ShellExecute(0, "print", f"{imprimir}/{arquivos[a]}", None, ".", 0)

        print("ESPERANDO 5 SEGUNDOS")
        time.sleep(5)
        print("TROCANDO PASTA DOS ARQUIVOS")

        movido = False

        while not movido:
            try:
                os.rename(f"{imprimir}/{arquivos[a]}", f"{impressos}/{arquivos[a]}")
                movido = True
            except(PermissionError):
                print("ENTROU EM EXCEPTION PERMISSION ERROR!! ESPERANDO 5 SEGUNOS")
                time.sleep(5)

        print("DANDO APPEND NA LISTA DE IMPRESSOS")
        arquivosImpressos.append(arquivos[a])
        time.sleep(3)
    except(IndexError):
        continue


# win32api.ShellExecute(0, "print", f"C:/Users/Usuário/Desktop/script/notas/pdf/imprimir/AÇOTEC 1753.pdf", None, ".", 0)

print("CHECAR NOTAS")
for b in arquivosImpressos:
    print(b)