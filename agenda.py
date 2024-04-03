from classe_agenda import GridAgenda
from classe_info_notas import GridInfoNotas
from classe_buscar_anexos import GridBuscarAnexos
from classe_tela_config import GridConfiguracoes
from classe_agenda_2 import GridAgenda_2
from classe_add_pagamento import GridAddPagamento
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from functools import partial
from funcoes import conectar, logar_imap
import ctypes

class App(ThemedTk):
    def __init__(self):
        super().__init__()

        self.conn = conectar()

        self.set_theme("breeze")
        self.title("asdjfidsf")
        self.state('zoomed')

        self.pages = {}

        self.main_frame = ttk.Frame(self, width=1440, height=835)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_propagate(False)
        self.main_frame.grid(column=0, row=0)

        self.criar_frame_nav()


    def criar_frame_nav(self):
        self.frame_btn = ttk.Frame(self.main_frame, height=20)
        self.frame_btn.grid(column=0, row=0, pady= 15)

        self.botao_agenda = ttk.Button(self.frame_btn, text="AGENDA", command=partial(self.troca_pagina, 1))
        self.botao_agenda.grid(column=0, row=0, sticky="nsew")
        self.botao_info_notas = ttk.Button(self.frame_btn, text="INFO NOTAS", command=partial(self.troca_pagina, 2))
        self.botao_info_notas.grid(column=1, row=0, sticky="nsew")
        self.botao_pg3 = ttk.Button(self.frame_btn, text="EMAILS", command=partial(self.troca_pagina, 3))
        self.botao_pg3.grid(column=2, row=0, sticky="nsew")
        self.botao_add_pag = ttk.Button(self.frame_btn, text="ANOTAR", command=partial(self.troca_pagina, 4))
        self.botao_add_pag.grid(column=3, row=0, sticky="nsew")
        self.botao_config = ttk.Button(self.frame_btn, text="CONFIGURAÇÕES", command=partial(self.troca_pagina, 5))
        self.botao_config.grid(column=4, row=0, sticky="nsew")


    def troca_pagina(self, pagina):
        print(pagina)
        try:
            self.pages[pagina].tkraise()

            for a in self.pages:
                if a != pagina:
                    self.pages[a].lower()
        except:
            if pagina == 1:
                try:
                    self.grid_agenda_2 = GridAgenda_2(self.main_frame, self.conn)
                except:
                    self.reconectar_bd()
                    self.grid_agenda_2 = GridAgenda_2(self.main_frame, self.conn)
                self.grid_agenda_2.grid(column=0, row=1, sticky="nsew")
                for b in range(0, 3): self.grid_agenda_2.grid_columnconfigure(b, weight=1)

                self.pages[1] = self.grid_agenda_2

            if pagina == 2:
                try:
                    self.grid_info_notas = GridInfoNotas(self.main_frame, self.conn)
                except:
                    self.reconectar_bd()
                    self.grid_info_notas = GridInfoNotas(self.main_frame, self.conn)

                self.grid_info_notas.grid(column=0, row=1, sticky="nsew")
                self.grid_info_notas.grid_columnconfigure(0, weight=1)
                self.grid_info_notas.grid_columnconfigure(1, weight=1)
                self.grid_info_notas.grid_columnconfigure(2, weight=1)
                self.pages[2] = self.grid_info_notas

            if pagina == 3:
                try:
                    self.grid_buscar_anexos = GridBuscarAnexos(self.main_frame, self.conn)
                except:
                    self.reconectar_bd()
                    self.grid_buscar_anexos = GridBuscarAnexos(self.main_frame, self.conn)
                self.grid_buscar_anexos.grid(column=0, row=1, sticky="nsew")
                self.grid_buscar_anexos.grid_columnconfigure(0, weight=1)
                self.grid_buscar_anexos.grid_columnconfigure(1, weight=1)
                self.grid_buscar_anexos.grid_columnconfigure(2, weight=1)
                self.pages[3] = self.grid_buscar_anexos

            if pagina == 4:
                try:
                    self.grid_add_pag = GridAddPagamento(self.main_frame, self.conn)
                except:
                    self.reconectar_bd()
                    self.grid_add_pag = GridAddPagamento(self.main_frame, self.conn)
                self.grid_add_pag.grid(column=0, row= 1, sticky= "nsew")
                for b in range(0, 3): self.grid_add_pag.grid_columnconfigure(b, weight=1)



            if pagina == 5:
                try:
                    self.grid_configuracoes = GridConfiguracoes(self.main_frame, self.conn)
                except:
                    self.reconectar_bd()
                    self.grid_configuracoes = GridConfiguracoes(self.main_frame, self.conn)
                self.grid_configuracoes.grid(column=0, row=1, sticky="nsew")
                for b in range(0, 3): self.grid_configuracoes.grid_columnconfigure(b, weight=1)

                self.pages[4] = self.grid_configuracoes


    def reconectar_bd(self):
        self.conn = conectar()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()