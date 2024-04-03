import tkinter as tk
from tkinter import ttk
from functools import partial
import mysql.connector
from funcoes import conectar

class GridAddPagamento(ttk.Frame):
    def __init__(self, container, conn: mysql.connector.connection.MySQLConnection):
        super().__init__(container)

        self.conn = conn


        self.var_desc = tk.StringVar()
        self.var_num = tk.StringVar()
        self.var_valor = tk.StringVar()
        self.var_venc = tk.StringVar()
        self.var_pago = tk.StringVar()

        self.criar_frame_esquerda()
        self.criar_frame_direita()
        
    def criar_frame_esquerda(self):
        self.frame_esquerda = tk.Frame(self, highlightcolor="blue", highlightthickness= 1)
        self.frame_esquerda.grid(column=0, row=0, sticky= "e", padx= 60)
        self.frame_esquerda.grid_columnconfigure(0, weight=1)
        self.frame_esquerda.grid_columnconfigure(1, weight=1)

        self.label_descricao = ttk.Label(self.frame_esquerda, text="Descrição: ")
        self.label_descricao.grid(column=0, row=0, sticky="nsew", pady= 25)

        self.entry_descricao = ttk.Entry(self.frame_esquerda, textvariable=self.var_desc)
        self.entry_descricao.grid(column=1, row=0, sticky="nsew", pady= 25)

        self.label_numero = ttk.Label(self.frame_esquerda, text="Número: ")
        self.label_numero.grid(column=0, row=1, sticky="nsew", pady= 25)

        self.entry_numero = ttk.Entry(self.frame_esquerda, textvariable= self.var_num)
        self.entry_numero.grid(column=1, row=1, sticky="nsew", pady= 25)

        self.label_valor = ttk.Label(self.frame_esquerda, text="Valor: ")
        self.label_valor.grid(column=0, row=2, sticky="nsew", pady= 25)

        self.entry_valor = ttk.Entry(self.frame_esquerda, textvariable= self.var_valor)
        self.entry_valor.grid(column=1, row=2, sticky="nsew", pady= 25)

    def criar_frame_direita(self): 
        self.frame_direita = tk.Frame(self, highlightcolor="red", highlightthickness= 1)
        self.frame_direita.grid(column=1, row=0, sticky="w", padx= 60)
        self.frame_direita.grid_columnconfigure(0, weight=1)
        self.frame_direita.grid_columnconfigure(1, weight=1)


        self.label_vencimento = ttk.Label(self.frame_direita, text="Vencimento: ")
        self.label_vencimento.grid(column=0, row=0, sticky="nsew", pady=25)

        self.entry_vencimento = ttk.Entry(self.frame_direita, textvariable= self.var_venc)
        self.entry_vencimento.grid(column=1, row=0, sticky="nsew", pady=25)

        self.label_pago = ttk.Label(self.frame_direita, text="Pago: ")
        self.label_pago.grid(column=0, row=1, sticky="nsew", pady=25)

        self.entry_pago = ttk.Entry(self.frame_direita, textvariable= self.var_pago)
        self.entry_pago.grid(column=1, row=1, sticky="nsew", pady=25)

        self.botao_confirmar = ttk.Button(self.frame_direita, text="ANOTAR", command= self.anotar_bd)
        self.botao_confirmar.grid(column=0, row=2, columnspan=2, pady=25)
    
    def anotar_bd(self):
        desc = self.var_desc.get()
        num = self.var_num.get()
        valor = self.var_valor.get()
        venc = self.var_venc.get()
        pago = self.var_pago.get()