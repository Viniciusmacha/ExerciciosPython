import ExerciciosControl
import this
this.contador = 0
this.num = 0
this.soma = 0
this.a = 0
this.maior = 0
this.num1 = 0
this.menor = 0
this.vet = 0
def exercicio01():
    A = 10
    B = 20
    msg = 'Antes da Troca:A = {}, B = {}'.format(A,B)
    aux = A
    A = B
    B = aux
    msg = msg + '\nDepois da troca: A = {}, B = {}'.format(A,B)
    return msg
def exercicio02():
    A = int(input('Informe um número: '))
    B = A-1
    print("O numero inserido foi: A {} O antecessor é:B {}".format(A,B))
def exercicio03():
    B = float(int(input('Informe o primeiro número: ')))
    A = float(int(input('Informe o segundo número: ')))
    C = A*B
    print("A área do retângulo é:{}".format(C))
def exercicio04():
    idade = (int(input('Informe a sua idade: ')))
    A = 365
    B = 30
    R = idade*A+B
    print("A sua idade em dias é: {}".format(R))
def exercicio05():
    Vt = (int(input('Informe a Quantidade de Votos: ')))
    VtB =(int(input('Informe a Quantidade de Votos Brancos: ')))
    VtN =(int(input('Informe a Quantidade de Votos Nulos: ')))
    VtV =(int(input('Informe a Quantidade de Votos Validos: ')))
    X = 100
    form1 =  (VtB / Vt) *X
    form2 =  (VtN / Vt) *X
    form3 =  (VtV / Vt) *X
    print("A porcentagem de Votos Brancos é:{} ".format(form1))
    print("A porcentagem de Votos Nulos é:{} ".format(form2))
    print("A porcentagem de Votos Validos é:{} ".format(form3))
def exercicio06():
    salario = float(input('Qual é o seu salário? '))
    perc = float(input('Qual a porcentagem que você quer adicionar? '))
    A = salario + (salario * perc / 100)
    print('Seu novo salario é de A = {}  '.format(A))
def exercicio07():
    fabrica = float(input('Qual valor do carro? '))
    novoValor = (fabrica + fabrica * 0.45 + fabrica * 0.28)
    print ('O novo valor do carro é de novoValor = {}'.format(novoValor))
def exercicio08():
    nota1 = float(input('Qual a primeira nota?' ))
    nota2 = float(input('Qual a segunda nota? '))
    nota3 = float(input('Qual a terceira nota? '))
    notaFinal = (nota1 + nota2 + nota3 / 10)
    print ('A nota total do aluno foi de notaFinal = {} '.format(notaFinal))
def exercicio09():
    maca = 1.30
    maca2 = 1.00
    question = int(input(('Qual a quantidade de maças você quer comprar? ')))
    if maca > 11:
        maca * 1
        print ('A Maçã custa maca= {}' .format(maca))
    else: maca2 < 12
    maca2 * 1
    print ('A Maçã custa maca2= {} ' .format(maca2))
def exercicio10():
    for numero in range(0,11):
        print('Os números na ordem crescentes são numero = {} '.format (numero))
def exercicio11():
    salario = float(input('Qual seu salario? '))
    vendas = int(input('Qual o total de vendas? '))
    comi = 0.3
    ultra = 0.5
    novoSalario = salario + (salario / vendas * 3 * 5 )
    print ('Seu novo Sálario é = {} ' .format(novoSalario))
def exercicio12():
    saldo = float(input('Qual é seu saldo? '))
    debito = float(input('Quantos reais você possui no débito? '))
    credito = float(input('Quantos reais no crédito você possui? '))
    saldoAtual = (saldo - debito + credito)
    print('Seu saldoAtual = {}' .format (saldoAtual))
    if saldoAtual >= 0:
        print('Saldo Positivo!')
    else:
        print('Saldo Negativo!')
def exercicio13():
    num = int(input('Qual numero você deseja? '))
    print(' {} * {} = {} '.format(num, 1, num * 1))
    print(' {} * {} = {} '.format(num, 2, num * 2))
    print(' {} * {} = {} '.format(num, 3, num * 3))
    print(' {} * {} = {} '.format(num, 4, num * 4))
    print(' {} * {} = {} '.format(num, 5, num * 5))
    print(' {} * {} = {} '.format(num, 6, num * 6))
    print(' {} * {} = {} '.format(num, 7, num * 7))
    print(' {} * {} = {} '.format(num, 8, num * 8))
    print(' {} * {} = {} '.format(num, 9, num * 9))
    print(' {} * {} = {} '.format(num, 10, num * 10))
def exercicio14():
    N = int(input('Informe um número: '))
    if N < 0:
        this.contador+N
     for i in range (N+1):
      print ('O números são N = {}' . format(N))
def exercicio15():
    for i in range(10):
        print('Informe um número: ')
        num = int(input())
        if num < 0:
            this.contador = this.contador + 1
    return this.contador
def exercicio15():
    for i in range(10):
        print('Informe um número: ')
        num = int(input())
        if num < 0:
            this.contador = this.contador + 1
            print('A quantidade de números negativos é = {}'.format(this.contador))

def exercicio16():
    for i in range(10):
        print('Informe os números: ')
        this.num = int(input())

        if this.num < 40:
            this.soma = this.soma + this.num
            print('A soma dos número foi de = {}'. format(this.soma))

def exercicio17():
    a = 14
    b = 100
    total = (a + b) / 2
    print('As médias do números é de = {}'. format(total))

def exercicio18():
    this.maior = vet [0]
    this.menor = vet [0]

    for i in range(10):
        if vet [0] > this.maior:
            this.maior = vet[0]

            if vet[0] < menor:
                menor < vet[0]
   print('O maior número digitado foi = {} '.format(this.maior))
def exercicio19():
print('')
dados = []
contar = 0
nome_final = 'NOME'
while True:
	dados.append([])
	nome = str(input('Digite o nome do aluno: ')).strip('').title()
	nota = float(input('Digite a primeira nota: '))
	nota_1 = float(input('Digite a segunda nota: '))
	media = (nota + nota_1) / 2
	dados[contar].append(nome)
	dados[contar].append(media)
	dados[contar].append(nota)
	dados[contar].append(nota_1)
	print('')
	verifica = str(input('Quer continuar (S/N)? ')).strip().upper()
	while verifica not in 'S' and verifica not in 'N':
		verifica = str(input('Digite uma opção válida: ')).strip().upper()
	if verifica == 'N':
		print('')
		break
	contar += 1
	print('')
print('ÍNDICE ', nome_final.ljust(12), '        MÉDIA')
print('-' * 34)
for índice in range(len(dados)):
	print('{} {} {:.1f}'.format(str(índice +1).ljust(7), dados[índice][0].ljust(20), dados[índice][1]))
while True:
	print('')
	verifica = str(input('Você quer ver a nota de tal aluno (S/N)? ')).strip().upper()
	while verifica not in 'S' and verifica not in 'N':
		verifica = str(input('Digite uma opção válida: ')).strip().upper()
	print('')
	if verifica == 'N':
		break
	else:
		índice = int(input('Digite o índice do aluno: ')) -1
		print('As notas do aluno {} são: {} e {}.'.format(dados[índice][0], dados[índice][2], dados[índice][3]))
