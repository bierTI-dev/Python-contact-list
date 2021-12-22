def inicio():
    """
    Função que dará o cabeçário do programa, foram definidas cores as linhas, cor das letras e cor de fundo porém
    só funcionarão em terminal linux ou executando direto no PyCharm.

    """
#Acima está a explicação da função, foi colocada somente para fins visuais

    print('\033[42;1;30m' + '|', '__'*20,'|'+'\033[0;0m')
    print('\033[42;1;30m' + '|', '__'*20,'|'+'\033[0;0m')
    print('\033[42;1;55m     LÓGICA DE PROGRAMAÇÃO E ALGORITMOS     \033[0;0m')
    print('\033[42;1;55m           PYTHON CONTACT LIST              \033[0;0m')
    print('\033[42;1;30m' + '|', '__'*20,'|'+'\033[0;0m')
    print('\033[42;1;30m' + '|', '__'*20,'|'+'\033[0;0m')

inicio()

#Programa Principal

print('Lista telefonica')
print('Para encerrar a inserção deixe em branco e pressione enter no campo em que pedirá o Nome')

#Abaixo listas e dicionários em branco para serem preenchidos posteiormente
lista = []
info = {}
lista18 = []
lista17 = []
x = 0
cont18 = 0
cont17 = 0
while True:
    info['nome'] = str(input('Digite o nome do contato: ')) #Lê "nome" dentro do dicionário "info"
    if (info['nome'] == '') or (info['nome'] == ' '): #Se o usuário só apertar enter ou der espaço e enter encerra o programa
        print('\nEncerrando a inserção de dados')
        break
    info['numero'] = int(input(f'Digite o número de telefone de {info["nome"]}: ')) #Lê "numero" dentro do dicionário "info"
    info['idade'] = int(input(f'Digite a idade de {info["nome"]}: ')) #Lê "idade" dentro do dicionário "info"
    lista.append(info.copy()) #Copia o dicionario "info" para a lista "lista"
    continue #Reinicia as perguntas até o usuário utilizar a instrução para encerrar o programa, mas salvando os dados

lista_sorted = sorted(lista, key=lambda k: k['nome']) #Ordena a lista em ordem alfabética

print('\n\033[1;31mLISTA DE CONTATOS EM ORDEM ALFABÉTICA\033[0;0m')
print('--' * 19)
for pessoas in lista_sorted: #loop para apresentar nome, numero e idade digitados
    print(f'\033[;1mNOME:\033[0;0m {pessoas["nome"]} \n\033[;1mNUMERO:\033[0;0m {pessoas["numero"]} \n\033[;1mIDADE:\033[0;0m {pessoas["idade"]}')
    print('---' * 13)

for pessoasy in lista_sorted: #nova variavel para não dar problema com o comando sorted
    if pessoasy['idade'] >= 18: #lê idade maior ou igual a 18
        lista18.append(pessoasy.copy())
        cont18 += 1
    if pessoasy['idade'] < 18: #Idade menor que 18
        lista17.append(pessoasy.copy())
        cont17 += 1

if cont18 > 0:
    print('\n\033[1;31mPessoas com mais de 18 anos:\033[0;0m')
    for pessoasx in lista18:#nova variavel para nao dar problema com o comando sorted
        #apresenta as pessoas com idade maior ou igual 18 anos
        print(f'\033[;1mNOME: \033[0;0m{pessoasx["nome"]}\n\033[;1mNÚMERO: \033[0;0m{pessoasx["numero"]}\n\033[;1mIDADE: \033[0;0m{pessoasx["idade"]}')
        print('---' * 13)

if cont17 > 0:
    print('\n\033[1;31mPessoas com menos de 18 anos:\033[0;0m')
    for pessoasx in lista17: # nova variavel para nao dar problema com o comando sorted
        # apresenta as pessoas com idade menor que 18 anos
        print(f'\033[;1mNOME: \033[0;0m{pessoasx["nome"]}\n\033[;1mNÚMERO: \033[0;0m{pessoasx["numero"]}\n\033[;1mIDADE:\033[0;0m {pessoasx["idade"]}')
        print('---' * 13)