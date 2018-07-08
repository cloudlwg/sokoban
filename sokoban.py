 # -*- coding: utf-8 -*-

'''
"-" 空白处，可通过
"#" 墙,不可通过
"@" 人,可移动
"$" 箱子,可推动
"." 终点
"*" 到终点的箱子
'''

import pygame, sys, os,time
import threading
from pygame.locals import *

nextLevel = False
passLevel = 1
count =0
def win(level):
    """Judge the condition that win game"""
    global nextLevel,passLevel
    if  count %2 == 0 and level.count('$')==1:
        print('You win,next')
        passLevel +=1
        if passLevel == 9:
            gameOverSound()
            sys.exit()
        nextLevel = True


def to_box(level, index):
    global count
    if level[index] == '-' or level[index] == '@':
        level[index] = '$'
    else:
        level[index] = '*'
        if level[index] == '*':
            count +=1
        win(level)
        
def to_man(level, i):
    if level[i] == '-' or level[i] == '$':
        level[i]='@'
    else:
        level[i] = '+'
        
def to_floor(level, i):
    if level[i] == '@' or level[i] == '$':
        level[i]='-'
    else:
        level[i]='.'
        #pass

def to_offset(d, width):
    d4 = [-1, -width, 1, width,-1]
    m4 = ['l','u','r','d']
    if d in m4:
        return d4[m4.index(d.lower())]
    
def gameOver_Sound():
    file=r'D:\pygame_first\over.wav'
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def play_music():
    file=r'D:\pygame_first\gameMusic.mp3'
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    time.sleep(300)

def push_Sound():
    file=r'D:\pygame_first\pushSound.mp3'
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def win_Sound():
    file=r'D:\pygame_first\gameWin.mp3'
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
class Sokoban:
    
    def __init__(self,lv):
        self.levels(lv)
    def levels(self,index):
        if index == 1:
            self.level =      list('--###---'+\
                                   '--#.#---'+\
                                   '--#$####'+\
                                   '###@-$.#'+\
                                   '#.$--###'+\
                                   '####$#--'+\
                                   '---#.#--'+\
                                   '---###--')
            self.w = 8
            self.h = 8
            self.man = 27
        elif index == 2:
            self.level =      list('#####----'+\
                                   '#@--#----'+\
                                   '#-$$#-###'+\
                                   '#-$-#-#.#'+\
                                   '###-###.#'+\
                                   '-##----.#'+\
                                   '-#---#--#'+\
                                   '-#---####'+\
                                   '-#####---')
            
            self.w = 9
            self.h = 9
            self.man = 10
        elif index == 3:
            self.level =      list('-######-'+\
                                   '##--###-'+\
                                   '#@$-####'+\
                                   '##$-####'+\
                                   '##-$$.##'+\
                                   '#.$--###'+\
                                   '#..-.##-'+\
                                   '#######-')
            self.w = 8
            self.h = 8
            self.man = 17
        elif index == 4:
             self.level =     list('-#######--'+\
                                   '-#-----###'+\
                                   '##$###---#'+\
                                   '#-@-$--$-#'+\
                                   '#-..#-$-##'+\
                                   '##..#---#-'+\
                                   '-#--#####-'+\
                                   '-########-')
             self.w = 10
             self.h = 8
             self.man = 32
        elif index == 5:
             self.level =     list('-####---'+\
                                   '-#@-###-'+\
                                   '-#-$--#-'+\
                                   '###-#-##'+\
                                   '#.#-#--#'+\
                                   '#.$--#-#'+\
                                   '#.---$-#'+\
                                   '########')
             self.w = 8
             self.h = 8
             self.man = 10
        elif index == 6:
             self.level =     list('---#######---'+\
                                   '####-----#---'+\
                                   '#---.###-#---'+\
                                   '#-#-#----##--'+\
                                   '#-#-$-$#..#--'+\
                                   '#-#--*--#$#--'+\
                                   '#-.#$-$-#-#--'+\
                                   '##----#-#-###'+\
                                   '-#-###.----@#'+\
                                   '-#-----##---#'+\
                                   '-############')
             self.w = 13
             self.h = 11
             self.man = 115
        elif index == 7:
             self.level =     list('--########'+\
                                   '--#---#-@#'+\
                                   '--#-$-#--#'+\
                                   '--#$-$-$-#'+\
                                   '--#-$##--#'+\
                                   '###-$.#-##'+\
                                   '#.....--#-'+\
                                   '#########-')
             self.w = 10
             self.h = 8
             self.man = 18
        elif index == 8:
             self.level =     list('---######-'+\
                                   '-###----#-'+\
                                   '##.-$##-##'+\
                                   '#..$-$--@#'+\
                                   '#..-$-$-##'+\
                                   '######--#-'+\
                                   '-----####-')
             self.w = 10
             self.h = 7
             self.man = 38
    def draw(self, screen, skin):
        w = skin.get_width() / 4
        for i in range(0,self.w):
            for j in range(0,self.h):
                if self.level[j*self.w + i] == '#':
                    screen.blit(skin, (i*w, j*w), (0,2*w,w,w))
                elif self.level[j*self.w + i] == '-':
                    screen.blit(skin, (i*w, j*w), (0,0,w,w))
                elif self.level[j*self.w + i] == '@':
                    screen.blit(skin, (i*w, j*w), (w,0,w,w))
                elif self.level[j*self.w + i] == '$':
                    screen.blit(skin, (i*w, j*w), (2*w,0,w,w))
                elif self.level[j*self.w + i] == '.':
                    screen.blit(skin, (i*w, j*w), (0,w,w,w))
                elif self.level[j*self.w + i] == '+':
                    screen.blit(skin, (i*w, j*w), (w,w,w,w))
                elif self.level[j*self.w + i] == '*':
                    screen.blit(skin, (i*w, j*w), (2*w,w,w,w))
    def move(self, d):
        self._move(d)
    def _move(self, d):
        h = to_offset(d, self.w)
        h2 = 2 * h
        if self.level[self.man + h] == '-' or self.level[self.man + h] == '.':
        # move
            to_man(self.level, self.man+h)
            to_floor(self.level, self.man)
            self.man += h
        elif self.level[self.man + h] == '*' or self.level[self.man + h] == '$':
            if self.level[self.man + h2] == '-' or self.level[self.man + h2] == '.':
            # push
                to_box(self.level, self.man + h2)
                to_man(self.level, self.man + h)
                to_floor(self.level, self.man)
                self.man += h


