import pygame
from random import randint
import os.path
pygame.init()
pygame.font.init()


#Ja tenho as posições dentro do jogo, sem o sapo ou a cobra irem para o placar
lista_x = []
lista_y = []
for i in range(40, 380 + 1, 10): #Para as posições serem geradas dps do placar, verticalmente, e sem ter chance do boneco ir para fora do mapa
    lista_y.append(i)

for j in range(0, 380 + 1, 10): #Para as posições serem geradas em qualquer lugar, horizontalmente
    lista_x.append(j)

running = False


black = (0, 0, 0)
green = (0,255,0)
verde_claro = (153, 204, 255)
verde_escuro = (51, 153, 255)
vermelho = (255, 0, 0)
white = (255, 255, 255)
lala = (0, 64, 128)

largura, altura = 400, 400
fundo = pygame.display.set_mode((largura, altura))
tamanho_da_cobra = 20
maior = 0

pygame.display.set_caption("Snake Lunch ^^ ")

#Para o menu
def menu():
    fundo.fill((93, 216, 228))
    # Baixa a fonte
    fontee = pygame.font.SysFont(None, 70)
    fonte = pygame.font.SysFont(None, 40)

    # Renderiza na cor que desejar
    titulo_na_tela = fontee.render("SNAKE GAME", 1, black)
    classico = fonte.render("MODO CLÁSSICO", 1, white)
    dificil = fonte.render("MODO DIFÍCIL", 1, white)

    #Botões
    botao_1 = pygame.draw.rect(fundo, black, [10, 260, 200, 30])
    botao_2 = pygame.draw.rect(fundo, black, [10, 220, 240, 30])

    # Coloca na posição exata
    fundo.blit(titulo_na_tela, (30, 130))
    fundo.blit(classico, (10, 220))
    fundo.blit(dificil, (10, 260))

    #Imagem da cobra
    cobrinha = pygame.image.load("data/snake.png")
    fundo.blit(cobrinha, (190, 140))
    pygame.display.update()




