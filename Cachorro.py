from random import randint


class Cachorro:
    def __init__(self, nome, raca, sexo, idade):
        self.nome = nome
        self.raca = raca
        sexos = ['M', 'm', 'F', 'f']
        if sexo in sexos:
            self.sexo = sexo
        else:
            print('Sexo inválido.')
            self.sexo = 'N'
        self.idade = idade
        self.energia = 100
        self.numero_filhotes = 0

    def obter_dados(self):
        return (f'Nome: {self.nome}\n'
                f'Raça: {self.raca}\n'
                f'Sexo: {self.sexo}\n'
                f'Idade: {self.idade}\n'
                f'Energia: {self.energia}\n'
                f'Número de filhotes: {self.numero_filhotes}')

    def comer(self):
        if self.energia <= 50:
            print('R) Ração\n'
                  'C) Carne\n'
                  'L) Legumes')
            while True:
                comida = str(input('Escolha uma opção: ')).upper().strip()[0]
                if comida in 'RCL':
                    break
                else:
                    print('Opção inválida!', end=' ')
            if comida == 'R':
                self.energia += 50
            elif comida == 'C':
                self.energia += 40
            elif comida == 'L':
                self.energia += 30
            print(f'O cachorro foi alimentado!', end=' ')
        else:
            print('O cachorro não precisa comer.', end=' ')
        print(f'Energia atual: {self.energia}')

    def brincar(self, brincadeira):
        if self.energia >= 40:
            if brincadeira == 'B':
                self.energia -= 30
            elif brincadeira == 'S':
                self.energia -= 20
            elif brincadeira == 'G':
                self.energia -= 10
            print(f'O cachorro brincou de {brincadeira}.', end=' ')
        else:
            print('O cachorro não pode brincar agora.', end=' ')
        print(f'Energia atual: {self.energia}')

    def pode_cruzar(self, parc):
        if (1 <= self.idade <= 9 and 1 <= parc.idade <= 9 and self.raca == parc.raca and
                self.energia >= 80 and parc.energia >= 80 and self.sexo != parc.sexo):
            return True
        else:
            return False

    def cruzar(self, parc):
        if self.pode_cruzar(parc):
            self.energia -= 50
            parc.energia -= 50
            filhotes_gerados = randint(3, 10)
            self.numero_filhotes += filhotes_gerados
            parc.numero_filhotes += filhotes_gerados
            print(f'Cruzamento realizado. Filhotes gerados: {filhotes_gerados}')
        else:
            print('Não foi possivel realizar o cruzamento.')
