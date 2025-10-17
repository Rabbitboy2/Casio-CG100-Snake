import casioplot as cs
import random  as r

global running
running = True
highscore = [0]

class Snake():
    def __init__(self):
        self.slices = [[100,100],[120,100],[140,100]]
        self.add = 0
        self.side = 20
        self.previousMove = 'r'
        self.firstItem = len(self.slices)-1
        for slice in self.slices:
            self.drawSlice(slice,(0,0,0))
    def checkCollision(self,front):
        count = 0
        for i in self.slices:
            if i == front:
                count += 1
        if front[1]> 9*20 or front[0]<0 or front[1]<0 or front[0]>360:
            return True
        if count > 1:
            return True
    def move(self,direction):
        self.firstItem = len(self.slices)-1
        itemx = self.slices[self.firstItem][0]
        itemy = self.slices[self.firstItem][1]
        if direction == 'r' and self.previousMove != 'l':
            itemx += self.side
        elif direction == 'l' and self.previousMove != 'r':
            itemx -= self.side
        elif direction == 'u' and self.previousMove != 'd':
            itemy -= self.side
        elif direction == 'd' and self.previousMove != 'u':
            itemy += self.side
        else:
            return 'error, invalid direction'
        self.previousMove = direction
        self.slices.append([itemx,itemy])
        rmTail = self.slices[0]
        if self.add == 0:
            self.slices.pop(0)
            self.drawSlice(rmTail,(255,255,255))
        else:
            self.add -= 1
        print(self.slices)
        self.drawSlice([itemx,itemy],(0,0,0))
        if self.checkCollision([itemx,itemy]):
            global running
            running = False
    def addSlice(self):
        self.add += 1
    def drawSlice(self,slice,colour):
        for x in range(slice[0]+1,slice[0]+self.side-1):
            cs.set_pixel(x,slice[1]+1,colour)
            cs.set_pixel(x,slice[1]+self.side-1,colour)
        for y in range(slice[1]+1,slice[1]+self.side-1):
            cs.set_pixel(slice[0]+1,y,colour)
            cs.set_pixel(slice[0]+self.side-1,y,colour)
    def appleCollide(self, apple):
        self.firstItem = len(self.slices)-1
        itemx = self.slices[self.firstItem][0]
        itemy = self.slices[self.firstItem][1]
        if apple.x >= itemx and (apple.x + apple.side) <= (itemx + self.side) and apple.y >= itemy and (apple.y+apple.side) <= (itemy+self.side):
            self.addSlice()
            return True
class Apple():
    def __init__(self):
        self.x = 20*r.randint(0,18)
        self.y = 20*r.randint(0,8)
        self.side = 10
        self.draw((0,0,0))
    def draw(self,colour):
        for x in range(self.x+5, self.x+self.side+5):
            cs.set_pixel(x,self.y+5,colour)
            cs.set_pixel(x,self.y+5+self.side,colour)
        for y in range(self.y+5,self.y+self.side+6):
            cs.set_pixel(self.x+5,y,colour)
            cs.set_pixel(self.x+5+self.side,y,colour)
    def remove(self):
        self.draw((255,255,255))

def mainMenu():
    cs.draw_string(120,70,'SNAKE',(0,0,0),'large')
    cs.draw_string(150,110,"(1) Easy")
    cs.draw_string(150,130,"(2) Normal")
    cs.draw_string(150,150,"(3) Hard")
    cs.draw_string(150,170,"(X) Impossible")
    cs.show_screen()
    while True:
        k = cs.getkey()
        if k == 81:
            mode = 'easy'
            clock = 2100
            appleNum = 2
            break
        if k == 82:
            mode = 'normal'
            clock = 1200
            appleNum = 1
            break
        if k == 83:
            mode = 'hard'
            clock = 900
            appleNum = 1
            break
        if k == 74:
            mode = 'impossible'
            clock = 600
            appleNum = 1
            break
    return clock,appleNum,mode

def shareHighScore(mode,score):
    import random as r
def shareHighScore(mode,score):
    alphabet = ['w', 'g', 'b', 'o', 'p', 'j', 'q', 'd', 'e', 'z', 'n', 's', 'h', 'v', 'k', 'r', 'c', 'y', 'f', 'x', '+', 't', 'l', 'm', 'u', 'a', 'i']    
    code = ''
    a = 1
    code2 = 0
    for x in mode:
        code2 += alphabet.index(x)
    if mode == 'easy':
        multipliers = [2,3,4,5,6]
    elif mode == 'normal':
        multipliers = [2,3,4,5,6]
    elif mode == 'hard':
        multipliers = [2,3,4,5,6]
    elif mode == 'impossible':
        multipliers = [2,3,4,5,6]
    code += str(r.choice(multipliers)*code2)
    power = 0
    while a > 0:
        a = score // (26**power)
        print(a)
        if a > 0:
            power += 1
    codeLs = []
    print(power)
    for x in range(power,-1,-1):
        poly = 26**x
        exactDiv = score//poly
        codeLs.append(exactDiv)
        score = score - poly*exactDiv
    for i in codeLs:
        code += alphabet[i]
    print(codeLs)
    return code
    
  
def gameOver(score,mode):
    if score > highscore[0]:
        highscore.pop()
        highscore.append(score)
    cs.clear_screen()
    cs.draw_string(120,70,"GAME OVER",(0,0,0),'large')
    cs.draw_string(150,110, "Score: "+str(score))
    cs.draw_string(150,130,"Highscore: "+str(highscore[0]))
    cs.draw_string(140,150,"Press OK to restart",(0,0,0),"small")
    cs.draw_string(145,160,"Press AC to end",(0,0,0),"small")
    cs.show_screen()
    while True:
        k = cs.getkey()
        if k == 24:
            global running 
            running = True
            break
        if k == 95:
            cs.clear_screen()
            cs.draw_string(0,0,shareHighScore(mode,highscore[0]),(0,0,0),'large')
            cs.show_screen()
def startGame(clockMax,maxApple,mode):
    snake = Snake()
    clockStepper = 0
    currDirection = 'r'
    currApple = 0
    appleLs = []
    while running:
        if currApple < maxApple:
            newInstance = Apple()
            currApple += 1
            appleLs.append(newInstance)
        clockStepper += 1
        if clockStepper %300 == 0:
            k = cs.getkey()
        else:
            k = 0
        if k == 14 and currDirection != 'd':
            currDirection = 'u'
        elif k == 34 and currDirection != 'u':
            currDirection = 'd'
        elif k == 23 and currDirection != 'r':
            currDirection = 'l'
        elif k == 25 and currDirection != 'l':
            currDirection = 'r'
        if clockStepper == clockMax:
            snake.move(currDirection)
            clockStepper = 0
            for apple in appleLs:
                result = snake.appleCollide(apple)
                if result:
                    currApple-=1
                    apple.remove()
                    appleLs.remove(apple)
            cs.show_screen()
    gameOver(len(snake.slices)-3,mode)
clock, appleNum,mode = mainMenu()
while True:
    cs.clear_screen()
    startGame(clock,appleNum,mode)