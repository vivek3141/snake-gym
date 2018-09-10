# import the pygame module, so you can use it
import pygame
import time


# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo

    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    logo = pygame.image.load("01_image.png")
    bgd = pygame.image.load("background.png")
    logo.set_colorkey((255, 0, 255))
    screen = pygame.display.set_mode((200, 200))
    screen.blit(logo, (0, 0))
    pygame.display.flip()
    # define a variable to control the main loop
    running = True
    x = 0
    y = 0
    change = 10
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        if x > 136 or x < 0:
            change = -change
        screen.blit(bgd, (0, 0))
        screen.blit(logo, (x, 0))
        pygame.display.flip()
        x += change
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        time.sleep(0.5)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
