#  module imports
import pygame
#  file imports
import desktop.communicator as hch

#  checks for fonts and sounds, can be removed
if not pygame.font: print("Warning, fonts disabled")
if not pygame.mixer: print("Warning, sound disabled")

#  initializes all necessary modules
pygame.init()

'''
#  display testing stuff, remove?
userdisplaydefaults = pygame.display.Info()
print(userdisplaydefaults)
'''

#  makes the window
size = [1000, 1000]
screen = pygame.display.set_mode(size)

#  sets window name
pygame.display.set_caption("Pixel Grid Capture")

#  intro text
font = pygame.font.Font(None, 50)
text = ["Welcome to Pixel Grid Capture! The goal of this game is",
        "simple: cover the grid! You click pixels as quickly as you",
        "can, working with your team, composed of those of the",
        "same color family as you. Your username is your hex code.",
        "If you already have one, simply enter it below. If not,",
        "click a color family to receive one and start playing."]
space = 0
for line in text:
    temp = font.render(line, True,(255, 255, 255))
    screen.blit(temp, (10, 10 + space * 50))
    space += 1

#  hex code box
hexcodeinput = ""
hexcodebox = pygame.Rect(375, 375, 250, 50)
pygame.draw.rect(screen, (100, 100, 100), hexcodebox, 0)

#  color boxes
instruct2 = "Click on a color to recieve your hex code"
instruct2render = font.render(instruct2, True, (255, 255, 255))
screen.blit(instruct2render, (150, 550))

#  cap note
instruct3 = "Note: clicks are capped at one per 1/10 second"
instruct3render = font.render(instruct3, True, (255, 255, 255))
screen.blit(instruct3render, (50, 950))

#  red
redbox = pygame.Rect(50, 650, 100, 100)
pygame.draw.rect(screen, (150, 5, 25), redbox, 0)

#  orange
orangebox = pygame.Rect(300, 650, 100, 100)
pygame.draw.rect(screen, (255, 102, 0), orangebox, 0)

#  yellow
yellowbox = pygame.Rect(550, 650, 100, 100)
pygame.draw.rect(screen, (255, 255, 0), yellowbox, 0)

#  green
greenbox = pygame.Rect(800, 650, 100, 100)
pygame.draw.rect(screen, (0, 102, 0), greenbox, 0)

#  blue, my favorite color
bluebox = pygame.Rect(200, 800, 100, 100)
pygame.draw.rect(screen, (0, 0, 153), bluebox, 0)

#  purple
purplebox = pygame.Rect(450, 800, 100, 100)
pygame.draw.rect(screen, (102, 0, 204), purplebox, 0)

#  monochrome
monobox = pygame.Rect(700, 800, 100, 100)
pygame.draw.rect(screen, (255, 255, 255), monobox, 0)

#  render it all
pygame.display.flip()

#  state variables
done = False
mainmenu = True
hexcodeboxactive = False
hexcode = ""
colorfamily = ""
straighttogameplay = True
gridofboxes = []
change = False
xy = (0, 0)

