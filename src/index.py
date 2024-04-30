from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela
import queue
from datetime import datetime

contatos_lista = []
filaMensagem = queue.Queue()
contFila = 0

# FUNÇÕES
def AdicionarContato():
    # ESCREVER LÓGICA AQUI!
    nomeContatoNovo = str(input("Adcionar Nome do Contato: "))
    numeroContatoNovo = str(input ("Adcionar numero do contato: "))
    # Exemplo de criação de um contato
    novo_contato = Contato(nomeContatoNovo, numeroContatoNovo)

    for contato in contatos_lista:
        if contato.nome == nomeContatoNovo and contato.numero == numeroContatoNovo:
            print("Esse contato já existe, tente novamente!")
            input("[APERTE ENTER PARA CONTINUAR]")
            return
                      
    contatos_lista.append(novo_contato)
    print("Usuário Criado com Sucesso!")

    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def MostrarContatos():
    # ESCREVER LÓGICA AQUI
    print("Mostrando lista de contatos")
    for mostrar_contato in contatos_lista:
        print("Nome: ",mostrar_contato.nome,"  Telefone: ", mostrar_contato.numero)
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EditarContato():
    # ESCREVER LÓGICA AQUI

    for mostrar_contato in contatos_lista:
        print("Nome: ",mostrar_contato.nome,"  Telefone: ", mostrar_contato.numero)

    contatoParaEditar = input("Digite o nome do contato que voce quer editar: ")

    for mostrar_contato in contatos_lista:    
        if contatoParaEditar == mostrar_contato.nome :
            print("Voce selecionou ", mostrar_contato.nome)
            qualEditar = int(input("O que deseja editar, Nome(1) ou Telefone(2) ?"))
            if qualEditar == 1 :
                novoNome = input("Digite o novo nome: ")
                mostrar_contato.nome = novoNome
                print("Contato editado com sucesso!")
            elif qualEditar == 2 : 
                novoNumero = int(input("Digitar o novo numero: "))
                mostrar_contato.numero = novoNumero
                print("Contato editado com sucesso!")
            else : 
                print("Esse numero não foi reconhecido. Tente novamente")
                  
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def SelecionarContato():
    print("Selecione um contato:")
    for contato in contatos_lista:
        print(contato.nome)

    while True:
        nome_contato = input("Digite o nome do contato: ")
        for contato in contatos_lista:
            if contato.nome == nome_contato:
                return contato.nome  

        print("Contato não encontrado na lista. Digite um contato válido.")

def EscreverMensagem():
    # Exemplo de criação de uma mensagem
    contato = SelecionarContato()
    msgDaFila = input(f"Digite a mensagem para {contato}: ")

    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mensagem_com_dados = {
        "mensagem": msgDaFila, 
        "contato": contato, 
        "data_hora_envio": data_hora_atual 
        }
    
    if isinstance(mensagem_com_dados, dict):
        filaMensagem.put(mensagem_com_dados)

    print(f"{data_hora_atual} - Mensagem para {contato}: {msgDaFila}")

    #filaMensagem.put(msgDaFila)
    
    global contFila
    contFila = contFila + 1 

    print("Quantidade de mensagens na fila = ", contFila)
    print("Mensagem Criada com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")

           
    limparTela()
    

   # destinatario = Contato("Contato para envio", "Numero para envio")
   # mensagem = Mensagem(destinatario, "Mensagem", "01/01/2024")
    
def MandarMensagem():
    # Mandar msg para fila e mostrar a primeira mensagem pra mandar
    if not filaMensagem.empty() :
        print("Mandando a primeira msg da fila")
        msgDaFila = filaMensagem.get()

        if isinstance(msgDaFila, dict):
            print(f"Enviando mensagem: {msgDaFila['mensagem']} para {msgDaFila['contato']} as {msgDaFila['data_hora_envio']}")

        ## filaMensagem.qsize()
        global contFila
        contFila = contFila - 1 
        print("Numero de mensagens na fila = ", contFila)

        for item in list(filaMensagem.queue):
            print(f"Mensagem ainda na fila: {item['mensagem']} para {item['contato']}")
        
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()
    else:
        print("A fila de mensagens está vazia.")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()
    

# PROGRAMA PRINCIPAL
print("===== SISTEMA DE MENSAGENS =====\n")

fimPrograma = False

while not fimPrograma:
    imprimirMenuPrincipal()
    opcao = input("Escolha uma das opções: ")

    if int(opcao) == 1:
        AdicionarContato()
    elif int(opcao) == 2:
        MostrarContatos()
    elif int(opcao) == 3:
        EditarContato()
    elif int(opcao) == 4:
        EscreverMensagem()
    elif int(opcao) == 5:
        MandarMensagem()
    elif int(opcao) == 0:
        fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")