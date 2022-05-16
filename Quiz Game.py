from questoes import quiz
from random import sample
import operator

ranking={}

def mensagem_inicio(): #Função para mensagem de boas vindas ao jogador
    print("| |  | Q u i z   C o s m o s |  | |")
    print("Você está no jogo de perguntas cósmicas🪐👩‍🚀🌌! \nVamos Testar seu conhecimento sobre o universo?")
    print("Serão 5 perguntas divertidas sobre curiosidades e fatos do espaço sideral💫🌠")
    print()
    return True

def verificar(score): #verificação das respostas e atribuição de pontos
    if resposta.lower() == respostas.lower():
        print("=-=-=-=-="*10)
        print(f"Resposta Correta!\n\nSeu score:{score+1}\n")
        return True
    else:
        print("Você errou :(\n\n ")
        return False

if 'ranking.txt'== None: # Criação de um documento ranking.txt caso ainda não exista
    open('ranking.txt','x')
intro = mensagem_inicio()

while True:
    parte=1
    score=0
    user= input(str('Nome do Jogador> '))
    print()
    while parte < 6:
        score = score
        Lperguntas= quiz.keys()
        Lperguntas= list(Lperguntas)
        k=5
        Lista_perguntas= sample(Lperguntas, k) # Seleciona 5 itens aleatoriamente da lista criada apartir das chaves dicionário
        while True:
            for i in Lista_perguntas: # Exibe uma pergunta por vez dentre as perguntas sorteadas
                perguntas= i
            respostas= quiz.get(perguntas) # Variável procura a chave no dicionario que corresponde a pergunta exibida e recebe o valor 
            print(f'Pergunta {parte}')
            parte+=1
            print(perguntas)
            resposta = input("Digite a alternativa e pressione Enter para confirmar ( ' x ' para pular para a próxima ): ")
            if resposta == "x":
                print('\nVocê pulou a alternativa anterior\n')
                break
            check = verificar(score)
            if check:
                score += 1
                ranking[user]=score
                break
            else:
                break
      
    print(f"Pontuação: {score}!")
    users= sorted(ranking, key=ranking.get, reverse=True) # Ordena Nome dos jogadores em ordem decrescente
    print('\n\nR A N K I N G👑\n')
    for x in users: # Exibe jogadores da maior a menor pontuação
        print('%s: % .2f' %(x, ranking[x]))
    pnts= sorted(ranking.items(), key=operator.itemgetter(1), reverse=True) # Ordena o dicionario ranking de forma decrescente
    pnts= str(pnts)

    f=open('ranking.txt','w') # Salva o ranking em arquivo .txt
    f.write(pnts)
    f.close()

    # f = open('ranking.txt')
    # print(f.readlines())
    # f.close()
    print()
