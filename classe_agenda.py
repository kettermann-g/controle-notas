import tkinter as tk
from tkinter import ttk
from functools import partial
import mysql.connector
from datetime import datetime, date

# ------------------------------------------------
#     GRID AGENDA
# ------------------------------------------------
class GridAgenda(ttk.Frame):
    def __init__(self, container, conn: mysql.connector.connection.MySQLConnection):
        super().__init__(container)

        self.conn = conn
        self.lista_tuplas_sort = []
        self.cursor = self.conn.cursor()
        self.todas = self.buscarTodas(self.conn)
        self.filtro_tabela = ""
        self.filtro_pgto = ""
        self.c = 0
        self.conta_page = 0
        self.pagina = 0
        self.lista_paginas = [[]]
        self.lista_paginas_2 = [[]]

        self.todas_historico = self.buscar_todas_hist(self.conn)
        self.lista_historico = [[]]

        self.radio_var = tk.StringVar()
        self.var_emp = tk.StringVar()
        self.var_mes = tk.StringVar()
        self.var_ano = tk.StringVar()
        self.var_numero = tk.StringVar()

        self.visualizando_historico = False

        self.vars_controle = {
            False: {
                "filtro_tabela": "",
                "filtro_pgto": "",
                "c": 0,
                "conta_page": 0,
                "lista_paginas": [[]],
                "lista_paginas_2": [[]],
                "lista_tuplas_sort": [],
                "todas": self.buscarTodas(self.conn),
                "usar_pagina_dois": False
            }
        }
        self.usar_pagina_dois = False
        self.lista_pagar_notas = []

        self.ordena_dec = False

        self.heading_ativa = "venc"
        self.texto_heading_ativa = "Vencimento"

        self.criar_frame_hist_agenda()
        self.criar_tabela()
        self.criar_tabela_historico()
        self.criar_frame_buscar_notas()
        self.criar_frame_filtro_data()
        self.criar_frame_pagar()

    def buscarTodas(self, conn: mysql.connector.connection.MySQLConnection):
        cursor = conn.cursor()

        sql = '''SELECT
        IF(emp.customNome IS NOT NULL, emp.customNome, emp.nomeFantasia) AS nome,
        IF(numDuplicata <> "000", CONCAT(nfe.numeroNota, "-", numDuplicata), nfe.numeroNota) AS num,
        nfe.dataEmissao,
        idDuplicata,
        valor,
        venc,
        pago FROM
            duplicatas
            INNER JOIN notaFiscalEntrada AS nfe ON duplicatas.idNota = nfe.idNota
            INNER JOIN empresas as emp on emp.idEmpresa = nfe.empresa
                ORDER BY venc DESC'''

        cursor.execute(sql)
        fetch = cursor.fetchall()
        keys = cursor.column_names

        todas = list(map(lambda a: {keys[i]: a[i] for i in range(0, len(a))}, fetch))

        self.lista_tuplas_sort = todas

        return todas
    
    def trocar_tabela(self, trocar_para_historico: bool):
        mudou = trocar_para_historico != self.visualizando_historico
        if mudou:
            self.visualizando_historico = trocar_para_historico
            tf = {True: [self.tabela_hist, "HISTÓRICO"], False: [self.tabela, "AGENDA"]}
            frase = tf[trocar_para_historico][1]
            self.label_teste.config(text=frase)
            tf[trocar_para_historico][0].tkraise()
            tf[not trocar_para_historico][0].lower()

    def criar_tabela_historico(self):
        self.colunas_hist = ("NumeroCount_h", "id_h", "nome_h", "num_h", "id_dup_h", "venc_h", "valor_h", "pago_em")
        self.nomes_hist = ("", "#", "Nome", "Número", "ID duplicata", "Vencimento", "Valor", "Pago em:")
        self.largs_hist = (55, 55, 210, 130, 55, 100, 130, 100)
        self.tabela_hist = ttk.Treeview(self.grid_tabela, columns=self.colunas_hist, show="headings", height=24)
        for a in range(len(self.colunas_hist)):
            self.tabela_hist.heading(self.colunas_hist[a], text= self.nomes_hist[a])

            self.tabela_hist.column(self.colunas_hist[a], width= self.largs_hist[a])
        self.tabela_hist.grid(column=0, row=0, columnspan=3, sticky="nsew")
        self.tabela_hist.lower()

        self.mostrar_paginas(False, True)
        
    def buscar_todas_hist(self, conn: mysql.connector.connection.MySQLConnection):
        cursor = conn.cursor()

        sql = '''SELECT
                    IDpg,
                    IF(emp.customNome IS NOT NULL, emp.customNome, emp.nomeFantasia) AS nome,
                    IF(dup.numDuplicata <> "000", CONCAT(nfe.numeroNota, "-", dup.numDuplicata), nfe.numeroNota) AS num,
                    hpg.IDduplicata,
                    dup.valor,
                    dup.venc,
                    hpg.adicionadoEm
                        FROM historicoPagamentos as hpg
                            INNER JOIN duplicatas as dup ON hpg.IDduplicata = dup.idDuplicata
                            INNER JOIN notaFiscalEntrada AS nfe ON dup.idNota = nfe.idNota
                            INNER JOIN empresas AS emp ON nfe.empresa = emp.idEmpresa;'''
        
        cursor.execute(sql)
        fetch = cursor.fetchall()
        keys = cursor.column_names

        todas = list(map(lambda a: {keys[i]: a[i] for i in range(0, len(a))}, fetch))

        return todas


    
    def criar_frame_hist_agenda(self):
        self.grid_hist_agenda = ttk.Frame(self)
        self.grid_hist_agenda.grid(column=0, row=0, columnspan=3, sticky="ew", pady=30)
        for a in range(0, 2): self.grid_hist_agenda.grid_columnconfigure(a, weight=1)
        self.botao_agenda = ttk.Button(self.grid_hist_agenda, text="AGENDA", command=partial(self.trocar_tabela, False))
        self.botao_agenda.grid(column=0, row=0, sticky="e", padx=(0, 25))

        self.botao_historico = ttk.Button(self.grid_hist_agenda, text="HISTÓRICO", command=partial(self.trocar_tabela, True))
        self.botao_historico.grid(column=1, row=0, sticky="w", padx=(25, 0))

        self.paginar(self.todas_historico, False, True)

        print("TESTE TODAS HISTORICO ", self.lista_historico)


    def criar_tabela(self):
        self.grid_esquerda = ttk.Frame(self)
        self.grid_esquerda.grid(column=0, row=1, columnspan=2, sticky="ew", padx=(45, 20))

        for a in range(0, 3): self.grid_esquerda.grid_columnconfigure(a, weight=1)
        self.label_teste = ttk.Label(self.grid_esquerda, text="AGENDA")
        self.label_teste.grid(column=0, row=0, columnspan=3)
        self.colunas = ("NumeroCount", "nome", "num", "dataEmissao", "idDuplicata", "valor", "venc", "pago")
        self.nomes = ("", "Nome", "Número", "Emissão", "#", "Valor", "Vencimento", "Pago")
        self.largs = (55, 210, 130, 175, 55, 130, 100, 85)
        self.grid_tabela = ttk.Frame(self.grid_esquerda)
        self.grid_tabela.grid(column=0, row=1, columnspan=3, sticky="nsew")
        self.grid_btn_label_tabela = ttk.Frame(self.grid_esquerda)
        for a in range(0, 3): self.grid_btn_label_tabela.grid_columnconfigure(a, weight=1)
        self.grid_btn_label_tabela.grid(column=0, row=2, columnspan=3, sticky="nsew")
        self.tabela = ttk.Treeview(self.grid_tabela, columns=self.colunas, show="headings", height=24)
        self.tabela.bind("<<TreeviewSelect>>", self.buscar_notas_selecionadas)
        for a in range(len(self.colunas)):
            self.tabela.heading(self.colunas[a], text= self.nomes[a], command= partial(self.sort_heading, self.colunas[a], self.nomes[a]))

            self.tabela.column(self.colunas[a], width= self.largs[a])

        self.tabela.grid(column=0, row=0, columnspan=3, sticky="nsew")

        self.ant = ttk.Button(self.grid_btn_label_tabela, text="ANTERIOR", command=partial(self.troca_pagina_agenda, "menos"))
        self.qnt = ttk.Label(self.grid_btn_label_tabela, text="")
        self.prox = ttk.Button(self.grid_btn_label_tabela, text="PRÓXIMO", command=partial(self.troca_pagina_agenda, "mais"))
        self.ant.grid(row=0, column=0)
        self.qnt.grid(row=0, column=1)
        self.prox.grid(row=0, column=2)


    def criar_frame_buscar_notas(self):
        self.frame_direita = ttk.Frame(self)
        self.frame_direita.grid(column=2, row=1, sticky="nsew", padx=(20, 45))
        self.frame_direita.grid_columnconfigure(0, weight=1)
        self.frame_buscar_notas = ttk.Frame(self.frame_direita)
        self.frame_buscar_notas.grid(column=0, row=0, sticky="nsew", pady=10)
        for a in range(0,3): self.frame_buscar_notas.grid_columnconfigure(a, weight=1)

        self.r1 = ttk.Radiobutton(self.frame_buscar_notas, text="Todas", variable=self.radio_var, value="X", command=self.notas_pagas)
        self.r1.grid(column=0, row=2)

        self.r2 = ttk.Radiobutton(self.frame_buscar_notas, text="Pagar", variable=self.radio_var, value="pagar", command=self.notas_pagas)
        self.r2.grid(column=1, row=2)

        self.r3 = ttk.Radiobutton(self.frame_buscar_notas, text="Pagas", variable=self.radio_var, value="pagas", command=self.notas_pagas)
        self.r3.grid(column=2, row=2)

        self.botao2 = ttk.Button(self.frame_buscar_notas, text="BUSCAR TODAS AS NOTAS", command=self.mostrarTodas)
        self.botao2.grid(column=0, row=0, columnspan=3)
        self.botao_hoje = ttk.Button(self.frame_buscar_notas, text="NOTAS DE HOJE", command=partial(self.filtra_mes_ano, "venc_hoje"))
        self.botao_hoje.grid(column=0, row=1, columnspan=3)

    def criar_frame_filtro_data(self):
        self.frame_filtro_data = tk.Frame(self.frame_direita)
        self.frame_filtro_data.grid(column=0, row=1, sticky="nsew", pady=10)
        for a in range(0,2): self.frame_filtro_data.grid_columnconfigure(a, weight=1)
        self.label_empresa = ttk.Label(self.frame_filtro_data, text="Empresa: ").grid(column=0, row=0)
        self.label_numero = ttk.Label(self.frame_filtro_data, text="Número: ").grid(column=0, row=1)
        self.label_mes = ttk.Label(self.frame_filtro_data, text="Mês: ").grid(column=0, row=2)
        self.label_ano = ttk.Label(self.frame_filtro_data, text="Ano: ").grid(column=0, row=3)

        self.entry_empresa = ttk.Entry(self.frame_filtro_data, textvariable=self.var_emp).grid(column=1, row=0)
        self.entry_numero = ttk.Entry(self.frame_filtro_data, textvariable=self.var_numero).grid(column=1, row=1)
        self.entry_mes = ttk.Entry(self.frame_filtro_data, textvariable=self.var_mes).grid(column=1, row=2)
        self.entry_ano = ttk.Entry(self.frame_filtro_data, textvariable=self.var_ano).grid(column=1, row=3)

        self.botao_filtro = ttk.Button(self.frame_filtro_data, text="FILTRAR", command=partial(self.filtra_mes_ano, "venc")).grid(column=0, row=4, columnspan=2)

    def criar_frame_pagar(self):
        self.frame_pagar = ttk.Frame(self.frame_direita)
        for a in range(0,2): self.frame_pagar.grid_columnconfigure(a, weight=1)
        self.frame_pagar_2 = ttk.Frame(self.frame_pagar)
        self.frame_pagar.grid(column=0, row=2, sticky="nsew", pady=10)
        self.label_pagar = ttk.Label(self.frame_pagar, text="Marcar notas selecionadas\ncomo pagas:")
        self.label_pagar.grid(column=0, row=0, columnspan=2)
        self.botao_pagar = ttk.Button(self.frame_pagar, text="PAGAR", command=self.confirmar_pagar_notas).grid(column=0, row=1, columnspan=2)
        self.label_fantasma = ttk.Label(self.frame_pagar, text="")
        self.label_fantasma.grid(column=0, row=2, columnspan=2)
        self.frame_pagar_2.grid(column=0, row=3, sticky="nsew", columnspan=2)
        self.frame_pagar_2.grid_columnconfigure(0, weight=1)

    def texto_paginas(self, num, len_lista, usar_dois = False):
        numFinalLen = len(self.lista_paginas_2) if usar_dois else len(self.lista_paginas)
        return f"{(25*num) - 24} - {25*num if len_lista>num*25 else len_lista} DE {len_lista} (PAGINA {num} de {numFinalLen})"
    
    
    def filtra_mes_ano(self, tipo):
        self.conta_page=0

        mes = self.var_mes.get() if self.var_mes.get().isdigit() else ""
        ano = self.var_ano.get() if self.var_ano.get().isdigit() else ""
        emp = self.var_emp.get()
        numero = self.var_numero.get() if self.var_numero.get().replace("-", "").isdigit() else ""

        tem_mes = mes != ""
        tem_ano = ano != ""
        tem_emp = emp != ""
        tem_numero = numero != ""

        self.pagina = 0

        valido = {"emi", "venc", "venc_hoje"}
        if tipo not in valido:
            raise ValueError("Os únicos valores aceitados são 'emi' para data de emissão e 'venc' para data de vencimento.")
         
        self.lista_paginas = [[]]
        if tipo == "venc":
            self.filtro_tabela = "mes_ano_empresa_venc"
            if tem_mes and tem_ano:
                filtro = list(filter(lambda a: a["venc"].month == int(mes) and a["venc"].year == int(ano), self.todas))
            elif tem_ano and not tem_mes:
                filtro = list(filter(lambda a: a["venc"].year == int(ano), self.todas))
            elif not tem_ano and not tem_mes:
                filtro = self.todas
        elif tipo == "venc_hoje":
            self.filtro_tabela = "filtro_venc_hoje"
            filtro = list(filter(lambda a: a["venc"] == date.today(), self.todas))

        if tem_emp and tipo != "venc_hoje": filtro = list(filter(lambda a: emp.lower() in a["nome"].lower(), filtro))

        if tem_numero: filtro = list(filter(lambda a: numero in a["num"], filtro))

        self.lista_tuplas_sort = filtro

        for a in range (0, len(filtro)):

            n = {"n": a+1}
            n.update(filtro[a])
            n["venc"] = datetime.strftime(n["venc"], "%d/%m/%Y")
            n["dataEmissao"] = datetime.strftime(n["dataEmissao"], "%d/%m/%Y %H:%M:%S")
            n["valor"] = f"R$ {n['valor'].replace('.', ',')}"
            tupla = tuple(n.values())
            
            if a > 1:
                if a % 25 == 0: 
                    self.lista_paginas.append([])
                    self.pagina += 1
            self.lista_paginas[self.pagina].append(tupla)

        self.tabela.delete(*self.tabela.get_children())

        for a, b in enumerate(self.lista_paginas[0]):
            self.tabela.insert(parent='', index=a, values=b)

        len_total_paginas = 0
        for a in self.lista_paginas: len_total_paginas += len(a)
        self.qnt.config(text=self.texto_paginas(self.conta_page+1, len_total_paginas))

    def paginar(self, lista, dois: bool, historico = False):

        lista_de_tuplas = all(isinstance(x, tuple) for x in lista)
        

        self.conta_page = 0
        self.pagina = 0

        if not historico:
            if not dois: self.lista_paginas = [[]]
            self.lista_paginas_2 = [[]]
        else:
            self.lista_historico = [[]]


        for a in range (0, len(lista)):
            if not lista_de_tuplas:
                n = {"n": a+1}
                n.update(lista[a])
                n["venc"] = datetime.strftime(n["venc"], "%d/%m/%Y")
                chave = "dataEmissao" if not historico else "adicionadoEm"
                n[chave] = datetime.strftime(n[chave], "%d/%m/%Y %H:%M:%S")
                n["valor"] = f"R$ {n['valor'].replace('.', ',')}"
                tupla = tuple(n.values())

            else:
                tupla = lista[a]
            if a > 1:
                if a % 25 == 0: 
                    if not historico:
                        self.lista_paginas_2.append([]) if dois else self.lista_paginas.append([])
                    else:
                        self.lista_historico.append([])
                    self.pagina += 1
            if not historico:
                self.lista_paginas_2[self.pagina].append(tupla) if dois else self.lista_paginas[self.pagina].append(tupla)
            else:
                self.lista_historico[self.pagina].append(tupla)

    def mostrar_paginas(self, dois: bool, historico: bool):

        tabelas = {False: self.tabela, True: self.tabela_hist}
        listas = {False: {False: self.lista_paginas, True: self.lista_paginas_2}, True: {False: self.lista_historico}}

        tabelas[historico].delete(*tabelas[historico].get_children())


        for a, b in enumerate(listas[historico][dois][0]):
            tabelas[historico].insert(parent='', index=a, values=b)

        len_total_paginas = 0
        for a in listas[historico][dois]: len_total_paginas += len(a)

        self.qnt.config(text=self.texto_paginas(self.conta_page+1, len_total_paginas, self.usar_pagina_dois))

    def mostrarTodas(self):

        self.filtro_tabela = ""
        self.filtro_pgto = ""
        self.conta_page=0

        self.pagina = 0
        self.lista_paginas = [[]]

        self.paginar(self.todas, False)
        self.mostrar_paginas(False, False)
        self.sort_heading(self.heading_ativa, self.texto_heading_ativa, True)

    def notas_pagas(self):

        v = self.radio_var.get()

        todas_local_paginadas = []
        # uma lista (fora)
        # com listas (meio - paginas)
        # com itens (listas (dentro))

        if v == "pagar":
            self.filtro_pgto = "filtro_apenas_pagar"

            for a in self.lista_paginas:
                for b in a:
                    if list(b)[7] == 0:
                        todas_local_paginadas.append(b)
            self.usar_pagina_dois = True
            self.paginar(todas_local_paginadas, self.usar_pagina_dois)
            self.mostrar_paginas(True)

        if v == "pagas":
            self.filtro_pgto = "filtro_apenas_pagar"

            for a in self.lista_paginas:
                for b in a:
                    if list(b)[7] == 1:
                        todas_local_paginadas.append(b)

            self.usar_pagina_dois = True
            self.paginar(todas_local_paginadas, self.usar_pagina_dois)
            self.mostrar_paginas(True)
        if v == "X":

            self.filtro_pgto = ""
            print("ENTROU NA CONDIÇAO MOSTRAR TODAS AS NOTAS")
            print(self.lista_paginas)
            self.usar_pagina_dois = False
            self.mostrar_paginas(self.usar_pagina_dois)

    def buscar_notas_selecionadas(self, a):
        notas_selecionadas = []
        selecionados = self.tabela.selection()

        for item in selecionados:
            curr_item = self.tabela.item(item)["values"]
            if curr_item not in notas_selecionadas:
                notas_selecionadas.append(curr_item)
        
        self.lista_pagar_notas = notas_selecionadas
        print(notas_selecionadas)
        print(self.lista_pagar_notas == notas_selecionadas)
        for a in notas_selecionadas: print(f"ID DA NOTA: {a[4]}")

    def confirmar_pagar_notas(self):
        lista_child = [self.frame_pagar_2.children[a] for a in self.frame_pagar_2.children]
        if len(lista_child) > 0:
            for a in lista_child:
                a.destroy()

        for num, a in enumerate(self.lista_pagar_notas):
            self.label = ttk.Label(self.frame_pagar_2, text=f"{a[1]} {a[2]} {a[5]}").grid(column=0, row=num)
        
        lastrow = len(self.lista_pagar_notas)
        self.confirmar = ttk.Button(self.frame_pagar_2, text="CONFIRMAR", command=self.pagar_notas).grid(column=0, row=lastrow)

    def pagar_notas(self):
        lastrow = len(self.lista_pagar_notas) + 3
        texto = "Atualizando..."

        self.label_fantasma.config(text = "")
        self.label_fantasma.update_idletasks()
        self.label_fantasma.config(text = texto)
        self.label_fantasma.update_idletasks()

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

            self.cursor.execute(sql)
            self.cursor.execute(sql_hist)
        
        self.conn.commit()

        lista_child = [self.frame_pagar_2.children[a] for a in self.frame_pagar_2.children]
        if len(lista_child) > 0:
            for a in lista_child:
                a.destroy()
        
        self.todas = self.buscarTodas(self.conn)

        # mostrarTodas()

        if self.filtro_tabela == "mes_ano_empresa_venc":
            self.filtra_mes_ano("venc")
            if self.filtro_pgto == "filtro_apenas_pagar":
                print("entoru na condiçao filtro apenas pagar")
                self.notas_pagas()
            self.label_fantasma.config(text = "")
        elif self.filtro_tabela == "filtro_venc_hoje":
            self.filtra_mes_ano("venc_hoje")
            if self.filtro_pgto == "filtro_apenas_pagar":
                print("entoru na condiçao filtro apenas pagar")
                self.notas_pagas()
        elif self.filtro_tabela != "mes_ano_empresa_venc" and self.filtro_tabela != "filtro_venc_hoje" and self.filtro_pgto == "filtro_apenas_pagar":
            print("ENTROU IF FILTRO TABELA VAZIO AND FILTRO PGTO APENAS PAGAR")
            self.mostrarTodas()
            self.notas_pagas()

        else:
            self.mostrarTodas()

        print(self.filtro_pgto, self.filtro_tabela)

        self.label_fantasma.config(text = "")

    def troca_pagina_agenda(self, tipo):
        self.tabela.delete(*self.tabela.get_children())

        if not self.usar_pagina_dois:
            if tipo == "mais":
                if self.conta_page < len(self.lista_paginas)-1 and len(self.lista_paginas)>0:
                    self.conta_page += 1
                    
            elif tipo == "menos":
                if self.conta_page > 0:
                    self.conta_page -= 1

            for a, b in enumerate(self.lista_paginas[self.conta_page]):
                self.tabela.insert(parent='', index=a, values=b)
            
            len_total_paginas = 0
            for a in self.lista_paginas: len_total_paginas += len(a)
            self.qnt.config(text=self.texto_paginas(self.conta_page+1, len_total_paginas))
        else:
            if tipo == "mais":
                if self.conta_page < len(self.lista_paginas_2)-1 and len(self.lista_paginas_2)>0:
                    self.conta_page += 1
                    
            elif tipo == "menos":
                if self.conta_page > 0:
                    self.conta_page -= 1

            for a, b in enumerate(self.lista_paginas_2[self.conta_page]):
                self.tabela.insert(parent='', index=a, values=b)
            
            len_total_paginas = 0
            for a in self.lista_paginas_2: len_total_paginas += len(a)
            self.qnt.config(text=self.texto_paginas(self.conta_page+1, len_total_paginas, True))

    def sort_heading(self, nome_heading, texto_heading, dec_forcado = False):
        self.conta_page = 0
        print(nome_heading, texto_heading)
        if nome_heading != "NumeroCount":
            trocou = nome_heading != self.heading_ativa
            if trocou and not dec_forcado:
                self.tabela.heading(self.heading_ativa, text= self.texto_heading_ativa)
                self.ordena_dec = True
                txt = f"{texto_heading} ↑Z-A"
                self.texto_heading_ativa = texto_heading
                self.heading_ativa = nome_heading
                self.tabela.heading(nome_heading, text= txt)

            elif dec_forcado:
                self.tabela.heading(self.heading_ativa, text= self.texto_heading_ativa)
                self.texto_heading_ativa = texto_heading
                self.heading_ativa = nome_heading
                self.ordena_dec = True
                flecha = "↑Z-A"
                self.tabela.heading(nome_heading, text= f"{texto_heading} {flecha}")

            else:
                self.ordena_dec = not self.ordena_dec
                flecha = "↑Z-A" if self.ordena_dec else "↓A-Z"
                self.tabela.heading(nome_heading, text= f"{texto_heading} {flecha}")
            
            if nome_heading != "num" and nome_heading != "valor":
                nova_lista = sorted(self.lista_tuplas_sort, key= lambda x: x[nome_heading], reverse= self.ordena_dec)
            elif nome_heading == "num":
                nova_lista = sorted(self.lista_tuplas_sort, key= lambda x: int(x["num"].split("-", 1)[0]), reverse= self.ordena_dec)
            elif nome_heading == "valor":
                nova_lista = sorted(self.lista_tuplas_sort, key= lambda x: float(x["valor"].replace(",",".")), reverse= self.ordena_dec)

            self.paginar(nova_lista, True)

            self.tabela.delete(*self.tabela.get_children())

            for a, b in enumerate(self.lista_paginas_2[self.conta_page]):
                self.tabela.insert(parent='', index=a, values=b)
            
            len_total_paginas = 0
            for a in self.lista_paginas_2: len_total_paginas += len(a)
            self.qnt.config(text=self.texto_paginas(self.conta_page+1, len_total_paginas))