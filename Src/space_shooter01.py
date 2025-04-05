import pygame
import random
import sys

pygame.init()

largura_tela = 1000
altura_tela = 720
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Invasores Espaciais")
relogio = pygame.time.Clock()

#cores (podemos transformar num dicionario depois, só pra ficar mais modular)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
ROXO = (128, 0, 128)
LARANJA = (255, 165, 0)
CIANO = (0, 255, 255)

#classe do Jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura_tela // 2
        self.rect.bottom = altura_tela - 10
        self.velocidade = 8
        self.vidas = 3
        self.delay_tiro = 250  #milissegundos
        self.ultimo_tiro = pygame.time.get_ticks()
        self.pontuacao = 0
        self.powerup_tiro_duplo = False
        self.powerup_tiro_triplo = False
        self.tempo_powerup = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        
        self.rect.x = max(0, min(self.rect.x, largura_tela - self.rect.width))
        
        #atualiza tempo dos powerups
        if self.powerup_tiro_duplo or self.powerup_tiro_triplo:
            self.tempo_powerup += relogio.get_time()
            if self.tempo_powerup >= 10000:  # 10 segundos
                self.powerup_tiro_duplo = False
                self.powerup_tiro_triplo = False
                self.tempo_powerup = 0

    def atirar(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_tiro > self.delay_tiro:
            self.ultimo_tiro = agora
            
            if self.powerup_tiro_triplo:
                #tiro triplo em leque
                for deslocamento in [-20, 0, 20]:
                    tiro = Tiro(self.rect.centerx + deslocamento, self.rect.top)
                    tiro.velocidade_x = deslocamento / 10  #desvio lateral com base no deslocamento

                    todos_sprites.add(tiro)
                    tiros.add(tiro)

            elif self.powerup_tiro_duplo:
                #tiro duplo
                for deslocamento in [-15, 15]:
                    tiro = Tiro(self.rect.centerx + deslocamento, self.rect.top)
                    todos_sprites.add(tiro)
                    tiros.add(tiro)
            else:
                #tiro normal
                tiro = Tiro(self.rect.centerx, self.rect.top)
                todos_sprites.add(tiro)
                tiros.add(tiro)

#classe dos inimigos (cometas)
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(largura_tela - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidade_y = random.randrange(1, 5)
        self.velocidade_x = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.velocidade_y
        self.rect.x += self.velocidade_x

        if self.rect.top > altura_tela + 10 or self.rect.left < -25 or self.rect.right > largura_tela + 25:
            self.kill()

#classe dos tiros
class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidade_y = -10
        self.velocidade_x = 0

    def update(self):
        self.rect.y += self.velocidade_y
        self.rect.x += self.velocidade_x
        if self.rect.bottom < 0 or self.rect.top > altura_tela or self.rect.left < 0 or self.rect.right > largura_tela:
            self.kill()

#classe dos powerups
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, tipo, x=None, y=None):
        super().__init__()
        self.tipo = tipo
        
        if self.tipo == 'vida':
            self.image = pygame.Surface((25, 25))
            self.image.fill(ROXO)
        elif self.tipo == 'pontos':
            self.image = pygame.Surface((25, 25))
            self.image.fill(AMARELO)
        elif self.tipo == 'tiro_duplo':
            self.image = pygame.Surface((25, 25))
            self.image.fill(CIANO)
        elif self.tipo == 'tiro_triplo':
            self.image = pygame.Surface((25, 25))
            self.image.fill(LARANJA)
        
        self.rect = self.image.get_rect()
        if x and y:
            self.rect.centerx = x
            self.rect.centery = y
        else:
            self.rect.x = random.randrange(largura_tela - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
        self.velocidade_y = 2

    def update(self):
        self.rect.y += self.velocidade_y
        if self.rect.top > altura_tela:
            self.kill()

#classe do inimigo chefe
class InimigoChefe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 60))
        self.image.fill(ROXO)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura_tela // 2
        self.rect.y = 50
        self.velocidade_x = 3
        self.direcao = 1
        self.vida_maxima = 200
        self.vida_atual = self.vida_maxima
        self.delay_tiro = 1000
        self.ultimo_tiro = pygame.time.get_ticks()
        
    def update(self):
        self.rect.x += self.velocidade_x * self.direcao
        
        if self.rect.right > largura_tela or self.rect.left < 0:
            self.direcao *= -1
        
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_tiro > self.delay_tiro:
            self.ultimo_tiro = agora
            self.atirar()
    
    def atirar(self):
        for angulo in [-30, 0, 30]:
            cometa = CometaChefe(self.rect.centerx, self.rect.bottom)
            cometa.velocidade_y = 5
            cometa.velocidade_x = angulo / 10
            todos_sprites.add(cometa)
            cometas_chefe.add(cometa)
    
    def desenhar_barra_vida(self, superficie):
        largura_barra = 100
        altura_barra = 10
        vida_ratio = self.vida_atual / self.vida_maxima
        largura_atual = largura_barra * vida_ratio
        
        barra_rect = pygame.Rect(self.rect.x, self.rect.y - 15, largura_atual, altura_barra)
        fundo_rect = pygame.Rect(self.rect.x, self.rect.y - 15, largura_barra, altura_barra)
        
        pygame.draw.rect(superficie, VERMELHO, fundo_rect)
        pygame.draw.rect(superficie, VERDE, barra_rect)
        pygame.draw.rect(superficie, BRANCO, fundo_rect, 2)

