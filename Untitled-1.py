from pygame import*
#параметры экрана и скорость шара
w_h = 600
w_v = 500
speed_x = 3
speed_y = 3
font.init()
#дефолт класс для спрайта
class GS(sprite.Sprite):
    def __init__ (self,p_i,p_x,p_y,p_s,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(p_i),(size_x,size_y))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.directs = 'right'
    def reset(self):
        win.blit(self.image,(self.rect.x ,self.rect.y ))
#реализация для ракеток
class Player(GS):
    def update1(self):
        key_p = key.get_pressed()
        if key_p[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_p[K_s] and self.rect.y < w_h - 280:
            self.rect.y += self.speed
    def update2(self):
        key_p = key.get_pressed()
        if key_p[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_p[K_DOWN] and self.rect.y < w_h - 280:
            self.rect.y += self.speed


    
    

#cоздание интерфейса     
win = display.set_mode((w_h,w_v))
back = (255,255,200 )
display.set_caption('Пинг Понг')

pl1 = Player('Roc.png',30,200,10,20,200)
pl2 = Player('Roc.png',520,200,10,20,200)
ball = GS('ball.png',200,200,3,50,50)
bal = font.SysFont(None,70)
clock = time.Clock()
tex1f = bal.render('Player 1 Win',1,(255,0,0))
tex2f = bal.render('Player 2 Win',1,(0,255,0))

FPS = 60
no_f = 0
rec = False
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


                
#условия выиграша и проигрыша 
    if finish != True:
        win.fill(back)
        pl1.reset()
        pl2.reset()
        pl1.update1()
        pl2.update2()
        ball.reset()
        ball.rect.x += speed_x 
        ball.rect.y += speed_y
        
        if sprite.collide_rect(ball,pl1) or sprite.collide_rect(ball,pl2):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > w_h - 140 or ball.rect.y < 0:
            speed_y *= -1
            speed_x *= 1
        if ball.rect.x < 0 :
            finish =True
            win.blit(tex2f,(150,200))
        if ball.rect.x > w_v + 60 :
            finish =True
            win.blit(tex1f,(150,200))



    display.update()
    clock.tick(FPS)
