import g2d_pyg as g2d
import random
import sys

class Snake(): 
    def __init__(self, w, h):
        self._dim = 20
        self._x = w//2
        self._y = h//2
        self._dx = 0
        self._dy = 0
        self._xc = -1
        self._yc = -1
        self._lastMove = ''
        self._currentMove = ''
        self._points = 0
        self._tail = []

    def biteSelf(self):
        for i in range(len(self._tail)):
            if (self._x == self._tail[i]._x) and (self._y == self._tail[i]._y):
                self.restart()
                break

    def restart(self):
        global c
        self._x = w//2
        self._y = h//2
        self._dx = 0
        self._dy = 0
        self._xc = -1
        self._yc = -1
        self._lastMove = ''
        self._currentMove = ''
        self._points =0
        self._tail = []
        c = 3

    def move(self):
        global collide

        self._points = int(self._points)
        if (self.position() == f.position()):
            collide = True
            f.relocate()
            self._tail.append(TailElement(self._x, self._y))
            self._points += 1

        if self._points == len(self._tail):           
            for i in range(len(self._tail)):
                if (self._tail[i]._x in f.position()) and (self._tail[i]._y in f.position()):
                    f.relocate()
                if (i + 1) >= len(self._tail):
                    self._tail[i]._x = self._x
                    self._tail[i]._y = self._y
                    break
                else:
                    self._tail[i]._x = self._tail[i + 1]._x
                    self._tail[i]._y = self._tail[i + 1]._y
        
        if (pos == 3):                      #if mod is hard the snake is costrained to the arena

            self._x += self._dx * self._dim
            if self._x != 0:
                if self._x + (self._dx * self._dim) == self._x:     #checks if the snake has moved in the x axis
                    self._xc = 0
                else:
                    self._xc = 1    #flags the movement

            if (self._x - self._dim < 0 - self._dim):
                self.restart()
                
            elif (self._x + self._dim > w):
                self.restart()
                
            self._y += self._dy * self._dim
            if self._y != 0:
                if self._y + (self._dy * self._dim) == self._y:     #same as before but on the y axis
                    self._yc = 0
                else:
                    self._yc = 1

            if (self._y - self._dim < 0 - self._dim):
                self.restart()

            elif (self._y + self._dim > h):
                self.restart()

        else:                              #in easy mod box has no limits

            self._x += self._dx * self._dim
            if self._x != 0:
                if self._x + (self._dx * self._dim) == self._x:
                    self._xc = 0
                else:
                    self._xc = 1

            if (self._x == 0 - self._dim):
                self._x = 600
            elif (self._x == w):
                self._x = 0

   
            self._y += self._dy * self._dim
            if self._y != 0:
                if self._y + (self._dy * self._dim) == self._y:
                    self._yc = 0
                else:
                    self._yc = 1

            if (self._y == 0 - self._dim):
                self._y = 600
            elif (self._y == h):
                self._y = 0

    def position(self):
        return (self._x, self._y)
            
    def draw(self):
        global c
        global collide
        global r, g, b
        a1, a2, a3, b1, b2, b3, c1, c2, c3 = 0
        c = int(c)
        if (collide == True) and (self._points > 5) and (self._points % 6 == 0): 
                c += 1        
        collide = False

        if defaultColor == True:            #this set of numbers changes the colors of the snake
            a1 = r - 5
            a2 = r + 15
            a3 = r + 15

            b1 = g - 40
            b2 = g - 150
            b3 = g - 65

            c1 = b -5
            c2 = b + 15
            c3 = b + 15

        elif color == 1:
            a1 = 255
            b1 = 190
            c1 = 0

            a2 = 160
            b2 = 130
            c2 = 11

            a3 = 220
            b3 = 170
            c3 = 32

        elif color == 2:
            a1 = 0
            b1 = 190 
            c1 = 190

            a2 = 0
            b2 = 120
            c2 = 120

            a3 = 0
            b3 = 170
            c3 = 170
            
        elif color == 3:
            a1 = 160
            b1 = 10
            c1 = 10

            a2 = 105
            b2 = 0
            c2 = 0

            a3 = 140
            b3 = 20
            c3 = 20

        for i in range(self._points):
            if (i >= self._points - c):
                #g2d.draw_circle((a1, b1, c1), (self._tail[i]._x, self._tail[i]._y), (10))
                g2d.draw_rect((a1, b1, c1), (self._tail[i]._x, self._tail[i]._y, self._dim, self._dim))
                #expanding at times part
            elif (i < 3):
                #g2d.draw_circle((a2, b2, c2), (self._tail[i]._x, self._tail[i]._y), (10))
                g2d.draw_rect((a2, b2, c2), (self._tail[i]._x, self._tail[i]._y, self._dim, self._dim))
                #edge part
            else:
                #g2d.draw_circle((a3, b3, c3), (self._tail[i]._x, self._tail[i]._y), (10))
                g2d.draw_rect((a3, b3, c3), (self._tail[i]._x, self._tail[i]._y, self._dim, self._dim))
                #increasing for every point part

        #g2d.draw_circle((r, g, b), (self._x, self._y), (10))
        g2d.draw_rect((r, g, b), (self._x, self._y, self._dim, self._dim))

    def go_left(self):

        self._currentMove = 'left'
        if self._lastMove == self._currentMove:
            return
        if (self._y + (self._dy * self._dim) != self._y) :
            if self._yc == 0:
                return
        self._dx, self._dy = -1, 0
        self._lastMove = 'right'
        
    def go_right(self):

        self._currentMove = 'right'
        if self._lastMove == self._currentMove:
            return
        if (self._y + (self._dy * self._dim) != self._y) :
            if self._yc == 0:
                return
        self._dx, self._dy = 1, 0
        self._lastMove = 'left'

    def go_up(self):

        self._currentMove = 'up'
        if self._lastMove == self._currentMove:
            return
        if (self._x + (self._dx * self._dim) != self._x): 
            if self._xc == 0:
                return
        self._dx, self._dy = 0, -1
        self._lastMove = 'down'
            
    def go_down(self):

        self._currentMove = 'down'
        if self._lastMove == self._currentMove:
            return
        if (self._x + (self._dx * self._dim) != self._x):
            if self._xc == 0:
                return
        self._dx, self._dy = 0, 1
        self._lastMove = 'up'