class CometaChefe(Inimigo):
    def __init__(self, x, y):
        super().__init__()
        self.rect.centerx = x
        self.rect.centery = y
        self.image.fill(AMARELO)
        self.velocidade_y = 3
        self.velocidade_x = 0
        self.dano = 1

#grupos de sprites
todos_sprites = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
tiros = pygame.sprite.Group()
powerups = pygame.sprite.Group()
cometas_chefe = pygame.sprite.Group()
chefes = pygame.sprite.Group()

jogador = Jogador()
todos_sprites.add(jogador)

#cria inimigos iniciais
for i in range(8):
    inimigo = Inimigo()
    todos_sprites.add(inimigo)
    inimigos.add(inimigo)

tempo_spawn = 0
tempo_powerup = 0
jogo_terminado = False
spawn_chefe = False
fase_atual = 1
fonte = pygame.font.SysFont('Arial', 30)

#loop principal
rodando = True
while rodando:
    relogio.tick(60)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogador.atirar()
            if evento.key == pygame.K_r and jogo_terminado:
                jogo_terminado = False
                jogador.vidas = 3
                jogador.pontuacao = 0
                spawn_chefe = False
                jogador.powerup_tiro_duplo = False
                jogador.powerup_tiro_triplo = False

                for sprite in todos_sprites:
                    sprite.kill()

                jogador = Jogador()
                todos_sprites.add(jogador)

                for i in range(8):
                    inimigo = Inimigo()
                    todos_sprites.add(inimigo)
                    inimigos.add(inimigo)
    
    if not jogo_terminado:
        todos_sprites.update()
        
        #aparece o chefe quando o jogador alcança 100 pontos
        if jogador.pontuacao >= 100 and not spawn_chefe and len(chefes) == 0:
            chefe = InimigoChefe()
            todos_sprites.add(chefe)
            chefes.add(chefe)
            spawn_chefe = True
        
        #colisões entre tiros e inimigos normais
        colisoes = pygame.sprite.groupcollide(inimigos, tiros, True, True)
        for colisao in colisoes:
            jogador.pontuacao += 10
            #chance de dropar um powerup (10%) melhor aumentar até
            if random.random() < 0.1:
                tipos = ['vida', 'pontos', 'tiro_duplo', 'tiro_triplo']
                powerup = PowerUp(random.choice(tipos))
                powerup.rect.centerx = colisao.rect.centerx
                powerup.rect.centery = colisao.rect.centery
                todos_sprites.add(powerup)
                powerups.add(powerup)
            inimigo = Inimigo()
            todos_sprites.add(inimigo)
            inimigos.add(inimigo)
        
        #colisões entre tiros e chefes
        if spawn_chefe:
            for chefe in chefes:
                colisoes_chefe = pygame.sprite.spritecollide(chefe, tiros, True)
                for tiro in colisoes_chefe:
                    chefe.vida_atual -= 10
                    if chefe.vida_atual <= 0:
                        chefe.kill()
                        jogador.pontuacao += 100
                        spawn_chefe = False
                
        #colisões entre jogador e inimigos normais
        colisoes = pygame.sprite.spritecollide(jogador, inimigos, True)
        for colisao in colisoes:
            jogador.vidas -= 1
            inimigo = Inimigo()
            todos_sprites.add(inimigo)
            inimigos.add(inimigo)
            if jogador.vidas <= 0:
                jogo_terminado = True
        
        #colisões entre jogador e cometas do chefe
        colisoes_cometa = pygame.sprite.spritecollide(jogador, cometas_chefe, True)
        for cometa in colisoes_cometa:
            jogador.vidas -= cometa.dano
            if jogador.vidas <= 0:
                jogo_terminado = True
        
        #colisões entre jogador e powerups
        colisoes = pygame.sprite.spritecollide(jogador, powerups, True)
        for powerup in colisoes:
            if powerup.tipo == 'vida':
                jogador.vidas += 1
            elif powerup.tipo == 'pontos':
                jogador.pontuacao += 50
            elif powerup.tipo == 'tiro_duplo':
                jogador.powerup_tiro_duplo = True
                jogador.powerup_tiro_triplo = False
                jogador.tempo_powerup = 0
            elif powerup.tipo == 'tiro_triplo':
                jogador.powerup_tiro_triplo = True
                jogador.powerup_tiro_duplo = False
                jogador.tempo_powerup = 0
        
        #spawn de inimigos ao longo do tempo (só na fase 1)
        if fase_atual == 1:
            tempo_spawn += 1
            if tempo_spawn > 60 and len(inimigos) < 10:
                tempo_spawn = 0
                inimigo = Inimigo()
                todos_sprites.add(inimigo)
                inimigos.add(inimigo)
        
        #spawn de powerups ao longo do tempo
        tempo_powerup += 1
        if tempo_powerup > 300:
            tempo_powerup = 0
            if random.random() < 0.3:  # 30% de chance
                tipos = ['vida', 'pontos', 'tiro_duplo', 'tiro_triplo']
                powerup = PowerUp(random.choice(tipos))
                todos_sprites.add(powerup)
                powerups.add(powerup)
    
    tela.fill(PRETO)
    todos_sprites.draw(tela)
    
    #desenha a barra de vida do chefe se ele estiver vivo
    if spawn_chefe:
        for chefe in chefes:
            chefe.desenhar_barra_vida(tela)
    
    #mostra a pontuação e vidas
    texto_pontuacao = fonte.render(f"Pontuação: {jogador.pontuacao}", True, BRANCO)
    tela.blit(texto_pontuacao, (10, 10))
    
    texto_vidas = fonte.render(f"Vidas: {jogador.vidas}", True, BRANCO)
    tela.blit(texto_vidas, (10, 50))
    
    #mostra powerups ativos
    y_deslocamento = 90
    if jogador.powerup_tiro_duplo:
        tempo_restante = max(0, (10000 - jogador.tempo_powerup) // 1000)
        texto_powerup = fonte.render(f"Tiro Duplo: {tempo_restante}s", True, CIANO)
        tela.blit(texto_powerup, (10, y_deslocamento))
        y_deslocamento += 30
    
    if jogador.powerup_tiro_triplo:
        tempo_restante = max(0, (10000 - jogador.tempo_powerup) // 1000)
        texto_powerup = fonte.render(f"Tiro Triplo: {tempo_restante}s", True, LARANJA)
        tela.blit(texto_powerup, (10, y_deslocamento))
    
    if jogo_terminado:
        texto_game_over = fonte.render("FIM DE JOGO! Pressione R para reiniciar", True, VERMELHO)
        tela.blit(texto_game_over, (largura_tela//2 - 180, altura_tela//2))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
