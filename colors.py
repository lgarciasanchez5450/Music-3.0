
class Color:
    def __init__(self,r:int = 0,g:int = 0,b:int = 0):
        self.r = r 
        self.g = g
        self.b = b
        if self.r > 255: self.r = 255
        elif self.r < 0: self.r = 0
        if self.g > 255: self.g = 255
        elif self.g < 0: self.g = 0
        if self.b > 255: self.b = 255
        elif self.b < 0: self.b = 0
        self.color = (self.r,self.g,self.b)
    
    def __add__(self,thing:int|object):
        if isinstance(thing,int):
            return Color(self.r+thing,self.g+thing,self.b+thing)
        elif isinstance(thing,Color):
            return Color(self.r+thing.r+self.g+thing.g,self.b+thing.b)
    def __mul__(self,thing:int):
        return Color(self.r*thing,self.g*thing,self.b*thing)

    def __str__(self):
        return self.color.__str__()

null = (0,0,0)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
light_red = (255,100,100)
light_green = (100,255,100)
light_blue = (100,100,255)
dark_grey = (40,40,40)
grey = (120,120,120)
light_grey = (210,210,210)
dark_red = (150,0,0)
dark_green = (0,150,0)
dark_blue = (0,0,150)
light_dark_grey = (70,70,70)
dark_light_grey = (180,180,180)
purple = (100,0,100)
royal_purple = (60,10,100)
theme_purple = (95,59,229)
theme_yellow = (248,196,0)
theme_light_yellow = (254,229,147)
theme_red_purple = (125,64,146)
theme_light_purple = (100,62,235)
theme_dark_purple = (80,50,150)
'''if __name__ == '__main__':
    from random import randint
    from time import perf_counter
    from numba import njit
    start = perf_counter()
    thingy = []
    for x in range(2000):
        thingy.append(x)
    for x in range(2000):
        thingy.append(x)
    end = perf_counter()
    a1 = end-start
    start = perf_counter()
    thingy = []
    for x in range(2000):
        thingy.append(x)
        thingy.append(x)
    end = perf_counter()    
    a2 = end-start
    if a1/a2 > 1:
        print(f'The second statement is {a1/a2} times faster than the first')
    else:
        print(f'The first statement is {a2/a1} times faster than the second')
'''









#nerf miner