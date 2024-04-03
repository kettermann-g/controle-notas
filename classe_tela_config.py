import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from functools import partial
import mysql.connector
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from configparser import ConfigParser
import os
from funcoes import bosta


class GridConfiguracoes(ttk.Frame):
    def __init__(self, container, conn: mysql.connector.connection.MySQLConnection):
        super().__init__(container)
        self.conn = conn

        self.todos = self.buscar_todos_nomes()

        self.lista_paginas = []

        self.conta_paginas = 0

        self.var_nome = tk.StringVar()

        self.nome_selecionado = "VAZIO"

        self.criar_frame_custom_nome()
        self.criar_frame_atualizar()
        self.paginar()
        self.joga_paginas()

    def criar_frame_custom_nome(self):
        self.grid_tabela_nomes = ttk.Frame(self)
        self.grid_tabela_nomes.grid(column=0, row=0)
        colunas = ("numero", "id", "nomeCustom", "nomeFantasia", "razaoSocial")
        nomes = ("#", "ID", "Nome pers.", "Nome Fantasia", "Razão Social")
        larg = (35, 35, 200, 300, 350)
        self.tabela_nomes = ttk.Treeview(self.grid_tabela_nomes, columns=colunas, show= "headings", height=19)
        for col, nome, lg in zip(colunas, nomes, larg):
            self.tabela_nomes.heading(col, text= nome)

            self.tabela_nomes.column(col, width=lg)
        
        self.tabela_nomes.grid(column=0, row=0)

        self.tabela_nomes.bind("<ButtonRelease-1>", self.selec_nome)

        self.scrollbar_treeview_itens = ttk.Scrollbar(self.grid_tabela_nomes, orient="vertical", command=self.tabela_nomes.yview)
        self.scrollbar_treeview_itens.grid(column=1, row=0, sticky="nsew")

        self.tabela_nomes.configure(yscrollcommand=self.scrollbar_treeview_itens.set)

    def criar_frame_atualizar(self):
        self.grid_botoes = ttk.Frame(self)
        self.grid_botoes.grid(column=1, row=0)

        self.label_nome_custom = ttk.Label(self.grid_botoes, text="Novo nome: ")
        self.label_nome_custom.grid(column=0, row=0, sticky="nsew")

        self.entry_custom_nome = ttk.Entry(self.grid_botoes, textvariable=self.var_nome)
        self.entry_custom_nome.grid(column=1, row=0, sticky="nsew")

        self.botao_atualizar_lista = ttk.Button(self.grid_botoes, text="ATUALIZAR LISTA", command=self.atualizar_lista)
        self.botao_atualizar_lista.grid(column=0, row=1, sticky="nsew")

        self.botao_confirmar = ttk.Button(self.grid_botoes, text="CONFIRMAR", command=partial(self.confirmar_alteracao))
        self.botao_confirmar.grid(column=1, row=1, sticky="nsew")

    def buscar_todos_nomes(self):
        null = lambda x: x if x is not None else ""

        cursor = self.conn.cursor()
        cursor.execute("SELECT idEmpresa, customNome, nomeFantasia, razaoSocial FROM empresas")
        lista = [tuple(map(null, list(a))) for a in cursor.fetchall()]
        return lista
    
    def paginar(self):
        self.lista_paginas = []
        lista = []
        for num, a in enumerate(self.todos):
            tup = [num+1] + list(a)
            lista.append(tuple(tup))
        self.lista_paginas.append(lista)
    
    def joga_paginas(self):
        self.tabela_nomes.delete(*self.tabela_nomes.get_children())
        for a in self.lista_paginas[self.conta_paginas]:
            self.tabela_nomes.insert(parent='', index=a[0], values=a)

    def selec_nome(self, a):
        reg = self.tabela_nomes.identify("region", a.x, a.y)
        if reg == "heading":
            return
        item = self.tabela_nomes.item(self.tabela_nomes.focus())['values']
        self.nome_selecionado = item
        print(item)
        print(item[1])

    def confirmar_alteracao(self):
        nome = self.var_nome.get()
        id = self.nome_selecionado[1]

        if nome != "":
            nome = f"'{nome}'"
        else:
            nome = "NULL"
        
        sql = f'''UPDATE empresas SET customNome = {nome} WHERE idEmpresa = {id}'''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        self.renomear_arquivos()

        self.atualizar_lista()

    def atualizar_lista(self):
        self.todos = self.buscar_todos_nomes()
        self.paginar()
        self.joga_paginas()

    def renomear_arquivos(self):
        xNome = self.nome_selecionado[4]
        lista_pasta_pdf = os.listdir("./notas/pdf/imprimir")
        lista_pasta_xml = os.listdir("./notas/xml")
        
        novo_nome = self.var_nome.get()

        for num, filename_xml in enumerate(lista_pasta_xml):
            arquivo = open(f"./notas/xml/{filename_xml}", "r")
            dados = arquivo.read()
            soup = BeautifulSoup(bosta(dados), features="xml")
            arquivo.close()
            razao_social = soup.find("xNome").text

            if razao_social == xNome:

                nome_antigo = filename_xml.split(".", 1)[0]
                numero_nota_filename = nome_antigo.rsplit(" ", 1)[-1]

                filename_pdf = lista_pasta_pdf[num]

                novo_filename_xml = f"{novo_nome} {numero_nota_filename}.xml"
                novo_filename_pdf = f"{novo_nome} {numero_nota_filename}.pdf"

                print()

                os.rename(f"./notas/xml/{filename_xml}", f"./notas/xml/{novo_filename_xml}")
                os.rename(f"./notas/pdf/imprimir/{filename_pdf}", f"./notas/pdf/imprimir/{novo_filename_pdf}")