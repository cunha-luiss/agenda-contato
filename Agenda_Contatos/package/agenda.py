class Agenda():
    def __init__(self):
        self.contato = {}
        self.loop()

    def loop(self):
        while True:
            # Interface da aplicação
            print("\nAgenda de contatos:")
            print("1. Adicionar contatos")
            print("2. Lista de contatos")
            print("3. Procurar contato")
            print("4. Editar contato")
            print("5. Deletar contato")
            print("6. Encerrar app")


            choice = int(input("Insira sua escolha: "))
            if choice == 1:
                # chama a classe contatos para adicionar os "valores" dentro de listas
                self.adicionarContato("Digite o nome: ", "Digite o telefone: ")

            if choice == 2:
                # formação de uma lista de contatos
                self.listaContato()

            if choice == 3:
                self.procurarContato()

            if choice == 4:
                self.alterarContato()

            if choice == 5:
                self.removerContato()

            if choice == 6:
                # finalização da aplicação
                break


    def adicionarContato(self,nome,telefone):
        # nome e telefone são as mensagens que serão mostradas ao usuário
        nome = input(nome).strip()
        telefone = input(telefone).strip()

        # verificando se já existe o contato (pelo número e pelo nome)
        for nomess, telefoness in self.contato.items():
            if nome == nomess or telefone == telefoness:
                print("\nUsuário já adicionado, tente novamente")
                return
            
        self.contato[nome] = telefone
    
    def listaContato(self):
        print("\nLista de Contatos")
        x = 1
        for nome, telefone in sorted(self.contato.items()):
            print(f'{x}. {nome.title()}, {telefone}')
            x = x+1

    def procurarContato(self):
        searchC = input("\nQual contato deseja procurar? ")
        for nome, telefone in self.contato.items():
            if nome == searchC:
                print("\nContato encontrado!")
                print(f'{nome.title()}, {telefone}')

    def alterarContato(self):
        changeN = input("Qual o nome do contato que deseja alterar? ")
        telefoneN = input("Qual o número novo? ")
        self.contato[changeN] = telefoneN
        print(f'\nContato {changeN} alterado com sucesso!')
    
    def removerContato(self):
        removeC = input("Qual o nome do contato que deseja remover? ")
        del self.contato[removeC]
        print(f'\nContato {removeC} removido com sucesso!')