class myGameThread(threading.Thread):
    def __init__(self,name=None):
        threading.Thread.__init__(self,name=None)
    def run(self):
        global nextLevel,passLevel
        # start pygame
        pygame.init()
        screen = pygame.display.set_mode((400,300))


        # load skin
        skinfilename = os.path.join('borgar.png')
        try:
            skin = pygame.image.load(skinfilename)
        except pygame.error as msg:
            print ('cannot load skin')
        skin = skin.convert()
        screen.fill(skin.get_at((0,0)))
        pygame.display.set_caption('sokoban.py')

        # create Sokoban object
        skb = Sokoban(1)
        skb.draw(screen,skin)
        clock = pygame.time.Clock()
        #按住某个键每隔interval(50)毫秒产生一个KEYDOWN事件，delay(200)就是多少毫秒后才开始触发这个事件。
        pygame.key.set_repeat(200,50)
        # main game loop
        def operation():
            clock.tick(60)#给tick方法加上的参数就成为了游戏绘制的最大帧率        
            for event in pygame.event.get():
                if event.type == QUIT:
                    #print skb.solution
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        skb.move('l')
                        pushSound()
                        skb.draw(screen,skin)
                    elif event.key == K_UP:
                        skb.move('u')
                        pushSound()
                        skb.draw(screen,skin)
                    elif event.key == K_RIGHT:
                        skb.move('r')
                        pushSound()
                        skb.draw(screen,skin)
                    elif event.key == K_DOWN:
                        skb.move('d')
                        pushSound()
                        skb.draw(screen,skin)
                    elif event.key == K_s:
                        pygame.mixer.music.stop()
                    elif event.key == K_r:
                        print("Game Over!failed")
                        pygame.mixer.music.stop()
                        sys.exit()
        
        while True:
            operation()
            if nextLevel:
                winSound()
                time.sleep(0.3)
                skb = Sokoban(passLevel)
                nextLevel = False
            pygame.display.update()
        

class playMusicThread(threading.Thread):
    def __init__(self,name=None):
        threading.Thread.__init__(self,name=None)
    def run(self):
        play_music()
class pushSoundThread(threading.Thread):
    def __init__(self,name=None):
        threading.Thread.__init__(self,name=None)
    def run(self):
        push_Sound()

class winSoundThread(threading.Thread):
    def __init__(self,name=None):
        threading.Thread.__init__(self,name=None)
    def run(self):
        win_Sound()

class gameOverSoundThread(threading.Thread):
    def __init__(self,name=None):
        threading.Thread.__init__(self,name=None)
    def run(self):
        gameOver_Sound()
        
def openThread():
    p = myGameThread()
    #m = playMusicThread()
    p.start()
    #m.start()
    p.join()
    #m.join()
    
def pushSound():
    """推箱子音效"""
    s = pushSoundThread()
    s.start()
    s.join()

def winSound():
    """游戏胜利音效"""
    w = winSoundThread()
    w.start()
    w.join()

def gameOverSound():
    """游戏结束音效"""
    o=gameOverSoundThread()
    o.start()
    o.join()

          
def main():
    openThread()
    
if __name__ == '__main__':
    main()
    