'///////////////////////////////////////////////////////////////'

class TailElement():
    def __init__(self, x, y):
        self._x = x
        self._y = y

'///////////////////////////////////////////////////////////////'
        
class Food():
    def __init__(self, w, h):
        self._dim = 20
        self._col = (w - self._dim) // self._dim
        self._row = (h - self._dim) // self._dim
        self._x = random.randint(1, self._col - 1) * self._dim
        self._y = random.randint(1, self._row - 1) * self._dim       
        
    def draw(self):
        global af, bf, cf
        if defaultColor == True:
            af = 230
            bf = 210
            cf = 20

        g2d.draw_rect((af, bf, cf), (self._x, self._y, self._dim, self._dim))

    def position(self):
        return (self._x, self._y)
    
    def relocate(self):
        if collide == True:
            if (pos == 2):
                self._x = random.randint(2, self._col - 2) * self._dim
                self._y = random.randint(2, self._row - 2) * self._dim
            else:
                self._x = random.randint(1, self._col - 1) * self._dim
                self._y = random.randint(1, self._row - 1) * self._dim 

'/////////////////////////////////////////////////////////////////'

class colorMenu():
    def __init__(self, width, height):
        self._w = width
        self._h = height

    def draw(self):
        global r, g, b
        global af, bf, cf
        g2d.fill_canvas((0, 0, 0))

        if colorPos == 1:
            r = 240
            g = 215
            b = 0

            af = 0
            bf = 0
            cf = 0

            g2d.draw_rect((255, 255, 255), (60, 131, 65, 28))
            g2d.draw_text(('Gold'), (240, 215, 0), (64, 134), (36))
            #g2d.draw_image((sprites2), (300, 125))
            g2d.draw_rect((200,90,90), (300, 125, 280, 280))
            g2d.draw_rect((af, bf, cf), (325, 255, 20, 20))
            g2d.draw_rect((r, g, b), (440, 255, 20, 20))
        else:
            g2d.draw_text(('Gold'), (240, 205, 0), (64, 134), (36))

        if colorPos == 2:
            r = 0
            g = 229
            b = 229

            af = 220
            bf = 20
            cf = 60

            g2d.draw_rect((255, 255, 255), (60, 221, 62, 28))
            g2d.draw_text(('Blue'), (0, 255, 255), (64, 224), (36))
            #g2d.draw_image((sprites2), (300, 125))
            g2d.draw_rect((188,143,143), (300, 125, 280, 280))
            g2d.draw_rect((af, bf, cf), (325, 255, 20, 20))
            g2d.draw_rect((r, g, b), (440, 255, 20, 20))
        else:
            g2d.draw_text(('Blue'), (0, 255, 255), (64, 224), (36))

        if colorPos == 3:
            r = 220 
            g = 20
            b = 20

            af = 20
            bf = 220
            cf = 77

            g2d.draw_rect((255, 255, 255), (60, 315, 53, 28))
            g2d.draw_text(('Red'), (220, 20, 60), (64, 318), (36))
            #g2d.draw_image((sprites2), (300, 125))
            g2d.draw_rect((31,117,169), (300, 125, 280, 280))
            g2d.draw_rect((af, bf, cf), (325, 255, 20, 20))
            g2d.draw_rect((r, g, b), (440, 255, 20, 20))
        else:
            g2d.draw_text(('Red'), (220, 20, 60), (64, 318), (36))

        if colorPos == 4:
            r = 35
            g = 220
            b = 35

            af = 230
            bf = 210
            cf = 20

            g2d.draw_rect((255, 255, 255), (60, 405, 93, 28))
            g2d.draw_text(('Default'), (22, 220, 40), (64, 408), (36))
            #g2d.draw_image((sprites2), (300, 125))
            g2d.draw_rect((159,73,7), (300, 125, 280, 280))
            g2d.draw_rect((af, bf, cf), (325, 255, 20, 20))
            g2d.draw_rect((r, g, b), (440, 255, 20, 20))
        else:
            g2d.draw_text(('Default'), (22, 220, 40), (64, 408), (36))

    def go_down(self):
        global colorPos
        if colorPos >= 4:
            colorPos = 4
            return
        colorPos += 1

    def go_up(self):
        global colorPos
        if colorPos <= 1:
            colorPos = 1
            return
        colorPos -= 1
        
