#!/usr/bin/env python

# Import the pygame module, along with some default python modules
import pygame, sys, time, random

# When you import a non-python default module, you will need to call it.  Below we call all pygame instructions for ease of use.  As well as the ktext instructions
from pygame.locals import *
from ktextsurfacewriter import KTextSurfaceWriter

# Initialise pygame
pygame.init()

# Create a clock for controlling the game speed
fpsClock = pygame.time.Clock()

# Set related surface variables
surfaceDimensions = (800, 600)
gridSquareSize = 20

# Create a display surface (aka canvas) to be used as the primary surface
playSurface = pygame.display.set_mode(surfaceDimensions)
pygame.display.set_caption('Raspberry Snake')

# Define some colors
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)

# Define some static game variable defaults
snakePositionDefault = (100,100)
snakeSegmentsDefault = ((100,100),(80,100),(60,100))
raspberryPositionDefault = (300,300)

# Define fonts/styles
fontTitle = pygame.font.Font('freesansbold.ttf', 72)
fontMenu = pygame.font.Font('freesansbold.ttf', 42)
fontParagraph = pygame.font.Font('freesansbold.ttf', 12)

# Other default values
selectedItem = 0 #For the menu

# Configure re-useable raspberry image
raspberryImage = pygame.image.load("raspi_icon.png")    
raspberryImage = pygame.transform.scale(raspberryImage,(gridSquareSize,gridSquareSize))
raspberryImage = raspberryImage.convert()
raspberryImageRect = raspberryImage.get_rect()



# Annoyed with the laborious nature of inserting rows of text, so creating a function to handle this for me
def configureText(textRows, textStyle, withTitle):
    newLineTop = 0
    i = 0
    for row in textRows:
        if gameStatus == "Menu":
            if i == selectedItem:
              rowText = textStyle.render(row, True, redColour)
            else:
              rowText = textStyle.render(row, True, greyColour)
        elif gameStatus != "Menu":
            if withTitle == 1 and i == 0:
                rowText = fontTitle.render(row, True, greyColour)
            else:
                rowText = textStyle.render(row, True, greyColour)
                
        rowRect = rowText.get_rect()
        rowRect.midtop = (320, newLineTop)        
        playSurface.blit(rowText, rowRect)
        newLineTop = rowRect[3] + newLineTop
        i+=1



# An improved version of configure text to use ktext instead as auto wraps long lines (https://pypi.python.org/pypi/KTextSurfaceWriter/)
def configureText2(textRows, textStyle, withTitle):


    # ktext will only print one text area, and so the title must be rendered seperately
    rowText = fontTitle.render(textRows[0], True, whiteColour)
    rowRect = rowText.get_rect()
    rowRect.midtop = (320, 10)        
    playSurface.blit(rowText, rowRect)
        
    # Print the copy
    if withTitle==1:
        text_rect = pygame.Rect( (10, 100),(600,200) )
    else:
        text_rect = pygame.Rect( (10, 10),(600,200) )
    ktext = KTextSurfaceWriter(text_rect)
    ktext.color = whiteColour
    ktext.font = fontParagraph
    ktext.fillcolor = blackColour
    ktext.text = textRows[1]
    ktext.draw(playSurface)
    
    

# Display the menu screen
def displayMenu():
    global gameStatus
    gameStatus = 'Menu'
    # Clear the surface
    setupCircuitboard()
    snakeMenu = ('[S]tart','[H]elp', '[Q]uit')
    configureText(snakeMenu, fontMenu, 0)
    redrawSurface()



# Function to run when a menu item is selected
def menuSelect():
    if gameStatus == "Menu":
        if selectedItem==0:
            resetGame();
        elif selectedItem==1:
            displayHelp();
        elif selectedItem==2:
            pygame.event.post(pygame.event.Event(QUIT))



# Display the help screen
def displayHelp():
    global gameStatus
    gameStatus = 'Help'
    # Clear the surface
    playSurface.fill(blackColour)
    snakeHelp = ('Help','This is a simple game of snake.  The writing of this had just one purpose, and that was to help me learn Python.  The initial code for this was taken from the Raspberry Pi User Guide.  This was then evolved by me to add new functionality and ensure I understood some of the underlying differences between this and PHP (which I am more used to).  To play this game simply use the arrow keys (or number pad) to move the snake and collect raspberries.  Avoid hitting yourself or the walls')
    configureText2(snakeHelp, fontParagraph, 1)
    redrawSurface()



# Create reuseable 'gameOver' function
def gameOver():
    global gameStatus
    
    # Clear the surface
    playSurface.fill(blackColour)

    fpsClock.tick(0)
    
    gameStatus = 'Game Over'

    # Create text variable
    gameOverTitle = 'Game Over'
    gameOverCopy1 = 'Press S to start again, or Q to quit'
    gameOverCopy2 = 'Reaper report: {0}'.format(reaperReport)

    gameOverText = (gameOverTitle, gameOverCopy1, gameOverCopy2)
    configureText(gameOverText, fontParagraph, 1)
    
    redrawSurface()

    

