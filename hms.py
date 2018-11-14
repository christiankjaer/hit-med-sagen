# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
import pygame
import sys
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

 
# Define some colors
BLACK    = (   0,   0,   0)
GREY     = ( 127, 127, 127)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 100,  0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)


questions = []

f = codecs.open(sys.argv[1], 'r', 'utf-8')

chop = FirefoxProfile()
chop.add_extension('ublock.xpi')

dr = webdriver.Firefox(firefox_profile = chop)

for line in f:
    q = []
    b = []
    both = line.split(" //")
    for i, w in enumerate(both[0].split()):
        if w[-1] == '!':
            b.append(i)
            q.append(w[0:-1])
        else:
            q.append(w)

    questions.append((q,b, both[1]))

def draw_question(screen, counter, toggled, won=False):
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    font = pygame.font.Font(None, 36)
    text = font.render(str(counter+1), 1, WHITE)
    textpos = text.get_rect()
    screen.blit(text, textpos)
    choices, dongs, url = questions[counter]
    n = len(choices)
    b_width = size[0] / n
    if len(toggled) > 0 and toggled[-1] in dongs:
        fall.play()
    elif not won:
        ping.play()
    if won:
        dr.get(url)

    for i, q in enumerate(choices):
        if won or i in toggled:
            font = pygame.font.Font(None, 120)
            text = font.render(q, 1, WHITE)
        else:
            font = pygame.font.Font(None, 480)
            text = font.render(str(i+1), 1, WHITE)
        rect = pygame.Rect(i*b_width+10, 0, b_width-20, size[1]/4)
        rect.centery = size[1] / 2
        if won:
            pygame.draw.rect(screen, GREEN, rect)
        elif i in dongs and i in toggled:
            pygame.draw.rect(screen, RED, rect)
        else:
            pygame.draw.rect(screen, BLUE, rect)
        textpos = text.get_rect()
        textpos.centerx = rect.centerx
        textpos.centery = rect.centery
        screen.blit(text, textpos)


# Setup
pygame.init()
pygame.mixer.init()
  
# Set the width and height of the screen [width,height]
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
 
pygame.display.set_caption("Hit med sangen")
 
#Loop until the user clicks the close button.
done = False
redraw = True
won = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

fall = pygame.mixer.Sound("fail.wav")
fall.set_volume(0.5)
ping = pygame.mixer.Sound("ping.wav")
ping.set_volume(0.5)

toggled = []
counter = 0
screen.fill(GREY)
draw_question(screen, counter, toggled)
pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            # User pressed down on a key
        
        elif event.type == pygame.KEYDOWN:
            redraw = True
            won = False
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_1:
                toggled.append(0)
            elif event.key == pygame.K_2:
                toggled.append(1)
            elif event.key == pygame.K_3:
                toggled.append(2)
            elif event.key == pygame.K_4:
                toggled.append(3)
            elif event.key == pygame.K_5:
                toggled.append(4)
            elif event.key == pygame.K_6:
                toggled.append(5)
            elif event.key == pygame.K_7:
                toggled.append(6)
            elif event.key == pygame.K_8:
                toggled.append(7)
            elif event.key == pygame.K_SPACE:
                won = True

            elif event.key == pygame.K_PAGEDOWN:
                toggled = []
                if counter < len(questions)-1:
                    counter += 1
                    dr.find_element_by_tag_name("body").send_keys('k')
            elif event.key == pygame.K_PAGEUP:
                toggled = []
                if counter > 0:
                    counter -= 1
                dr.find_element_by_tag_name("body").send_keys('k')
            else:
                redraw = False
            if redraw:
                screen.fill(GREY)
                draw_question(screen, counter, toggled, won=won)
                pygame.display.flip()
                 

    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
