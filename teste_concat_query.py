c = 0
for a in range(0, 100):
    f = input("SINAL: ")
    if f != "x":
        aumenta = f == "+"
        if aumenta: n= c+1
        else: n=c-1
        if 0 < n < 10: c = n
        print(c)
    else:
        break
# primeira_metade_sql = '''SELECT
#         IF(emp.customNome IS NOT NULL, emp.customNome, emp.nomeFantasia) AS nome,
#         IF(numDuplicata <> "000", CONCAT(nfe.numeroNota, "-", numDuplicata), nfe.numeroNota) AS num,
#         nfe.dataEmissao,
#         idDuplicata,
#         valor,
#         venc,
#         pago FROM
#             duplicatas
#             INNER JOIN notaFiscalEntrada AS nfe ON duplicatas.idNota = nfe.idNota
#             INNER JOIN empresas as emp on emp.idEmpresa = nfe.empresa'''

# print("INPUTS: VAZIO PARA IGNORAR")
# empresa = input("Insira empresa: ")
# empresa = False if empresa == "" else f'''nfe.empresa = (SELECT idEmpresa from empresas WHERE customNome LIKE "%{empresa}%" OR nomeFantasia LIKE "%{empresa}%" OR razaoSocial LIKE "%{empresa}%" LIMIT 1)'''

# num = input("Insira num: ")
# num = False if num == "" else f"nfe.numeronota = '{num}'" 

# mes = input("Insira mes: ")
# mes = False if mes == "" else f"MONTH(venc) = {mes}"

# ano = input("Insira ano: ")
# ano = False if ano == "" else f"YEAR(venc) = {ano}"

# lista_query = [empresa, num, mes, ano]
# lista_juncoes = ["\nWHERE", "\nAND", "\nAND","\nAND"]
# cqv = 0 # conta_querys_verdadeiras

# for q in lista_query:
#     if q != False:
#         primeira_metade_sql += f"{lista_juncoes[cqv]} {q}"
#         cqv += 1

# query_final = f"{primeira_metade_sql}\nORDER BY venc DESC"

# print(query_final)