# Create reuseable 'resetGame' function
def resetGame():
    global snakePosition
    global snakeSegments
    global raspberryPosition
    global raspberrySpawned
    global gameStatus
    global direction
    global changeDirection
    global reaperReport
    reaperReport = ''
    snakePosition = list(snakePositionDefault)
    snakeSegments = list(snakeSegmentsDefault)
    raspberryPosition = list(raspberryPositionDefault)
    raspberrySpawned = 1 # (BOOLEAN) Has the raspberry been spawned onto the display surface
    direction = 'right'
    changeDirection = direction    
    gameStatus = 'Playing'
    redrawSurface()



# Redraw the surface (in a function as is often called, so easy to manage in this one place
def redrawSurface():
    if gameStatus == 'Game Over' or gameStatus == 'Menu' or gameStatus == 'Help':
        # Draw the shapes we set above
        pygame.display.flip()
    elif gameStatus == 'Playing':
        # Clear the surface
        setupCircuitboard()

        # Set snake and raspberry positions and colors
        for position in snakeSegments:
            pygame.draw.rect(playSurface,whiteColour,Rect(position[0], position[1], gridSquareSize, gridSquareSize))
            pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1], gridSquareSize, gridSquareSize))
            raspberryImageRect.top = raspberryPosition[1]
            raspberryImageRect.left = raspberryPosition[0]            
            playSurface.blit(raspberryImage, raspberryImageRect)

        # Draw the shapes we set above
        pygame.display.flip()



# When screen is cleared, setup the circuitboard background first to be used
def setupCircuitboard():
    playSurface.fill(blackColour)
    circuitboard_tile = pygame.image.load('tile_circuitboard_100x100.png')
    tileDimensions = (200,200)
    
    x = 0
    
    while x<surfaceDimensions[0]:
        y = 0
        while y<surfaceDimensions[1]:
            playSurface.blit(circuitboard_tile, (x, y))
            y+=tileDimensions[1]
        x+=tileDimensions[0]



# Display menu on application load
displayMenu()



# THE GAME
while True:

    # Setup event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == ord('s'):
                if gameStatus != 'Playing':
                    resetGame();
            elif event.key == ord('m'):
                if gameStatus != 'Playing':
                    displayMenu();
            elif event.key == ord('q') or event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == ord('h'):
                if gameStatus != 'Playing':
                    displayHelp();
            elif event.key == K_RETURN:
                menuSelect()
            elif event.key == K_UP or event.key == ord('5'):
                if gameStatus == 'Menu' and selectedItem!=0:
                    selectedItem -= 1
                    displayMenu()
                changeDirection = 'up'
            elif event.key == K_DOWN or event.key == ord('2'):
                if gameStatus == 'Menu' and selectedItem!=2:
                    selectedItem += 1
                    displayMenu()
                changeDirection = 'down'
            elif event.key == K_RIGHT or event.key == ord('3'):
                if gameStatus == 'Playing':
                    changeDirection = 'right'
            elif event.key == K_LEFT or event.key == ord('1'):
                if gameStatus == 'Playing':
                    changeDirection = 'left'


    # Setup ingame logic
    if gameStatus == 'Playing':          

        # Once changeDirection is set, we need to check it is valid, then amend snakes direction accordingly
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        # Move the snake
        if direction == 'right':
            snakePosition[0] += gridSquareSize
        if direction == 'left':
            snakePosition[0] -= gridSquareSize
        if direction == 'up':
            snakePosition[1] -= gridSquareSize
        if direction == 'down':
            snakePosition[1] += gridSquareSize

        # Increase the snake length by adding the new position
        snakeSegments.insert(0,list(snakePosition))

        # If snakes head is same segment as raspberry, then set spawn, and don't decrease snake length
        if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
            raspberrySpawned = 0
        # Otherwise, decrease snake length by one to simulate movement
        else:
            snakeSegments.pop() #pop returns and removes from the bottom of the list

        # Respawn raspberrys
        if raspberrySpawned == 0:
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            raspberryPosition = [int(x*gridSquareSize),int(y*gridSquareSize)]
            raspberrySpawned = 1

        redrawSurface()

        # The many ways to kill a snake
        if snakePosition[0] > 780 or snakePosition[0] < 0:
            reaperReport = 'Hit horizontal walls'
            gameOver()
        if snakePosition[1] > 580 or snakePosition[1] < 0:
            reaperReport = 'Hit vertical walls'
            gameOver()
        # Loop through all snakeSegments (except for the head) and see if the head has hit them
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                reaperReport = 'Hit self'
                gameOver()

        # Set game speed
        fpsClock.tick(20)
