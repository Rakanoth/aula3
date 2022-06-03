from tkinter import *

class Tela:

    #Criando a janela
    janela_principal = Tk()
        
    #Mudando o título da janela
    janela_principal.wm_title("Cadastro de Clientes")

    #Criando variaveis dinamicas para armazenar os dados digitados pelo usuário
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    #Criando os labels para sinalizar do que se trata cada caixa de texto
    labelNome = Label(janela_principal, text="Nome")
    labelSobrenome = Label(janela_principal, text="Sobrenome")
    labelEmail = Label(janela_principal, text="Email")
    labelCPF = Label(janela_principal, text="CPF")

    #Criando as caixas de texto para cada dado que será digitado pelo usuário
    entNome = Entry(janela_principal, textvariable=txtNome)
    entSobrenome = Entry(janela_principal, textvariable=txtSobrenome)
    entEmail = Entry(janela_principal, textvariable=txtEmail)
    entCPF = Entry(janela_principal, textvariable=txtCPF)

    #Criando componente para listar os clientes
    listClientes = Listbox(janela_principal)

    #Criando area de texto para funcionar junto com o listbox
    scrollClientes = Scrollbar(janela_principal)

    #Criando os botões do sistema
    verTodos = Button(janela_principal, text="Ver todos")
    buscar = Button(janela_principal, text="Buscar")
    inserir = Button(janela_principal, text="Inserir")
    atualizar = Button(janela_principal, text="Atualizar Selecionados")
    deletar = Button(janela_principal, text="Deletar Selecionados")
    fechar = Button(janela_principal, text="Fechar")

    #Adicionar os componentes(widgets) a janela
    labelNome.grid(row = 0, column = 0)
    labelSobrenome.grid(row = 1, column = 0)
    labelEmail.grid(row = 2, column = 0)
    labelCPF.grid(row = 3, column = 0)

    entNome.grid(row = 0, column = 1)
    entSobrenome.grid(row = 1, column = 1)
    entEmail.grid(row = 2, column = 1)
    entCPF.grid(row = 3, column = 1)

    listClientes.grid(row = 0, column = 2, rowspan=10)

    scrollClientes.grid(row = 0, column = 6, rowspan=10)

    verTodos.grid(row =4, column = 0, columnspan=2)
    buscar.grid(row = 5, column = 0, columnspan=2)
    inserir.grid(row = 6, column = 0, columnspan=2)
    atualizar.grid(row = 7, column = 0, columnspan=2)
    deletar.grid(row = 8, column = 0, columnspan=2)
    fechar.grid(row = 9, column = 0, columnspan=2)

    #Associando a scrollbar com o listbox
    listClientes.configure(yscrollcommand = scrollClientes.set)
    scrollClientes.configure(command = listClientes.yview)

    #Criando variaveis parada definir o padding e a largura dos componentes
    x_pad = 5
    y_pad = 3
    width_entry = 30

    #Adicionando um pouco de beleza na interface
    for child in janela_principal.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky = "ew", padx = x_pad, pady = y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx = 0, pady = 0, sticky = "ns")
        elif widget_class == "Scrollbar":
            child.grid_configure(padx = 0, pady = 0, sticky = "ns")
        else:
            child.grid_configure(padx = x_pad, pady = y_pad, sticky = "n")
        
    def executar(self):
        Tela.janela_principal.mainloop()
