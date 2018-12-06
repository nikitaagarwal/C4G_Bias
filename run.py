import glob
import os
import random
import sys
from math import hypot


import pygame
from pygame.locals import *
# from pygame import display,movie

# Image data path
IMG_DIR = os.path.join(os.path.abspath(__file__), "img")

# Color Consts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen size
SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1333

# Setup pygame window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Current screen index
CURRENT_GAME_STATE = "00.png" # OG start screen
NUM_GAME_SATES = 7

captain_1 = False
captain_2 = False
captain_3 = False
captain_4 = False
firstLieut_1 = False
firstLieut_2 = False
firstLieut_3 = False
firstLieut_4 = False
secondLieut_1 = False
secondLieut_2 = False
secondLieut_3 = False
secondLieut_4 = False
doctor_1 = False
doctor_2 = False
doctor_3 = False
doctor_4 = False
engineer_1 = False
engineer_2 = False
engineer_3 = False
engineer_4 = False
placeholderfor6_1 = False
placeholderfor6_2 = False
placeholderfor6_3 = False
placeholderfor6_4 = False
placeholderfor7_1 = False
placeholderfor7_2 = False
placeholderfor7_3 = False
placeholderfor7_4 = False


PATH = os.getcwd()


def distance(first,second):
    (x1,y1)=first
    (x2,y2)=second
    return hypot(x2-x1, y2-y1)

# def _load_next_img():
#     """ Load a random image from the image set at pos (0,0)
#     """
#     # Select a random image from the png files in the data folder
#     global CURRENT_GAME_STATE
#     CURRENT_GAME_STATE += 1
#     if CURRENT_GAME_STATE > NUM_GAME_SATES:
#         sys.exit(0)
#     img = pygame.image.load(os.path.join(PATH,'imgs',str(CURRENT_GAME_STATE)+".png"))
#     DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


StartRect = Rect(457,589,400,200)
OPTION1 = Rect(422,331,100,70)
OPTION2 = Rect(659,331,100,70)
OPTION3 = Rect(886,331,100,70)
OPTION4 = Rect(1122,331,100,70)

def update_screen_and_state(new_state):
    global CURRENT_GAME_STATE
    img = pygame.image.load(os.path.join(PATH,'imgs',new_state))
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    CURRENT_GAME_STATE = new_state
    pygame.display.update()

def _handle_click(click_pos):
    global CURRENT_GAME_STATE

    """ Handle a click event
    """
    # START SCREEN: HIT PLAY!
    if CURRENT_GAME_STATE == "00.png":
        if StartRect.collidepoint(click_pos):
            update_screen_and_state("01.png")
    # CAPTAIN SCREEN
    elif CURRENT_GAME_STATE == "01.png":
        print ("in here\n")
        if OPTION1.collidepoint(click_pos):
            captain_1 = True
        elif OPTION2.collidepoint(click_pos):
            captain_2 = True
        elif OPTION3.collidepoint(click_pos):
            captain_3 = True
        else:
            captain_4 = True
        update_screen_and_state("02.png")
    elif CURRENT_GAME_STATE == "02.png":
        if OPTION1.collidepoint(click_pos):
            firstLieut_1 = True
        elif OPTION2.collidepoint(click_pos):
            firstLieut_2 = True
        elif OPTION3.collidepoint(click_pos):
            firstLieut_3 = True
        else:
            firstLieut_4 = True
        update_screen_and_state("03.png")
    elif CURRENT_GAME_STATE == "03.png":
        if OPTION1.collidepoint(click_pos):
            secondLieut_1 = True
        elif OPTION2.collidepoint(click_pos):
            secondLieut_2 = True
        elif OPTION3.collidepoint(click_pos):
            secondLieut_3 = True
        else:
            secondLieut_4 = True
        update_screen_and_state("04.png")
    elif CURRENT_GAME_STATE == "04.png":
        if OPTION1.collidepoint(click_pos):
            doctor_1 = True
        elif OPTION2.collidepoint(click_pos):
            doctor_2 = True
        elif OPTION3.collidepoint(click_pos):
            doctor_3 = True
        else:
            doctor_4 = True
        update_screen_and_state("05.png")
    elif CURRENT_GAME_STATE == "05.png":
        if OPTION1.collidepoint(click_pos):
            engineer_1 = True
        elif OPTION2.collidepoint(click_pos):
            engineer_2 = True
        elif OPTION3.collidepoint(click_pos):
            engineer_3 = True
        else:
            engineer_4 = True
        update_screen_and_state("05.png") # PLACE HOLDER! (CHANGE TO 06.PNG)
    elif CURRENT_GAME_STATE == "05.png": # PLACE HOLDER CHANGE TO 06
        if OPTION1.collidepoint(click_pos):
            placeholderfor6_1 = True
        elif OPTION2.collidepoint(click_pos):
            placeholderfor6_2 = True
        elif OPTION3.collidepoint(click_pos):
            placeholderfor6_3 = True
        else:
            placeholderfor6_4 = True
        update_screen_and_state("05.png") # PLACE HOLDER! CHANGE TO 07
    else: # PLACE HOLDER CHANGE TO 07
        if OPTION1.collidepoint(click_pos):
            placeholderfor7_1 = True
        elif OPTION2.collidepoint(click_pos):
            placeholderfor7_2 = True
        elif OPTION3.collidepoint(click_pos):
            placeholderfor7_3 = True
        else:
            placeholderfor7_4 = True
        update_screen_and_state("05.png") # PLACE HOLDER! CHANGE TO END?


    # _load_next_img()
    # # Check if there was a collision with the next buttonn
    
    
    #     _load_next_img()




def main():
    # Set caption
    pygame.display.set_caption('Game Demo!')

    # Set the first image
    clock = pygame.time.Clock()
    # movie = pygame.movie.Movie(os.path.join(PATH,'imgs','m1.mp4'))
    # movie_screen = pygame.Surface(movie.get_size()).convert()

    FPS = 30

    img = pygame.image.load(os.path.join(PATH,'imgs',"00.png"))
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


    # img = pygame.image.load(os.path.join(PATH,'imgs',str(CURRENT_GAME_STATE)+".png"))
    # DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    # global CURRENT_GAME_STATE
    CURRENT_GAME_STATE = "00.png"
    # Main event loop
    while True:
        # Check for new events
        for event in pygame.event.get():

            # Recv quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Recv click event
            if event.type == pygame.MOUSEBUTTONUP:
                # print ("kfajs;ldfja\n")
                # _load_next_img
                click_pos = pygame.mouse.get_pos()
                # print (str(click_pos) + "\n")
                _handle_click(click_pos)

        # Get the mouse position
        # mouse_pos = pygame.mouse.get_pos()

        # Draw the button to click
        # _draw_next_button(mouse_pos)

        # DISPLAYSURF.blit(movie_screen, 0, 0)
        clock.tick(FPS)

        # Update the display based on current state after reading events
        pygame.display.update()


if __name__ == "__main__":
    main()