#Para o fundo ficar listrado
def backgroundnojogo():
    fundo.fill(white)
    for i in range(40, altura + 1, 10):
        for j in range(0, largura + 1, 10):
            if (i//10) % 2 == 0:
                azuis_claros_primeira = pygame.draw.rect(fundo, (93, 216, 228), [j + 10, i, 10, 10])
                azuis_escuros_primeira = pygame.draw.rect(fundo, (84, 194, 205), [j , i, 10, 10])
            else:
                azuis_claros_segunda = pygame.draw.rect(fundo, (93, 216, 228), [j, i, 10, 10])
                azuis_escuros_segunda = pygame.draw.rect(fundo, (84, 194, 205), [j + 10, i, 10, 10])




#Para mostrar a cobra
def CobraCabeça(ListaCobra, acontecer):
    global cabeça
    if acontecer:
        for i in range(0,len(ListaCobra)):
            cabeça = pygame.draw.rect(fundo, (0, 51, 0), [ListaCobra[i][0], ListaCobra[i][1], tamanho_da_cobra, tamanho_da_cobra])
            olho = pygame.draw.rect(fundo, white, [ListaCobra[len(ListaCobra)-1][0], ListaCobra[len(ListaCobra)-1][1] + 2, 5, 5])
            olho_2 =  pygame.draw.rect(fundo, white, [ListaCobra[len(ListaCobra)-1][0] + 15, ListaCobra[len(ListaCobra)-1][1] + 2, 5, 5])





#Para o objeto pegado pela cobra
def SapoOuMaça(acontecer, movimentar, lado, frente):
    if acontecer == True and movimentar == True:
        global rect_sapo, rect_maca
        imagem_sapo = pygame.image.load("data/Froggit.png")
        para_modificar = imagem_sapo.convert()
        tamanho_sapo = pygame.transform.scale(para_modificar, (20, 20)) #Superficie
        tamanho_sapo.set_colorkey((0,0,0)) #Fundo Transparente
        fundo.blit(tamanho_sapo, (lado, frente))
        rect_sapo = tamanho_sapo.get_rect()
        rect_sapo.topleft = lado, frente
    if acontecer == True and movimentar == False:
        imagem_maca = pygame.image.load("data/unnamed.png")
        modificar = imagem_maca.convert()
        tamanho_maca = pygame.transform.scale(modificar, (20, 20)) #Superficie
        tamanho_maca.set_colorkey((0,0,0)) #Fundo Transparente
        fundo.blit(tamanho_maca,(lado, frente))
        rect_maca = tamanho_maca.get_rect()
        rect_maca.topleft = lado, frente






#Durante o jogo, vai a mostrar a quantidade de pontos totais, tanto dessa partida como de outra
def Pontos(durante_o_jogo, pontos):
    if durante_o_jogo:
        quando_for_aparecer = pygame.font.SysFont(None, 30) #Para usar a fonte default
        texto = quando_for_aparecer.render("SCORE: " + str(pontos), 30, black) #O que vai aparecer
        aparece_pontoss = fundo.blit(texto, (5, 12))


#Vai aparecer quando bater na borda, ou seja x > largura ou x < 0, y > altura ou y < 0
def TelaFimDeJogo(fim_de_jogo,pontos, maior_pontuacao):
    if fim_de_jogo:
        #Background
        fundo.fill(white)
        for i in range(0, altura + 1, 10):
            for j in range(0, largura + 1, 10):
                if (i // 10) % 2 == 0:
                    azuis_claros_primeira = pygame.draw.rect(fundo, (93, 216, 228), [j + 10, i, 10, 10])
                    azuis_escuros_primeira = pygame.draw.rect(fundo, (84, 194, 205), [j, i, 10, 10])
                else:
                    azuis_claros_segunda = pygame.draw.rect(fundo, (93, 216, 228), [j, i, 10, 10])
                    azuis_escuros_segunda = pygame.draw.rect(fundo, (84, 194, 205), [j + 10, i, 10, 10])

        #Botões de escolher modo de novo, e jogar
        pygame.draw.rect(fundo, black, [112, 265, 175, 23])
        pygame.draw.rect(fundo, black, [168, 305, 55, 23])
        titulo = pygame.font.SysFont(None, 60)
        quando_for_aparecer = pygame.font.SysFont( None, 30)
        texto_3 = quando_for_aparecer.render("JOGAR DE NOVO", 45, white)
        fundo.blit(texto_3, (115, 270))

        #Botão sair
        texto_4 = quando_for_aparecer.render("SAIR", 45, white)
        fundo.blit(texto_4, (170, 310))

        #Maior pontuação
        if pontos > maior_pontuacao:
            maior_pontuacao = pontos
        texto_5 = quando_for_aparecer.render("HIGHSCORE: " + str(maior_pontuacao), 45, black)
        fundo.blit(texto_5, (125, 200))

        #Imagem de game over
        game_over_tamanho_certo = titulo.render("GAME OVER", 45, black)
        fundo.blit(game_over_tamanho_certo, (75, 150))







#O jogo é nada mais nada menos que um grande loop com funções
def jogo(maior):

    #Utilizei o sistema de TRUE ou FALSE para ter mais controle sobre os acontecimentos que estão passando na telase
    acontecer = True  #para o sapo e a cobra serem desenhados
    running = False
    durante_o_jogo = True #tela com o score, highscore, fundo azul listrado
    fim_de_jogo = False #tela de fim de jogo, com game over


    #Tela de menu, antes de começar o jogo
    while running == False:
        menu()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_x = mouse_pos[0]
                mouse_y = mouse_pos[1]
                if 9 < mouse_x < 250 and 220 < mouse_y < 250:
                    running = True  # Inicia o jogo
                    movimentar = False  # A maçã parada aparece
                if 12 < mouse_x < 209 and 260 < mouse_y < 290:
                    running = True  # Inicia o jogo
                    movimentar = True # O sapo se movimentando e a aranha aparecem


    #Para as posições serem geradas aleatoriamente
    pos_x_la = randint(0, len(lista_x)-1)
    pos_y_la = randint(0, len(lista_y)-1)
    lado_x = randint(0, len(lista_x)-1)
    frente_y = randint(0, len(lista_y)-1)

    #Para a cabeça da cobra
    pos_x = lista_x[pos_x_la] #O randint é utilizado para a cobra aparecer em algum ponto aleatório do mapa
    pos_y = lista_y[pos_y_la]
    velocidade_x = 0
    velocidade_y = 0

    #Para o corpo da cobra
    Cobra_XY = []
    Comprimento = 2

    direita = 0
    if movimentar == True: #Para o sapo começar a andar do x zero
        lado = 0
        frente = lista_y[frente_y]

    if movimentar == False: #Para a maça ser gerada aleatoriamente em x, y
        lado = lista_x[lado_x]
        frente = lista_y[frente_y]

    #Para a pontuação
    pontos = 0

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and fim_de_jogo == True: #Quando o jogo acabar
                mouse_pos = pygame.mouse.get_pos()
                mouse_x = mouse_pos[0]
                mouse_y = mouse_pos[1]
                if 112 < mouse_x < 284 and 265 < mouse_y < 287:
                    if pontos > maior:
                        maior = pontos
                        jogo(maior)
                    else:
                        jogo(maior)
                if 160 < mouse_x < 220 and 300 < mouse_y < 325:
                    pygame.quit()
            if event.type == pygame.KEYDOWN: #Apertar em qualquer tecla
                if event.key == pygame.K_LEFT and velocidade_x != 10: #Depois que a esquerda tiver sido apertada ela não pode ir para a direita
                    velocidade_x = -10
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT and velocidade_x != -10: #Depois que a direita tiver sido apertada, ela não pode ir para a esquerda
                    velocidade_x = 10
                    velocidade_y = 0
                if event.key == pygame.K_UP and velocidade_y != 10: #Tecla cima
                    velocidade_x = 0
                    velocidade_y = -10
                if event.key == pygame.K_DOWN and velocidade_y != -10: #Tecla baixo
                    velocidade_x = 0
                    velocidade_y = 10
                if event.key == pygame.K_s:
                    running = False
                    pygame.quit()

        # Aqui acumula-se a posição com a velocidade para a cobra se mover
        pos_x +=velocidade_x
        pos_y += velocidade_y
        backgroundnojogo()

        #Caso o modo dificil tenha sido escolhido, o sapo será mostrado e ele andará na horizontal:
        if movimentar == True:
            # Para verificar se ela bateu na parede ou n
            if lado == 0: #Parede do numero 400, borda direita
                direita = True
            if lado == 390:
                direita = False
             #Parede do 0, borda esquerda

            #Para se mover da esquerda pra direita, e da direita pra esquerda
            if direita == True:
                lado += 10
            else:
                lado -= 10

        #Para o corpo da cobra
        CabeçaDaCobra = []
        CabeçaDaCobra.append(pos_x)
        CabeçaDaCobra.append(pos_y) #[x, y]
        Cobra_XY.append(CabeçaDaCobra)#Aqui é uma lista com as coordenadas em forma de lista: [[0, 10], [0, 30]]
        if len(Cobra_XY) > Comprimento:
            del Cobra_XY[0]#Excluir sempre o primeiro [x,y], para nao ir crescendo infinitamente

        CobraCabeça(Cobra_XY, acontecer) #Desenho da cobra se movendo
        SapoOuMaça(acontecer, movimentar, lado, frente) #Sapo ou maça
        Pontos(durante_o_jogo, pontos) #Background durante o jogo, com o placar
        TelaFimDeJogo(fim_de_jogo, pontos, maior)#Background final
        if movimentar == True:
            pygame.time.Clock().tick(20)
        if movimentar == False:
            pygame.time.Clock().tick(5)
        pygame.display.update()


        # Para quando for colidir com a maçã, ela ir para outro lugar e a cobra crescer.
        if movimentar == False:
            if pygame.Rect.colliderect(rect_maca, cabeça):
                novo_lado_x = randint(0, len(lista_x)-1)
                lado = lista_x[novo_lado_x]
                nova_frente_y = randint(0, len(lista_y)-1)
                frente = lista_y[nova_frente_y]
                pontos += 10
                Comprimento +=1
                pygame.mixer.music.load("data/sd_0.wav")
                pygame.mixer.music.play(1)

        if movimentar == True:
            if pygame.Rect.colliderect(rect_sapo, cabeça):
                novo_lado_x = randint(0, len(lista_x)-1)
                lado = lista_x[novo_lado_x]
                nova_frente_y = randint(0, len(lista_y)-1)
                frente = lista_y[nova_frente_y]
                pontos += 10
                Comprimento +=1
                pygame.mixer.music.load("data/sd_0.wav")
                pygame.mixer.music.play(1)


        # Vai perder quando atravessar a borda ou quando bater em si mesmo.
        if pos_x > largura  or pos_x < 0 or pos_y > altura - 20 or pos_y < 40:
            velocidade_x = 0
            velocidade_y = 0
            lado = 0
            fim_de_jogo = True
            durante_o_jogo = False
            acontecer = False

        if any(block == CabeçaDaCobra for block in Cobra_XY[:-2]):
            velocidade_x = 0
            velocidade_y = 0
            lado = 0
            fim_de_jogo = True
            durante_o_jogo = False
            acontecer = False

jogo(maior)
