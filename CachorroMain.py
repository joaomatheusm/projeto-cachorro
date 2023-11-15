from Cachorro import Cachorro
from sys import exit


def manipular_cachorro(cao_atual, lista_caes):
    try:
        while True:
            print('-' * 30)
            print('1) Ver dados do cão\n'
                  '2) Alimentar\n'
                  '3) Brincar\n'
                  '4) Cruzar\n'
                  '5) Menu inicial')
            opcao = int(input('Escolha uma opção: '))
            print('-' * 30)

            if opcao == 1:
                print(cao_atual.obter_dados())
            elif opcao == 2:
                cao_atual.comer('comida')
            elif opcao == 3:
                if cao_atual.energia >= 40:
                    print('B) Buscar bolinha\n'
                          'S) Saltar\n'
                          'G) Girar')
                    while True:
                        brincadeira = str(input('Escolha uma opção: ')).upper().strip()[0]
                        if brincadeira in 'BSG':
                            break
                        else:
                            print('Opção inválida!', end=' ')
                    cao_atual.brincar(brincadeira)
                else:
                    print('O cachorro não pode brincar agora.')
            elif opcao == 4:
                print(f'{" COD":<4}{"NOME":>20}')
                for c in lista_caes:
                    if cao_atual.pode_cruzar(c):
                        print(f'  {lista_caes.index(c):<4}{c.nome:>20}')
                while True:
                    parceiro = int(input('Escolha um parceiro para o cachorro cruzar: '))
                    if cao_atual.pode_cruzar(lista_caes[parceiro]):
                        break
                    else:
                        print('Opção indisponível.', end=' ')
                cao_atual.cruzar(lista_caes[parceiro])
            elif opcao == 5:
                return
            else:
                print('Opção inválida.')
    except ValueError:
        print('Opção inválida.')


def main():
    lista_caes = []
    while True:
        try:
            print('-' * 30)
            print('1) Cadastrar cão\n'
                  '2) Listar cães\n'
                  '3) Sair do programa')
            opcao = int(input('Escolha uma opção: '))
            print('-' * 30)

            if opcao == 1:
                nome = str(input('Nome: '))
                raca = str(input('Raça: '))
                while True:
                    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
                    if sexo in 'MF':
                        break
                    else:
                        print('Opção inválida.', end=' ')
                while True:
                    try:
                        idade = int(input('Idade: '))
                    except ValueError:
                        print('Opção inválida.', end=' ')
                    else:
                        break

                lista_caes.append(Cachorro(nome, raca, sexo, idade))
            elif opcao == 2:
                if len(lista_caes) >= 1:
                    print(f'{" COD":<4}{"NOME":>20}')
                    for i, c in enumerate(lista_caes):
                        print(f'  {i:<1}{c.nome:>20}')
                    cao_atual = int(input('Escolha um cão para manipular: '))
                    manipular_cachorro(lista_caes[cao_atual], lista_caes)
                else:
                    print('Nenhum cachorro foi cadastrado ainda.')
            elif opcao == 3:
                print('<< PROGRAMA ENCERRADO >>')
                exit(0)
            else:
                print('Opção inválida.')
        except ValueError:
            print('Opção inválida')


main()
