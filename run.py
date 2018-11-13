import glob
import os
import random
import sys
from math import hypot


import pygame
from pygame.locals import *

# Image data path
IMG_DIR = os.path.join(os.path.abspath(__file__), "img")

# Color Consts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen size
SCREEN_HEIGHT = 600
SCREEN_WIDTH = int(SCREEN_HEIGHT * 1.77777)

# Setup pygame window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Current screen index
CURRENT_GAME_STATE = 1
NUM_GAME_SATES = 7

# "next" button consts
NEXT_BUTTON_CENTER = (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT- 65))
NEXT_BUTTON_RADIUS = 50

def distance(first,second):
    (x1,y1)=first
    (x2,y2)=second
    return hypot(x2-x1, y2-y1)

def _load_next_img():
    """ Load a random image from the image set at pos (0,0)
    """
    # Select a random image from the png files in the data folder
    global CURRENT_GAME_STATE
    CURRENT_GAME_STATE += 1
    if CURRENT_GAME_STATE > NUM_GAME_SATES:
        sys.exit(0)
    img = pygame.image.load(f'/Users/dumble/Desktop/pygame_test/imgs/{CURRENT_GAME_STATE}.jpg')
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


def _handle_click(click_pos):
    """ Handle a click event
    """
    _load_next_img()
    # # Check if there was a collision with the next buttonn
    # button_dist = distance(click_pos, NEXT_BUTTON_CENTER)
    # if button_dist <= NEXT_BUTTON_RADIUS:
    #     _load_next_img()


# def _draw_next_button(mouse_pos):
#     """ Draw the "next" button
#     """

#     # If the mouse is over the button change the color
#     mouse_dist = distance(mouse_pos, NEXT_BUTTON_CENTER)
#     if mouse_dist <= NEXT_BUTTON_RADIUS:
#         button_color = LIGHT_GREY
#     else:
#         button_color = GREY

#     # Draw button
#     pygame.draw.circle(DISPLAYSURF, button_color, NEXT_BUTTON_CENTER, NEXT_BUTTON_RADIUS)

#     # Draw text for button
#     button_font = pygame.font.Font(None, 36) # None can be a font file instead
#     button_text = button_font.render("NEXT", True, WHITE)
#     button_text_box = button_text.get_rect(centerx=NEXT_BUTTON_CENTER[0], centery=NEXT_BUTTON_CENTER[1])
#     DISPLAYSURF.blit(button_text, button_text_box)


def main():
    # Set caption
    pygame.display.set_caption('Game Demo!')

    # Set the first image
    img = pygame.image.load(f'/Users/dumble/Desktop/pygame_test/imgs/{CURRENT_GAME_STATE}.jpg')
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


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
                click_pos = pygame.mouse.get_pos()
                _handle_click(click_pos)

        # Get the mouse position
        # mouse_pos = pygame.mouse.get_pos()

        # Draw the button to click
        # _draw_next_button(mouse_pos)

        # Update the display based on current state after reading events
        pygame.display.update()


if __name__ == "__main__":
    main()

