import tkinter as tk
from tkinter import ttk
from functools import partial
import mysql.connector
from datetime import datetime, date

# ------------------------------------------------
#     GRID AGENDA
# ------------------------------------------------
class GridAgenda_2(ttk.Frame):
    def __init__(self, container, conn: mysql.connector.connection.MySQLConnection):
        super().__init__(container)

        # - DECLARAR VARIAVEIS -
        self.conn = conn
        self.visualizando_historico = False
        self.vars_controle = {
            #agenda
            False: {
                "texto_label": "AGENDA",
                "conta_page": 0,
                "pagina": 0,
                "string_lista_atual": "",
                "ultima_var_empresa": "",
                "ultima_var_mes": "",
                "ultima_var_ano": "",
                "ultima_var_numero": "",
                "ordena_dec": "",
                "heading_ativa": "", 
                "texto_heading_ativa": "",
                "index_heading_ativa": 0
            },
            #historico
            True: {
                "texto_label": "HISTÓRICO",
                "conta_page": 0,
                "pagina": 0,
                "string_lista_atual": "",
                "ultima_var_empresa": "",
                "ultima_var_mes": "",
                "ultima_var_ano": "",
                "ultima_var_numero": "",
                "ordena_dec": "",
                "heading_ativa": "",
                "texto_heading_ativa": "",
                "index_heading_ativa": 0
            }
        }
        self.listas = {
            False: {
                "todas": [],
                "lista_paginas": [[]]
                
            },
            True: {
                "todas": [],
                "lista_paginas": [[]]
            }
        }
        self.lista_pagar_notas = []
        # - EXECUTAR FUNÇÕES DE FRAMES E WIDGETS
        self.var_emp = tk.StringVar()
        self.var_mes = tk.StringVar()
        self.var_ano = tk.StringVar()
        self.var_numero = tk.StringVar()

        self.criar_frame_troca_hist_agenda()
        self.criar_frame_tabelas()
        self.criar_frame_filtros()



    # FUNÇOES PRA  CRIAR FRAMES
        # BOTOES TROCAR AGENDA HISTORICO 
    def criar_frame_troca_hist_agenda(self):
        self.grid_hist_agenda = ttk.Frame(self)
        self.grid_hist_agenda.grid(column=0, row=0, columnspan=3, sticky="ew", pady=30)
        for a in range(0, 2): self.grid_hist_agenda.grid_columnconfigure(a, weight=1)
        self.botao_agenda = ttk.Button(self.grid_hist_agenda, text="AGENDA", command=partial(self.trocar_view_tabela, False))
        self.botao_agenda.grid(column=0, row=0, sticky="e", padx=(0, 25))

        self.botao_historico = ttk.Button(self.grid_hist_agenda, text="HISTÓRICO", command=partial(self.trocar_view_tabela, True))
        self.botao_historico.grid(column=1, row=0, sticky="w", padx=(25, 0))

        # FRAME TABELAS
    def criar_frame_tabelas(self):
        self.grid_esquerda = ttk.Frame(self)
        self.grid_esquerda.grid(column=0, row=1, columnspan=2, sticky="ew", padx=(45, 20))
        for a in range(0, 3): self.grid_esquerda.grid_columnconfigure(a, weight=1)

        self.label_teste = ttk.Label(self.grid_esquerda, text="AGENDA")
        self.label_teste.grid(column=0, row=0, columnspan=3)

        self.grid_tabela = ttk.Frame(self.grid_esquerda)
        self.grid_tabela.grid(column=0, row=1, columnspan=3, sticky="nsew")
        for a in range(0, 3): self.grid_tabela.grid_columnconfigure(a, weight=1)

        self.grid_btn_label_tabela = ttk.Frame(self.grid_esquerda)
        self.grid_btn_label_tabela.grid(column=0, row=2, columnspan=3, sticky="nsew")
        for a in range(0, 3): self.grid_btn_label_tabela.grid_columnconfigure(a, weight=1)

        self.criar_tabela_agenda()
        self.listas[False]["todas"] = self.buscar_bd(self.conn, False, False)
        self.sort_heading(self.tabela_agenda, False, "venc", "Vencimento", 6)

        self.criar_tabela_historico()
        self.listas[True]["todas"] = self.buscar_bd(self.conn, True, False)
        self.sort_heading(self.tabela_hist, True, "pago_em", "Pago em:", 7)


        self.ant = ttk.Button(self.grid_btn_label_tabela, text="ANTERIOR", command=partial(self.trocar_pagina_tabela, False))
        self.qnt = ttk.Label(self.grid_btn_label_tabela, text="")
        self.prox = ttk.Button(self.grid_btn_label_tabela, text="PRÓXIMO", command=partial(self.trocar_pagina_tabela, True))
        self.ant.grid(row=0, column=0)
        self.qnt.grid(row=0, column=1)
        self.prox.grid(row=0, column=2)
        self.configurar_texto(False, "lista_paginas")


        #TABELA AGENDA
    def criar_tabela_agenda(self):
        self.colunas_agenda = ("NumeroCount", "nome", "num", "dataEmissao", "idDuplicata", "valor", "venc", "pago")
        self.nomes_agenda = ("", "Nome", "Número", "Emissão", "#", "Valor", "Vencimento", "Pago")
        self.largs_agenda = (55, 210, 130, 175, 55, 130, 100, 85)

        self.tabela_agenda = ttk.Treeview(self.grid_tabela, columns=self.colunas_agenda, show="headings", height=24)
        for a in range(len(self.colunas_agenda)):
            self.tabela_agenda.heading(self.colunas_agenda[a], text= self.nomes_agenda[a], command=partial(self.sort_heading, self.tabela_agenda, False, self.colunas_agenda[a], self.nomes_agenda[a], a))

            self.tabela_agenda.column(self.colunas_agenda[a], width= self.largs_agenda[a])

        self.tabela_agenda.grid(column=0, row=0, columnspan=3, sticky="nsew")
        self.tabela_agenda.bind("<<TreeviewSelect>>", self.buscar_notas_selecionadas)


    def criar_tabela_historico(self):
        self.colunas_hist = ("NumeroCount_h", "id_h", "nome_h", "num_h", "id_dup_h", "venc_h", "valor_h", "pago_em")
        self.nomes_hist = ("", "#", "Nome", "Número", "ID pagamento", "Vencimento", "Valor", "Pago em:")
        self.largs_hist = (55, 55, 200, 130, 95, 90, 90, 130)

        self.tabela_hist = ttk.Treeview(self.grid_tabela, columns=self.colunas_hist, show="headings", height=24)
        for a in range(len(self.colunas_hist)):
            self.tabela_hist.heading(self.colunas_hist[a], text= self.nomes_hist[a], command=partial(self.sort_heading, self.tabela_hist, True, self.colunas_hist[a], self.nomes_hist[a], a))

            self.tabela_hist.column(self.colunas_hist[a], width= self.largs_hist[a])

        self.tabela_hist.grid(column=0, row=0, columnspan=3, sticky="nsew")
        self.tabela_hist.lower()

    def criar_frame_filtros(self):
        self.frame_direita = ttk.Frame(self)
        self.frame_direita.grid(column=2, row=1, sticky="nsew", padx=(20, 45))
        self.frame_direita.grid_columnconfigure(0, weight=1)
        self.frame_buscar_notas = ttk.Frame(self.frame_direita)
        self.frame_buscar_notas.grid(column=0, row=0, sticky="nsew", pady=10)
        for a in range(0,3): self.frame_buscar_notas.grid_columnconfigure(a, weight=1)
        self.criar_radio_buttons()
        self.criar_frame_filtro_data()
        self.criar_frame_pagar()

    def criar_radio_buttons(self):
        self.botao_hoje = ttk.Button(self.frame_buscar_notas, text="NOTAS DE HOJE", command=partial(self.notas_hoje, self.conn))
        self.botao_hoje.grid(column=0, row=0, columnspan=3)

    def criar_frame_filtro_data(self):
        self.frame_filtro_data = tk.Frame(self.frame_direita)
        self.frame_filtro_data.grid(column=0, row=1, sticky="nsew", pady=10)
        for a in range(0,2): self.frame_filtro_data.grid_columnconfigure(a, weight=1)
        self.criar_filtro_data()

    def criar_filtro_data(self):
        self.label_empresa = ttk.Label(self.frame_filtro_data, text="Empresa: ")
        self.label_empresa.grid(column=0, row=0)

        self.label_numero = ttk.Label(self.frame_filtro_data, text="Número: ")
        self.label_numero.grid(column=0, row=1)

        self.label_mes = ttk.Label(self.frame_filtro_data, text="Mês: ")
        self.label_mes.grid(column=0, row=2)
        
        self.label_ano = ttk.Label(self.frame_filtro_data, text="Ano: ")
        self.label_ano.grid(column=0, row=3)

        self.entry_empresa = ttk.Entry(self.frame_filtro_data, textvariable=self.var_emp)
        self.entry_empresa.grid(column=1, row=0)

        self.entry_numero = ttk.Entry(self.frame_filtro_data, textvariable=self.var_numero)
        self.entry_numero.grid(column=1, row=1)

        self.entry_mes = ttk.Entry(self.frame_filtro_data, textvariable=self.var_mes)
        self.entry_mes.grid(column=1, row=2)

        self.entry_ano = ttk.Entry(self.frame_filtro_data, textvariable=self.var_ano)
        self.entry_ano.grid(column=1, row=3)

        self.botao_filtro = ttk.Button(self.frame_filtro_data, text="FILTRAR", command=self.filtrar_tabela)
        self.botao_filtro.grid(column=0, row=4, columnspan=2)

    def criar_frame_pagar(self):
        self.frame_pagar = ttk.Frame(self.frame_direita)
        for a in range(0,2): self.frame_pagar.grid_columnconfigure(a, weight=1)
        self.frame_pagar_2 = ttk.Frame(self.frame_pagar)
        self.frame_pagar.grid(column=0, row=2, sticky="nsew", pady=10)

        self.label_pagar = ttk.Label(self.frame_pagar, text="Marcar notas selecionadas\ncomo pagas:")
        self.label_pagar.grid(column=0, row=0, columnspan=2)

        self.botao_pagar = ttk.Button(self.frame_pagar, text="PAGAR", command=partial(self.pagar_notas, self.conn))
        self.botao_pagar.grid(column=0, row=1, columnspan=2)

        self.label_fantasma = ttk.Label(self.frame_pagar, text="")
        self.label_fantasma.grid(column=0, row=2, columnspan=2)

        self.frame_pagar_2.grid(column=0, row=3, sticky="nsew", columnspan=2)
        self.frame_pagar_2.grid_columnconfigure(0, weight=1)

    # METODOS
    def trocar_view_tabela(self, nova_bool_historico):
        mudou = nova_bool_historico != self.visualizando_historico
        if mudou:
            self.visualizando_historico = nova_bool_historico
            self.label_teste.config(text= self.vars_controle[self.visualizando_historico]["texto_label"])
            self.tabela_hist.tkraise() if nova_bool_historico else self.tabela_agenda.tkraise()

            self.configurar_texto(self.visualizando_historico, self.vars_controle[self.visualizando_historico]["string_lista_atual"])

    def buscar_bd(self, conn: mysql.connector.connection.MySQLConnection, historico: bool, hoje = False):
    
        #AGENDA "nome", "num", "dataEmissao", "idDuplicata", "valor", "venc", "pago"
        #HISTORICO "id_h", "nome_h", "num_h", "id_dup_h", "venc_h", "valor_h", "pago_em"


        empresa = self.vars_controle[historico]["ultima_var_empresa"]
        mes = self.vars_controle[historico]["ultima_var_mes"]
        ano = self.vars_controle[historico]["ultima_var_ano"]
        numero = self.vars_controle[historico]["ultima_var_numero"]

        if not historico:
            primeira_parte_query = '''SELECT
            IF(emp.customNome IS NOT NULL, emp.customNome, emp.nomeFantasia) AS nome,
            IF(numDuplicata <> "000", CONCAT(nfe.numeroNota, "-", numDuplicata), nfe.numeroNota) AS num,
            DATE_FORMAT(nfe.dataEmissao, "%d/%m/%Y %H:%i:%S") as dataEmissao,
            idDuplicata,
            REPLACE(CONCAT("R$ ", valor), ".", ",") as preco,
            DATE_FORMAT(venc, "%d/%m/%Y") AS vencimento,
            pago FROM
                duplicatas
                INNER JOIN notaFiscalEntrada AS nfe ON duplicatas.idNota = nfe.idNota
                INNER JOIN empresas as emp on emp.idEmpresa = nfe.empresa'''
        else:
            primeira_parte_query = '''SELECT
                    IDpg,
                    IF(emp.customNome IS NOT NULL, emp.customNome, emp.nomeFantasia) AS nome,
                    IF(dup.numDuplicata <> "000", CONCAT(nfe.numeroNota, "-", dup.numDuplicata), nfe.numeroNota) AS num,
                    hpg.IDduplicata,
                    DATE_FORMAT(dup.venc, "%d/%m/%Y") AS vencimento,
                    REPLACE(CONCAT("R$ ", dup.valor), ".", ",") as preco,
                    DATE_FORMAT(hpg.adicionadoEm, "%d/%m/%Y %H:%i:%S") as pago_em
                        FROM historicoPagamentos as hpg
                            INNER JOIN duplicatas as dup ON hpg.IDduplicata = dup.idDuplicata
                            INNER JOIN notaFiscalEntrada AS nfe ON dup.idNota = nfe.idNota
                            INNER JOIN empresas AS emp ON nfe.empresa = emp.idEmpresa'''
            
        if not hoje:
            empresa = False if empresa == "" else f'''nfe.empresa = (SELECT idEmpresa from empresas WHERE customNome LIKE "%{empresa}%" OR nomeFantasia LIKE "%{empresa}%" OR razaoSocial LIKE "%{empresa}%" LIMIT 1)'''

            numero = False if numero == "" else f"nfe.numeronota = '{numero}'" 

            mes = False if mes == "" else f"MONTH(venc) = {mes}"

            ano = False if ano == "" else f"YEAR(venc) = {ano}"

            lista_query = [empresa, numero, mes, ano]
            lista_juncoes = ["\nWHERE", "\nAND", "\nAND","\nAND"]
            cqv = 0 # conta_querys_verdadeiras

            for q in lista_query:
                if q != False:
                    primeira_parte_query += f"{lista_juncoes[cqv]} {q}"
                    cqv += 1
        else:
            s_hoje = "\nWHERE venc = CURDATE()"
            primeira_parte_query += s_hoje
        
        ordena = f"ORDER BY {'hpg.adicionadoEm' if historico else 'venc'} DESC"

        query_final = f"{primeira_parte_query}\n{ordena}"

        cursor = conn.cursor()

        cursor.execute(query_final)
        fetch = cursor.fetchall()

        resultado = fetch

        if not hoje:
            if not any(lista_query): self.vars_controle[historico]["string_lista_atual"] = "lista_paginas"

        return resultado
    
    def paginar(self, historico: bool, lista, string_lista):
        novalista = [[]]
        pagina = 0
        for num, a in enumerate(lista):
            if num % 25 == 0 and num > 1:
                pagina += 1
                novalista.append([])
            aa = tuple([num+1]) + a
            novalista[pagina].append(aa)
        
        self.listas[historico][string_lista] = novalista

    def mostrar_tabela(self, historico: bool, tabela: ttk.Treeview, num_pag, string_lista):
        tabela.delete(*tabela.get_children())

        for a, b in enumerate(self.listas[historico][string_lista][num_pag]):
            tabela.insert(parent='', index=a, values=b)
        
    def configurar_texto(self, historico: bool, string_lista):
        numero = self.vars_controle[historico]["conta_page"]

        pag_final = len(self.listas[historico][string_lista])

        len_itens_ultima_pagina = len(self.listas[historico][string_lista][pag_final-1])

        inicio = (numero * 25) + 1
        num_total_itens = (25 * (pag_final - 1)) + len_itens_ultima_pagina

        fim = inicio + 24 if numero+1 < pag_final else len_itens_ultima_pagina + inicio -1

        texto = f"{inicio} - {fim} DE {num_total_itens} (PÁGINA {numero+1} DE {pag_final})"

        self.qnt.config(text= texto)

    def trocar_pagina_tabela(self, aumenta: bool):
        historico = self.visualizando_historico
        string_lista = self.vars_controle[historico]["string_lista_atual"]
        tabela = self.tabela_hist if historico else self.tabela_agenda
        pagina_final = len(self.listas[historico][string_lista])-1
        n = self.vars_controle[historico]["conta_page"]
        nv_n = n + 1 if aumenta else n-1

        if 0 <= nv_n <= pagina_final:
            self.vars_controle[historico]["conta_page"] = nv_n
            self.mostrar_tabela(historico, tabela, nv_n, string_lista)
            self.configurar_texto(historico, string_lista)

    def filtrar_tabela(self):
        hist = self.visualizando_historico
        s_lista = self.vars_controle[hist]["string_lista_atual"]

        empresa = self.var_emp.get()
        mes = self.var_mes.get()
        ano = self.var_ano.get()
        num = self.var_numero.get()

        self.vars_controle[hist]["ultima_var_empresa"] = empresa
        self.vars_controle[hist]["ultima_var_mes"] = mes
        self.vars_controle[hist]["ultima_var_ano"] = ano
        self.vars_controle[hist]["ultima_var_numero"] = num

        lista = self.buscar_bd(self.conn, hist)
        lista = self.ordenar_lista(self.vars_controle[hist]["index_heading_ativa"], hist, lista, self.vars_controle[hist]["ordena_dec"])
        self.listas[hist]["todas"] = lista

        self.vars_controle[hist]["conta_page"] = 0
        self.paginar(hist, lista, s_lista)
        tabela = self.tabela_hist if hist else self.tabela_agenda
        self.mostrar_tabela(hist, tabela, self.vars_controle[hist]["conta_page"], s_lista)
        self.configurar_texto(hist, s_lista)
        
    def buscar_notas_selecionadas(self, a):
        notas_selecionadas = []
        selecionados = self.tabela_agenda.selection()

        for item in selecionados:
            curr_item = self.tabela_agenda.item(item)["values"]
            if curr_item not in notas_selecionadas:
                notas_selecionadas.append(curr_item)
        
        self.lista_pagar_notas = notas_selecionadas
        print(notas_selecionadas)
        print(self.lista_pagar_notas == notas_selecionadas)
        for a in notas_selecionadas: print(f"ID DA NOTA: {a[4]}")

    def pagar_notas(self, conn: mysql.connector.connection.MySQLConnection):

        cursor = conn.cursor()
        
        ids = []
        bools = []

        for a in self.lista_pagar_notas:
            booleano = 0 if a[7] == 1 else 1
            bv = booleano == 1
            id_dup = a[4]
            ids.append(id_dup)
            bools.append(booleano)

            sql = f'''UPDATE duplicatas
            SET pago = {booleano}
            WHERE idDuplicata = {id_dup}'''

            sql_hist = f'''INSERT INTO
            historicoPagamentos(IDduplicata, adicionadoEm)
            VALUES ({id_dup}, NOW())''' if bv else f'''DELETE FROM historicoPagamentos WHERE IDduplicata = {id_dup}'''

            cursor.execute(sql)
            cursor.execute(sql_hist)
        
        self.conn.commit()


        self.listas[False]["todas"] = self.buscar_bd(conn, False)
        self.paginar(False, self.listas[False]["todas"], "lista_paginas_2")
        self.mostrar_tabela(False, self.tabela_agenda, self.vars_controle[False]["conta_page"], "lista_paginas_2")

        self.listas[True]["todas"] = self.buscar_bd(conn, True)
        self.paginar(True, self.listas[True]["todas"], "lista_paginas_2")
        self.mostrar_tabela(True, self.tabela_hist, 0, "lista_paginas_2")
        self.vars_controle[True]["conta_page"] = 0

        self.trocar_view_tabela(False)

    def notas_hoje(self, conn: mysql.connector.connection.MySQLConnection):
        self.listas[False]["todas"] = self.buscar_bd(conn, False, True)
        self.paginar(False, self.listas[False]["todas"], "lista_paginas_2")
        self.mostrar_tabela(False, self.tabela_agenda, 0, "lista_paginas_2")

        self.trocar_view_tabela(False)

    def sort_heading(self, tabela: ttk.Treeview, historico: bool, nome_heading, texto_heading, index_sort):
        # venc Vencimento pago_em Pago Em:
        mudou = self.vars_controle[historico]["heading_ativa"] != nome_heading and index_sort != self.vars_controle[historico]["index_heading_ativa"]
        vazio = self.vars_controle[historico]["texto_heading_ativa"] == self.vars_controle[historico]["heading_ativa"] == self.vars_controle[historico]["ordena_dec"] == ""
        if mudou or vazio:
            self.vars_controle[historico]["ordena_dec"] = True
        else:
            self.vars_controle[historico]["ordena_dec"] = not self.vars_controle[historico]["ordena_dec"]

        nova_lista = self.ordenar_lista(int(index_sort), historico, self.listas[historico]["todas"], self.vars_controle[historico]["ordena_dec"])
        if nova_lista != None:
            self.vars_controle[historico]["conta_page"] = 0
            self.listas[historico]["todas"] = nova_lista
            self.paginar(historico, self.listas[historico]["todas"], "lista_paginas")
            self.mostrar_tabela(historico, tabela, 0, "lista_paginas")
            self.formatar_sort_heading(historico, tabela, mudou, vazio, nome_heading, texto_heading, index_sort, self.vars_controle[historico]["ordena_dec"])

    def formatar_sort_heading(self, historico, tabela: ttk.Treeview, mudou, vazio, nome_heading, texto_heading, index_sort, dec):
        if mudou:
            if not vazio: tabela.heading(self.vars_controle[historico]["heading_ativa"], text= self.vars_controle[historico]["texto_heading_ativa"])

            self.vars_controle[historico]["heading_ativa"] = nome_heading
            self.vars_controle[historico]["texto_heading_ativa"] = texto_heading
            self.vars_controle[historico]["index_heading_ativa"] = index_sort

        flecha = "↑Z-A" if dec else "↓A-Z"
        texto_formatado = f"{texto_heading} {flecha}"

        tabela.heading(nome_heading, text= texto_formatado)
    
    def ordenar_lista(self, index_sort, historico: bool, lista: list, desc: bool):
        #AGENDA "nome", "num", "dataEmissao", "idDuplicata", "valor", "venc", "pago"
        #HISTORICO "id_h", "nome_h", "num_h", "id_dup_h", "venc_h", "valor_h", "pago_em"
        if index_sort == 0:
            return None
        
        index_sort -= 1

        if (not historico and index_sort == 5) or (historico and index_sort == 4):
            nova_lista = sorted(lista, key= lambda linha: datetime.strptime(str(linha[index_sort]), "%d/%m/%Y"), reverse= desc)
        elif (not historico and index_sort == 2) or (historico and index_sort == 6):
            nova_lista = sorted(lista, key= lambda linha: datetime.strptime(linha[index_sort], "%d/%m/%Y %H:%M:%S"), reverse= desc)
        elif (not historico and index_sort in [3, 6]) or (historico and index_sort in [0, 3]):
            nova_lista = sorted(lista, key= lambda linha: int(linha[index_sort]), reverse= desc)
        elif (not historico and index_sort == 0) or (historico and index_sort == 1):
            nova_lista = sorted(lista, key= lambda linha: linha[index_sort], reverse= desc)
        elif (not historico and index_sort in [1, 4]) or (historico and index_sort in [2, 5]):
            nova_lista = sorted(lista, key= lambda linha: float(linha[index_sort].replace("R$ ", "").replace("-", "").replace(",",".")), reverse= desc)

        return nova_lista