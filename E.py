import random

des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |      Você Foi Enforcado! 
=========
''']

BookPalavras = random.choice(['arroz', 'feijao', 'feijoada', 'tapioca', 'tranca', 'truco', 'poker', 'paciencia', 'cadeado', 'quadro', 'catraca', 'xicara','lichia', 'morango', 'maracuja', 'abacaxi', 'Inconstitucionalissimamente','otorrinolaringologista', 'teclado', 'monitor', 'microfone', 'mouse'])
contagem = int(0)
tentativas = int(0)
i = int(0)
acertos = []
tentadas = []
fim = int(0)
print('*** Jogo da Forca ***')
print(des_forca[0])

if BookPalavras == 'arroz' or BookPalavras == 'feijao' or BookPalavras == 'feijoada' or BookPalavras == 'tapioca':
    print("Comida tipica Brasileira")
if BookPalavras == 'lichia' or BookPalavras == 'morango' or BookPalavras == 'maracuja' or BookPalavras == 'abacaxi':
    print("Fruta")
if BookPalavras == 'tranca' or BookPalavras == 'truco' or BookPalavras == 'Poker' or BookPalavras == 'paciencia':
    print("Jogo de Baralho")
if BookPalavras ==  'cadeado' or BookPalavras == 'quadro' or BookPalavras == 'catraca' or BookPalavras == 'xicara':
    print("Objeto")
if BookPalavras == 'otorrinolaringologista' or BookPalavras == 'Inconstitucionalissimamente':
    print("Difícil pra C*@#%&!")
if BookPalavras == 'teclado' or BookPalavras == 'monitor' or BookPalavras == 'microfone' or BookPalavras == 'mouse':
    print("Periféricos")
senha=""
for letra in BookPalavras:
        if letra in acertos:
            senha += letra
        else:
            senha += " _ "
while tentativas < 6 and senha != BookPalavras:
    print(senha)

    letra = input("Digite uma letra")
    while letra in tentadas:
        letra = input("Você esta digitando a mesma letra, digite uma diferente")

    tentadas += letra
    if letra in BookPalavras:
        acertos += letra
    else:
        i = i + 1
        tentativas = tentativas + 1
        print(des_forca[i])

    senha = ""
    for letra in BookPalavras:
        if letra in acertos:
            senha+=letra
        else:
            senha += " _ "

if senha == BookPalavras:
    print("A palavra correta é: %s" % senha)
    print("Você ganhou!")