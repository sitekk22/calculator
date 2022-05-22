import pygame, os, time
from pygame.locals import *
    
WIDTH, HEIGHT = 360, 480
pygame.init()
FPS = 60.0
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
dt = 1/FPS
run = True
numbers = "" 
res = ""
TEXT_COLOR = (69, 40, 60)
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 36, bold=True)
   
BTN_WIDTH, BTN_HEIGHT = 75, 75 # default square


    
default =  pygame.image.load(os.path.join("imgs", "calc.png")) 
zero_pressed =  pygame.image.load(os.path.join("imgs", "0_pressed.png")) 
one_pressed = pygame.image.load(os.path.join("imgs", "1_pressed.png")) 
two_pressed = pygame.image.load(os.path.join("imgs", "2_pressed.png")) 
three_pressed = pygame.image.load(os.path.join("imgs", "3_pressed.png")) 
four_pressed = pygame.image.load(os.path.join("imgs", "4_pressed.png")) 
five_pressed = pygame.image.load(os.path.join("imgs", "5_pressed.png")) 
six_pressed = pygame.image.load(os.path.join("imgs", "6_pressed.png")) 
seven_pressed = pygame.image.load(os.path.join("imgs", "7_pressed.png")) 
eight_pressed = pygame.image.load(os.path.join("imgs", "8_pressed.png")) 
nine_pressed = pygame.image.load(os.path.join("imgs", "9_pressed.png")) 
add_pressed = pygame.image.load(os.path.join("imgs", "add_pressed.png")) 
subtract_pressed = pygame.image.load(os.path.join("imgs", "sub_pressed.png")) 
multiply_pressed = pygame.image.load(os.path.join("imgs", "mul_pressed.png")) 
divide_pressed = pygame.image.load(os.path.join("imgs", "div_pressed.png")) 
remove_pressed = pygame.image.load(os.path.join("imgs", "rm_pressed.png"))
equal_pressed = pygame.image.load(os.path.join("imgs", "eq_pressed.png")) 





    
class calculator(pygame.sprite.Sprite): 
    def __init__(self, img):
        self.x = 0
        self.y = 0
        self.flip = False
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.rect = self.img.get_rect()

    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip, False),self.rect)
        
        
class button(pygame.sprite.Sprite):
    def __init__(self,x,y, width, height):
        self.x = x
        self.y= y
        self.width = width
        self.height = height
        self.btn=Rect(self.x,self.y, self.width, self.height)
            

button1 = button(25, 145, BTN_WIDTH, BTN_HEIGHT)
button2 = button(115, 145, BTN_WIDTH, BTN_HEIGHT)
button3 = button(205, 145, BTN_WIDTH, BTN_HEIGHT)
button4 = button(25, 235, BTN_WIDTH, BTN_HEIGHT)
button5 = button(115, 235, BTN_WIDTH, BTN_HEIGHT)
button6 = button(205, 235, BTN_WIDTH, BTN_HEIGHT)
button7 = button(25, 325, BTN_WIDTH, BTN_HEIGHT)
button8 = button(115, 325, BTN_WIDTH, BTN_HEIGHT)
button9 = button(205, 325, BTN_WIDTH, BTN_HEIGHT)
button0 = button(25, 415, BTN_WIDTH, 45)

button_subtract = button(295, 415, 45, 45)
button_remove_char = button(295, 145, 45, 75)
button_equal = button(300,235, 45,75) 
button_add = button(295, 330, 45, 70)
button_divide = button(205, 415, 75,45)
button_multiply = button(115, 415, 75,45)    


def draw(screen, numbers):    
    screen_text = font.render(numbers, True, TEXT_COLOR)
    res_text = font.render(res, True, TEXT_COLOR)
    
    
    
    #time.sleep(0.5)
    
    space_num = 320 - len(numbers)*22
    space_res = 320 - len(res)*22
    
    screen.blit(screen_text, (space_num, 30))
    screen.blit(res_text,(space_res, 80))
    
    pygame.display.flip()
    
    
    

calc= calculator(default)




zero = False



while run:
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

        if event.type == MOUSEBUTTONDOWN:

            pos = event.pos
            #print(pos)
            
            
            if button0.btn.collidepoint(pos):
                
                calc.img = zero_pressed  
                numbers+="0"
                res = ""
            if button1.btn.collidepoint(pos):
                calc.img = one_pressed
                numbers+="1"
                res = ""
            if button2.btn.collidepoint(pos):
                calc.img = two_pressed 
                numbers+="2"
            if button3.btn.collidepoint(pos):
                calc.img = three_pressed
                numbers+= "3"
                res = ""
            if button4.btn.collidepoint(pos):
                calc.img = four_pressed
                numbers+= "4"
                res = ""
            if button5.btn.collidepoint(pos):
                calc.img = five_pressed
                numbers+= "5"
                res = ""
            if button6.btn.collidepoint(pos):
                calc.img = six_pressed
                numbers+= "6"
                res = ""
            if button7.btn.collidepoint(pos):
                calc.img = seven_pressed
                numbers+= "7"
                res = ""
            if button8.btn.collidepoint(pos):
                calc.img = eight_pressed
                numbers+= "8"
                res = ""
            if button9.btn.collidepoint(pos):
                calc.img = nine_pressed
                numbers+= "9"
                res = ""
            if button_remove_char.btn.collidepoint(pos):
                calc.img = remove_pressed
                try: 
                    
                    tmp = list(numbers)
                    tmp.pop()    
                    numbers = ''.join(tmp)
                except IndexError:
                    pass
            if button_subtract.btn.collidepoint(pos):
                numbers+= "-"
                calc.img = subtract_pressed             
            if button_add.btn.collidepoint(pos):
                numbers+= "+"
                calc.img = add_pressed
            if button_equal.btn.collidepoint(pos):
                
                try:
                    calc.img = equal_pressed
                    res = str(eval(numbers))
                    numbers = ""
                except (SyntaxError, ZeroDivisionError) as e :
                    print("BRUH")
                    numbers = ""
                
            if button_divide.btn.collidepoint(pos):
                numbers+= "/"
                calc.img = divide_pressed

            if button_multiply.btn.collidepoint(pos):
                numbers+= "*"       
                calc.img = multiply_pressed
               
        if event.type == MOUSEBUTTONUP:
            
            calc.img = default
    
      
    calc.draw()
    draw(screen, numbers)
    dt = fps_clock.tick(FPS)
    