'/////////////////////////////////////////////////////////////////'

class Menu():
    def __init__(self, width, height):
        self._w = width
        self._h1 = height
        
    def draw(self):
        global r, g, b
        global af, bf, cf
        global colorPos

        wd = self._w // 2.3 
        hg1 = self._h1 // 3.35
        hg2 = self._h1 // 2.30
        hg3 = hg2 + (hg2 - hg1)
        posx = wd - 7
        posy1 = hg1 - 4
        posy2 = hg2 - 5
        posy3 = hg3 - 4
        g2d.fill_canvas((0, 0, 0))
        
        if (pos == 1): 
            g2d.draw_rect((240, 240, 240), (posx, posy1, 85, 37))

        if (pos == 2):
            g2d.draw_rect((240, 240, 240), (posx - 2, posy2, 93, 37))
            g2d.draw_text(('Color'), (245, 200, 0), (wd - 3, hg2), (46))
        else:
            g2d.draw_text(('Color'), (250, 240, 0), (wd - 3, hg2), (46))
        
        if (pos == 3):
            g2d.draw_rect((240, 240, 240), (posx, posy3, 85, 37))
            g2d.draw_text(('Hard'), (210, 40, 40), (wd, hg3), (46))
        else:
            g2d.draw_text(('Hard'), (255, 40, 40), (wd, hg3), (46))
            
        g2d.draw_text(('Easy'), (22, 220, 40), (wd, hg1), (46))
        
        if color == 1:
            colorPos = 1
            r = 240
            g = 215
            b = 0

            af = 0
            bf = 0
            cf = 0

        if color == 2:
            colorPos = 2
            r = 0
            g = 229
            b = 229

            af = 220
            bf = 20
            cf = 60

        if color == 3:
            colorPos = 3
            r = 220 
            g = 20
            b = 20

            af = 20
            bf = 220
            cf = 77

        if defaultColor == True:
            colorPos = 4
            r = 35
            g = 220
            b = 35

            af = 230
            bf = 210
            cf = 20
            

    def go_down(self):
        global pos
        if pos >= 3:
            pos = 3
            return
        pos += 1

    def go_up(self):
        global pos
        if pos <= 1:
            pos = 1
            return
        pos -= 1


