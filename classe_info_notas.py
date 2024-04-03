import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from functools import partial
import mysql.connector
from datetime import datetime, date, timedelta
import time
import os
from funcoes import conectar, buscarTodas

# ARGS KWARGS https://pythonacademy.com.br/blog/args-e-kwargs-do-python

# https://blog.teclado.com/tkinter-placeholder-entry-field/
class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder

        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"

    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"

class GridInfoNotas(ttk.Frame):
    def __init__(self, container, conn: mysql.connector.connection.MySQLConnection):
        super().__init__(container)

        self.conn = conn
        self.cursor = conn.cursor()
        self.lista_paginas = [[]]
        self.lista_paginas_2 = [[]]
        self.isfloat = lambda x: str(x).count(".") == 1 and str(x).replace(".", "").isdigit() and all((not str(x).endswith("."), not str(x).startswith(".")))

        self.f = lambda x: str(x)[:str(x).index(".")+3] if all((self.isfloat(x), len(str(x).rsplit(".", 1)[-1]) >= 2)) else x

        self.usar_pagina_2 = False
        self.conta_paginas = 0
        self.conta_paginas_paginar = 0
        self.ordena_dec = False
        self.todas = []
        self.lista_tuplas_sort = []
        self.len_total_paginas = 0
        self.heading_ativa = "dataEmissao"
        self.texto_heading_ativa = "Emissão"
        self.lista_tuplas_filtro = []
        self.imprimir_copias = tk.StringVar(value=1)
        self.nota_selecionada = []

        self.criarTreeviewSelecNotas()
        self.criarFrameMostrar()
        self.criar_frame_info_notas()

        self.mostrar_notas_tabela_esquerda("todas")

    def sort_heading(self, nome_heading, texto_heading, dec_forcado = False):
        
        if nome_heading != "NumeroCount":
            trocou = nome_heading != self.heading_ativa
            if trocou and not dec_forcado:
                self.tabela_selec.heading(self.heading_ativa, text= self.texto_heading_ativa)
                self.ordena_dec = True
                txt = f"{texto_heading} ↑Z-A"
                self.texto_heading_ativa = texto_heading
                self.heading_ativa = nome_heading
                self.tabela_selec.heading(nome_heading, text= txt)

            elif dec_forcado:
                self.tabela_selec.heading(self.heading_ativa, text= self.texto_heading_ativa)
                self.texto_heading_ativa = texto_heading
                self.heading_ativa = nome_heading
                self.ordena_dec = True
                flecha = "↑Z-A"
                self.tabela_selec.heading(nome_heading, text= f"{texto_heading} {flecha}")

            else:
                self.ordena_dec = not self.ordena_dec
                flecha = "↑Z-A" if self.ordena_dec else "↓A-Z"
                self.tabela_selec.heading(nome_heading, text= f"{texto_heading} {flecha}")
            
            nn = self.colunas.index(nome_heading)
            if nn == 4:
                nova_lista = sorted(self.lista_tuplas_sort, key= lambda x: datetime.strptime(x[nn], "%d/%m/%Y %H:%M:%S"), reverse= self.ordena_dec)

            else:
                nova_lista = sorted(self.lista_tuplas_sort, key= lambda x: x[nn], reverse= self.ordena_dec)
            self.paginar(nova_lista, True)

            self.tabela_selec.delete(*self.tabela_selec.get_children())

            for a, b in enumerate(self.lista_paginas[self.conta_paginas]):
                self.tabela_selec.insert(parent='', index=a, values=b)
            
            len_total_paginas = 0
            for a in self.lista_paginas: len_total_paginas += len(a)
            self.label_txt_page.config(text=self.texto_paginas(self.conta_paginas+1, len_total_paginas))

    def criarTreeviewSelecNotas(self):
        self.frame_selec = ttk.Frame(self)
        self.frame_selec.grid_columnconfigure(0, weight=1)
        self.frame_selec.grid(column=0, row=0, padx=(25, 10))

        self.frame_entry = ttk.Frame(self.frame_selec, width=500)
        self.frame_entry.grid(column=0, row=0)
        self.frame_entry.grid_columnconfigure(4, weight=1)
        for a in range(0, 4): self.frame_entry.grid_columnconfigure(a, weight=2)

        self.var_emp = tk.StringVar()
        self.var_mes = tk.StringVar()
        self.var_ano = tk.StringVar()
        self.var_numero = tk.StringVar()

        self.entry_empresa = PlaceholderEntry(self.frame_entry, "Empresa", textvariable= self.var_emp)
        self.entry_empresa.grid(column=0, row=0, sticky="nsew")

        self.entry_numero_nota = PlaceholderEntry(self.frame_entry, "Número", textvariable= self.var_numero)
        self.entry_numero_nota.grid(column=1, row=0, sticky="nsew")

        self.entry_mes = PlaceholderEntry(self.frame_entry, "Mês", textvariable= self.var_mes)
        self.entry_mes.grid(column=2, row=0, sticky="nsew")
        
        self.entry_ano = PlaceholderEntry(self.frame_entry, "Ano", textvariable= self.var_ano)
        self.entry_ano.grid(column=3, row=0, sticky="nsew")

        self.botao_filtrar = ttk.Button(self.frame_entry, text="Filtrar", command=partial(self.mostrar_notas_tabela_esquerda, "", True))
        self.botao_filtrar.grid(column=4, row=0, sticky="nsew")

        self.frame_tabela = ttk.Frame(self.frame_selec)
        self.frame_tabela.grid_columnconfigure(0, weight=1)
        self.frame_tabela.grid(column=0, row=1)

        self.colunas = ("NumeroCount", "idNota", "nome", "numeroNota", "dataEmissao", "impresso")
        self.widths = (35, 60, 240, 90, 155, 65)
        self.nomes = (" ", "#", "Nome", "Número", "Emissão", "Imp.")

        self.tabela_selec = ttk.Treeview(self.frame_tabela, columns=self.colunas, show="headings", height=24)
        for num, a in enumerate(self.colunas):
            self.tabela_selec.heading(a, text= self.nomes[num], command= partial(self.sort_heading, a, self.nomes[num]))
            self.tabela_selec.column(a, width=self.widths[num])
        
        self.tabela_selec.grid(column=0, row=0, sticky="nsew")
        self.tabela_selec.bind("<ButtonRelease-1>", self.buscar_infos_unica_nota)
        self.tabela_selec.bind("<KeyRelease-Up>", self.buscar_infos_unica_nota)
        self.tabela_selec.bind("<KeyRelease-Down>", self.buscar_infos_unica_nota)

        self.frame_nav_page = ttk.Frame(self.frame_selec)
        for a in range(0, 3): self.frame_nav_page.grid_columnconfigure(a, weight=1)
        self.frame_nav_page.grid(column=0, row=2, sticky="nsew")

        self.botao_ant = ttk.Button(self.frame_nav_page, text="ANTERIOR", command=partial(self.troca_pagina_info_nota, "menos"))
        self.botao_ant.grid(column=0, row=0)

        self.label_txt_page = ttk.Label(self.frame_nav_page, text="XX-XX DE XXX (PÁGINA X DE XX)")
        self.label_txt_page.grid(column=1, row=0, padx=35)

        self.botao_prox = ttk.Button(self.frame_nav_page, text="PRÓXIMA", command=partial(self.troca_pagina_info_nota, "mais"))
        self.botao_prox.grid(column=2, row=0)
    
    def criarFrameMostrar(self):
        self.frame_mostrar = tk.Frame(self)
        self.frame_mostrar.grid(column=1, row=0, sticky="nsew", columnspan=2, padx=(10, 25))
        self.frame_mostrar.grid_columnconfigure(0, weight=1)

        self.frame_info_texto = ttk.Frame(self.frame_mostrar)
        self.frame_info_texto.grid(column=0, row=0, sticky="nsew")
        self.frame_info_texto.grid_columnconfigure(0, weight=1)

        self.frame_info_1 = ttk.Frame(self.frame_info_texto)
        self.frame_info_1.grid(column=0, row=0, sticky="nsew")
        for a in range (0, 3): self.frame_info_1.grid_columnconfigure(a, weight=1)
        self.label_nome_custom = ttk.Label(self.frame_info_1, text="Nome pers.: ", wraplength=235)
        self.label_nome_custom.grid(column=0, row=0, sticky="nsew", pady=4)
        self.label_fant = ttk.Label(self.frame_info_1, text="Nome Fantasia: ", wraplength=235)
        self.label_fant.grid(column=1, row=0, sticky="nsew", pady=4)
        self.label_soc = ttk.Label(self.frame_info_1, text="Razão Social: ", wraplength=235)
        self.label_soc.grid(column=2, row=0, sticky="nsew", pady=4)

        self.frame_info_2 = ttk.Frame(self.frame_info_texto)
        self.frame_info_2.grid(column=0, row=1, sticky="nsew")
        self.frame_info_2.grid_columnconfigure(0, weight=1)
        self.frame_info_2.grid_columnconfigure(1, weight=1)
        self.frame_info_2.grid_columnconfigure(2, weight=1)
        self.label_numero_nota = ttk.Label(self.frame_info_2, text="Número: ", wraplength=200)
        self.label_numero_nota.grid(column=0, row=0, sticky="nsew", pady=4)
        self.label_valor_total = ttk.Label(self.frame_info_2, text="Valor Total: R$", wraplength=200)
        self.label_valor_total.grid(column=1, row=0, sticky="nsew", pady=4)
        self.label_emi = ttk.Label(self.frame_info_2, text="Emissao: ", wraplength=200)
        self.label_emi.grid(column=2, row=0, sticky="nsew", pady=4)
        self.label_cfop = ttk.Label(self.frame_info_2, text="CFOP: ", wraplength= 600)
        self.label_cfop.grid(column=0, row=1, sticky="nsew", columnspan=3, pady=4)

        self.frame_info_3 = ttk.Frame(self.frame_info_texto)
        self.frame_info_3.grid(column=0, row=2, sticky="nsew")
        self.frame_info_3.grid_columnconfigure(0, weight=1)
        self.frame_info_3.grid_columnconfigure(1, weight=1)

        self.label_remetente = ttk.Label(self.frame_info_3, text="Remetente: ", wraplength=250)
        self.label_remetente.grid(column=0, row=0, sticky="nsew", pady=4)
        self.label_data_email = ttk.Label(self.frame_info_3, text="Recebido em: ", wraplength=250)
        self.label_data_email.grid(column=1, row=0, sticky="nsew", pady=4)

        self.label_adicionado = ttk.Label(self.frame_info_3, text="Adicionado Em: ", wraplength=500)
        self.label_adicionado.grid(column=0, row=1, sticky="nsew", pady=4)

        self.frame_imprimir_nota = ttk.Frame(self.frame_info_3)
        self.frame_imprimir_nota.grid(column=1, row=1, sticky="nsew")

        self.label_impresso = ttk.Label(self.frame_imprimir_nota, text="Impresso: ", wraplength=250)
        self.label_impresso.grid(column=0, row=0, sticky="nsew", pady=4, padx= (0, 15))

        self.botao_imprimir = ttk.Button(self.frame_imprimir_nota, text= "IMPRIMIR", command=self.imprimir_nota_selecionada)
        self.botao_imprimir.grid(column=1, row=0)

        self.spin_numeros = ttk.Spinbox(self.frame_imprimir_nota, from_= 1, to= 10, wrap=True, textvariable=self.imprimir_copias, width=5)
        self.spin_numeros.grid(column=2, row=0)

        self.label_copias = ttk.Label(self.frame_imprimir_nota, text="CÓPIA(S)")
        self.label_copias.grid(column=3, row=0)

        self.label_assunto = ttk.Label(self.frame_info_3, text="Assunto: ", wraplength= 400)
        self.label_assunto.grid(column=0, row=2, columnspan=3, sticky="nsew", pady=4)

        self.lista_campos_texto = [self.label_nome_custom.cget('text'), self.label_fant.cget('text'), self.label_soc.cget('text'), self.label_numero_nota.cget('text'), self.label_valor_total.cget('text'), self.label_cfop.cget('text'), self.label_emi.cget('text'), self.label_remetente.cget('text'), self.label_assunto.cget('text'), self.label_data_email.cget('text'), self.label_impresso.cget('text'), self.label_adicionado.cget('text')]

    def criar_frame_info_notas(self):
        self.frame_info_tabela = ttk.Frame(self.frame_mostrar)
        self.frame_info_tabela.grid(column=0, row=1)
        self.frame_info_tabela.grid_columnconfigure(0, weight=1)

        self.colunas_itens = ("idItem", "cProd", "xProd", "uCom", "qCom", "vUnCom", "vProd")
        self.largs_itens = (45, 85, 290, 30, 50, 70, 70)
        self.nomes_itens = ("", "Código", "Produto", "UN", "QNT", "V UN", "V TOT")
        self.tabela_info = ttk.Treeview(self.frame_info_tabela, columns=self.colunas_itens, show="headings", height=14)
        for num, a in enumerate(self.colunas_itens):
            self.tabela_info.heading(self.colunas_itens[num], text= self.nomes_itens[num])
            self.tabela_info.column(a, width=self.largs_itens[num])

        self.tabela_info.grid(column=0, row=0, sticky="s", pady=4)

        self.scrollbar_treeview_itens = ttk.Scrollbar(self.frame_info_tabela, orient="vertical", command=self.tabela_info.yview)
        self.scrollbar_treeview_itens.grid(column=1, row=0, sticky="nsew")

        self.tabela_info.configure(yscrollcommand=self.scrollbar_treeview_itens.set)

        self.label_qnt_itens = ttk.Label(self.frame_info_tabela, text="")
        self.label_qnt_itens.grid(column=0, row=1, sticky="nsew")

    def mostrar_notas_tabela_esquerda(self, modo, filtro = False):
        self.conta_paginas = 0
        self.lista_paginas = [[]]
        
        inferno = lambda x, s: x if x is not None else s

        if filtro:
            self.tabela_selec.delete(*self.tabela_selec.get_children())
            emp = self.var_emp.get()
            mes = self.var_mes.get()
            ano = self.var_ano.get()
            numero_nota = self.var_numero.get()
            self.lista_tuplas_filtro = self.filtra_emp_mes_ano(self.todas, emp, mes, ano, numero_nota)
            self.lista_tuplas_sort = self.lista_tuplas_filtro
            self.paginar(self.lista_tuplas_filtro)
            self.sort_heading("dataEmissao", "Emissão", True)

        elif modo == "todas" and not filtro:
            try:
                self.todas = buscarTodas(self.conn, "notas")
            except mysql.connector.errors.OperationalError:
                self.reconectar_bd()
                self.todas = buscarTodas(self.conn, "notas")

            self.lista_tuplas = [(num+1, a['idNota'], inferno(a["customNome"], a["nomeFantasia"]), int(a['numeroNota']), datetime.strftime(a['dataEmissao'], "%d/%m/%Y %H:%M:%S"), a["impresso"]) for num, a in enumerate(self.todas)]
            self.lista_tuplas_sort = self.lista_tuplas
            self.paginar(self.lista_tuplas)
            self.sort_heading("dataEmissao", "Emissão")

    def troca_pagina_info_nota(self, tipo):
        self.tabela_selec.delete(*self.tabela_selec.get_children())

        if tipo == "mais":
            if self.conta_paginas < len(self.lista_paginas)-1 and len(self.lista_paginas)>0:
                self.conta_paginas += 1

        elif tipo == "menos":
            if self.conta_paginas > 0:
                self.conta_paginas -= 1

        for a, b in enumerate(self.lista_paginas[self.conta_paginas]):
            self.tabela_selec.insert(parent='', index=a, values=b)
        
        len_total_paginas = 0
        for a in self.lista_paginas: len_total_paginas += len(a)
        self.label_txt_page.config(text=self.texto_paginas(self.conta_paginas+1, len_total_paginas))

    def paginar(self, lista: list[tuple], sort: bool = False):
        self.lista_paginas = [[]]
        self.lista_paginas_2 = [[]]
        self.conta_paginas_paginar = 0
        self.conta_paginas = 0

        for a in range(0, len(lista)):

            if a > 1:
                if a % 25 == 0:
                    self.conta_paginas_paginar += 1
                    self.lista_paginas.append([])
            if sort:
                    self.lista_paginas[self.conta_paginas_paginar].append(tuple([a+1]) + lista[a][1:])
            else:
                self.lista_paginas[self.conta_paginas_paginar].append(lista[a])

    def texto_paginas(self, num, len_lista, usar_dois = False):
        numFinalLen = len(self.lista_paginas_2) if usar_dois else len(self.lista_paginas)
        return f"{(25*num) - 24} - {25*num if len_lista>num*25 else len_lista} DE {len_lista} (PAGINA {num} de {numFinalLen})"
    
    def buscar_infos_unica_nota(self, a):
        reg = self.tabela_selec.identify("region", a.x, a.y)
        if reg == "heading":
            return
        item = self.tabela_selec.item(self.tabela_selec.focus())['values']
        id_item = item[1]
        self.nota_selecionada = item

        lista_preencher_campos = [self.label_nome_custom, self.label_fant, self.label_soc, self.label_numero_nota, self.label_valor_total, self.label_cfop, self.label_emi, self.label_remetente, self.label_assunto, self.label_data_email, self.label_impresso, self.label_adicionado]

        try:
            unico = buscarTodas(self.conn, "unica_por_id", id_nota = id_item)
        except mysql.connector.errors.OperationalError:
            self.reconectar_bd()
            unico = buscarTodas(self.conn, "unica_por_id", id_nota = id_item)

        for num, a in enumerate(lista_preencher_campos):
            a.config(text=f"{self.lista_campos_texto[num]} {unico[num]}")
        
        self.buscar_itens_nota(id_item)

    def buscar_itens_nota(self, id_item):
        self.tabela_info.delete(*self.tabela_info.get_children())

        sql = f'''SELECT
                    cProd,
                    xProd,
                    uCom,
                    qCom,
                    vUnCom,
                    vProd
                        FROM produtos
                            INNER JOIN operacoes AS op ON  op.idOP = produtos.CFOP
                                WHERE idNota = {id_item}'''
        
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except:
            self.reconectar_bd()
            res = self.cursor.fetchall()

        if res is not None:
            lt = [tuple(map(self.f, list([num+1] + list(a)))) for num, a in enumerate(res)]
            c = 0
            for num, a in enumerate(lt):
                self.tabela_info.insert(parent='', index=num, values=a)
                c += 1
            
            print("CONTAGEM IF MAIS DE 15 ITENS", c)

            if c > 15:
                texto_label_qnt_itens = f"{c} itens no total."
                self.label_qnt_itens.config(text= texto_label_qnt_itens)
            else:
                self.label_qnt_itens.config(text= "")
            
            

    def filtra_emp_mes_ano(self, lista, emp: str, mes: str, ano: str, numero: str):
        print(emp, mes, ano, numero)
        inicio_1 = time.perf_counter()
        self.conta_paginas=0

        inferno = lambda x, s: x if x is not None else s

        tem_emp = emp != "Empresa"
        tem_mes = mes.isdigit()
        tem_ano = ano.isdigit()
        tem_num = numero.isdigit()
        if tem_ano: ano = int(ano)
        if tem_mes: mes = int(mes)
        print(tem_emp, tem_mes, tem_ano)

        nada = not tem_ano and not tem_mes and not tem_emp and not tem_num

        if nada:
            filtro = buscarTodas(self.conn, "notas")
        else:
            if tem_mes and tem_ano:
                filtro = list(filter(lambda a: a["dataEmissao"].month == mes and a["dataEmissao"].year == ano, self.todas))
            elif tem_ano and not tem_mes:
                filtro = list(filter(lambda a: a["dataEmissao"].year == ano, self.todas))
            elif tem_mes and not tem_ano:
                filtro = list(filter(lambda a: a["dataEmissao"].month == mes, self.todas))
            else:
                filtro = self.todas

            if tem_emp: filtro = list(filter(lambda a: self.inferno_merda_bosta(a, emp), filtro))

            if tem_num: filtro = list(filter(lambda a: numero == a["numeroNota"], filtro))

        l = [(num+1, a['idNota'], inferno(a["customNome"], a["nomeFantasia"]), int(a['numeroNota']), datetime.strftime(a['dataEmissao'], "%d/%m/%Y %H:%M:%S"), a["impresso"]) for num, a in enumerate(filtro)]

        fim_1 = time.perf_counter()
        print(f"PERFORMANCE {fim_1 - inicio_1}")
        return l
    
    def inferno_merda_bosta(self, dic, string):
        customNome = dic["customNome"]
        nomeFantasia = dic["nomeFantasia"]
        tem_custom_nome = dic["customNome"] is not None
        tem_nome_fantasia = dic["nomeFantasia"] is not None
        
        if tem_nome_fantasia and not tem_custom_nome:
            return string.lower() in nomeFantasia.lower()
        elif tem_custom_nome and tem_nome_fantasia:
            return string.lower() in customNome.lower() or string.lower() in nomeFantasia.lower()
        elif tem_custom_nome and not tem_nome_fantasia:
            return string.lower() in customNome.lower()
        
    def reconectar_bd(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def imprimir_nota_selecionada(self):
        num_copias = self.imprimir_copias.get()
        nota = self.nota_selecionada

        print(f"A NOTA {nota[2]} {nota[3]} SERÁ IMPRESSA {num_copias} VEZES")
        existe = f"{nota[2]} {nota[3]}.pdf" in os.listdir("./notas/pdf/imprimir")
        print("A NOTA EXISTE NA PASTA HAHAHAHAHAHA") if existe else print(":(")