#  main menu loop
while not done and mainmenu:

    #  input handling
    for event in pygame.event.get():

        #  close on close
        if event.type == pygame.QUIT:
            done = True

        #  if click
        if event.type == pygame.MOUSEBUTTONDOWN:

            #  if click hexcodebox
            if hexcodebox.collidepoint(event.pos):
                hexcodeboxactive = True

            #  if click red
            if redbox.collidepoint(event.pos):
                colorfamily = "red"
                mainmenu = False

            #  if click orange
            if orangebox.collidepoint(event.pos):
                colorfamily = "orange"
                mainmenu = False

            #  if click yellow
            if yellowbox.collidepoint(event.pos):
                colorfamily = "yellow"
                mainmenu = False

            #  if click green
            if greenbox.collidepoint(event.pos):
                colorfamily = "green"
                mainmenu = False

            #  if click blue
            if bluebox.collidepoint(event.pos):
                colorfamily = "blue"
                mainmenu = False

            #  if click purple
            if purplebox.collidepoint(event.pos):
                colorfamily = "purple"
                mainmenu = False

            #  if click mono
            if monobox.collidepoint(event.pos):
                colorfamily = "monochrome"
                mainmenu = False

            #  if click off hexcodebox
            elif not hexcodebox.collidepoint(event.pos):
                hexcodeboxactive = False

        #  if hit a key on keyboard
        if event.type == pygame.KEYDOWN:

            #  if in hexcodebox
            if hexcodeboxactive:

                #  if hit enter
                if event.key == pygame.K_RETURN:

                    #  send hexcode to checker
                    result = hch.checkenteredcode(hexcodeinput)

                    #  if not existing hex code
                    if result == "none":

                        #  display error message
                        error = "Hex code not found."
                        errortext = font.render(error, True, (255, 255, 255))
                        screen.blit(errortext, (350, 450))
                        error = "Please try again."
                        errortext = font.render(error, True, (255, 255, 255))
                        screen.blit(errortext, (350, 500))

                    #  if hex code found
                    else:
                        hexcode = hexcodeinput
                        colorfamily = result
                        mainmenu = False

                #  if hit delete
                elif event.key == pygame.K_BACKSPACE:
                    hexcodeinput = hexcodeinput[:-1]

                #  if hit whatever
                else:
                    hexcodeinput += event.unicode

            #  display as typed
            hexcodetext = font.render(hexcodeinput, True, (255, 255, 255))
            pygame.draw.rect(screen, (100, 100, 100), hexcodebox, 0)
            screen.blit(hexcodetext, (hexcodebox.x + 10, hexcodebox.y + 10))
            pygame.display.flip()

    #  end main menu loop


#  clear screen
screen.fill((255, 255, 255))

#  assigns stuff to new player
if hexcode == "" and not done:

    #  generate the hex code
    hexcode = hch.giveusernewcode(colorfamily)
    straighttogameplay = False

    #  hex code text
    text = ["Congrats, your new hex code is:",
            hexcode,
            "Please save this for future reference.",
            "Click anywhere to continue."]
    space = 0
    for line in text:
        temp = font.render(line, True, pygame.Color(hexcode))
        screen.blit(temp, (200, 350 + space * 50))
        space += 1
    pygame.display.flip()

#  mini loop
while not done and not straighttogameplay:

    #  input handling
    for event in pygame.event.get():

        #  close on close
        if event.type == pygame.QUIT:
            done = True

        #  if click anywhere
        if event.type == pygame.MOUSEBUTTONDOWN:
            straighttogameplay = True
    #  end mini loop

#  clear screen
screen.fill((255, 255, 255))

#  display pixel grid
arrayofhexs = hch.watchoutforthatgridonthefloor()
gridx = 0
gridy = 0
for row in arrayofhexs:
    for element in row:
        box = pygame.Rect(gridx * 20, gridy * 20, 20, 20)
        pygame.draw.rect(screen, pygame.Color(element), box, 0)
        gridx += 1
        gridofboxes.append(box)
    gridx = 0
    gridy += 1
pygame.display.flip()

#  gameplay loop
while not done:

    #  limit updates
    pygame.time.Clock().tick(100)

    #  input handling
    for event in pygame.event.get():

        #  close on close
        if event.type == pygame.QUIT:
            done = True

        #  if click
        if event.type == pygame.MOUSEBUTTONDOWN:

            #  for each pixel
            for box in gridofboxes:
                if box.collidepoint(event.pos):
                    xy = event.pos
                    change = True

    #  to prevent fatal glitch
    if change:
        hch.editgrid(hexcode, xy)
        change = False

    #  display loop
    screen.fill((255, 255, 255))
    arrayofhexs = hch.watchoutforthatgridonthefloor()
    gridx = 0
    gridy = 0
    for row in arrayofhexs:
        for element in row:
            box = pygame.Rect(gridx * 20, gridy * 20, 20, 20)
            pygame.draw.rect(screen, pygame.Color(element), box, 0)
            gridx += 1
            gridofboxes.append(box)
        gridx = 0
        gridy += 1
    pygame.display.flip()

    #  end of gameplay loop

#  just leave alone
pygame.quit()