'/////////////////////////////////////////////////////////'

c = 3    
w = 600
h = 600
collide = bool
color = 0
start = 0
pos = 1
colorPos = 1
r = 0
g = 0
b = 0
firstTime = -1
defaultColor = True
cM = colorMenu(w, h)
m = Menu(w, h)
s = Snake(w, h)
f = Food(w, h)
#sprites = g2d.load_image("Ground.png")
#sprites2 = g2d.load_image("Ground2.png")

def size():
    return (w, h)

frameCount = 0.0
frameEasy = 2.0
frameHard = 1.0
    
def update():
    global c
    global frameCount

    if start == 1:
        m.draw()
    
    elif all ([start >= 2, pos == 2]):
        cM.draw()

    elif any ([start >= 2, defaultColor == False]):
        frameCount += 0.5

        if frameCount >= (frameEasy if pos == 1 else frameHard):
            frameCount = 0.0
        else:
            return

        #g2d.draw_image((sprites), (0, 0))
        if defaultColor == True:
            g2d.fill_canvas((159,73,7))
        elif color == 1:
            g2d.fill_canvas((200,90,90))
        elif color == 2:
            g2d.fill_canvas((188,143,143))
        elif color == 3:
            g2d.fill_canvas((31,117,169))

        s.biteSelf()
        s.move()
        f.draw()
        s.draw()
        s._points = str(s._points)
        c = str(c)
        g2d.draw_text(('Points: '), (255, 255, 255), (7, 5), (25))
        g2d.draw_text((s._points), (255, 255, 255), (75, 5), (25))
        f.relocate()

    else:
        g2d.fill_canvas((0, 0, 0))
        g2d.draw_text(('Welcome to Snake'), (240, 240, 240), (205, 38), (32))
        g2d.draw_text(('Use directional keys or WASD to control the snake and menu,'), (240, 240, 240), (13, 135), (29))
        g2d.draw_text(('start the game by pressing either Space or Enter'), (240, 240, 240), (68, 160), (29))
        g2d.draw_text(('Enjoy!'), (240, 240, 240), (264, 245), (30))


'///////////////////////////////////////////////////////////////////////'

def keydown(code):
    global start
    global pos
    global defaultColor
    global firstTime
    global color


    if any ([code == "Space", code == "Return"]):
        start += 1
        if start > 2:
            start = 2

    if all ([start >= 2, pos == 2]):
        firstTime += 1
        if any ([code == "ArrowUp", code == "KeyW"]):
            cM.go_up()
        elif any ([code == "ArrowDown", code == "KeyS"]):
            cM.go_down()

        if (code == "Space" or code == "Return") and firstTime == 0:
            code = ""
        
        elif any ([code == "Space", code == "Return"]):
            if colorPos == 4:
                defaultColor = True
                color = 0
            else:
                defaultColor = False

            if colorPos == 1:
                color = 1
            elif colorPos == 2:
                color = 2
            elif colorPos == 3:
                color = 3

            start = 1
            s.restart()
            firstTime = -1

        if code == ("Escape"):
            firstTime = -1
            s.restart()
            start = 1

    elif (start >= 2):
        if any ([code == "ArrowUp", code == "KeyW"]):
            s.go_up()
        elif any ([code == "ArrowLeft", code == "KeyA"]):
            s.go_left()
        elif any ([code == "ArrowRight", code == "KeyD"]):
            s.go_right()
        elif any ([code == "ArrowDown", code == "KeyS"]):
            s.go_down()
        if code == ("Escape"):
            s.restart()
            start = 1

    elif (start == 1):
        if any ([code == "ArrowUp", code == "KeyW"]):
            m.go_up()
        elif any ([code == "ArrowDown", code == "KeyS"]):
            m.go_down()
        if code == "Escape":
            sys.exit()
    cod = code
        
def keyup(code):
    return

def main():
    g2d.init_canvas(size())
    g2d.handle_keyboard(keydown, keyup)
    g2d.main_loop(update, 1000 // 60)

main()
