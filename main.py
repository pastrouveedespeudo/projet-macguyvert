#-*- coding: utf-8 -*-

"""
This a litle labyrinth. we can embody macgyver,
which aims to retrieve different objectsin order to get out of the labyrinth.
For that we will be able to control it thanks to the arrows of the keyboard:
low, high, right, left.
Here the main page. It will import the different files needed to launch the maze.
It is the interconnection of the different modules in order,
to launch the program.
"""

import random                 #Importing random module.
from pygame.locals import *   #Importing pygame modules.

from labyrinth_class import * #Importing labyrinth class.
from movement_class import *  #Importing movement class
from game_class import *      #Importing game class.
from object_class import *
from constant import * #Importing constant file.
COUNTER = []  
class Play:
    
                  
    def main(self):

        
        
        """ Interconexion about import class"""
        pygame.init() #Initialization of pygame.


        #Creation of the window, side_window is import from constant.py.
        win = pygame.display.set_mode((SIDE_WINDOW,
                                       SIDE_WINDOW_MESSAGE))

        #Image overlay for the wallpaper, picture's imported from constant.py.
        fond_fenetre = pygame.image.load(BACKGOUND_PICTURE).convert()
        fond_fenetre2 = pygame.image.load(BACKGOUND_PICTURE).convert()
        fond_inventory = pygame.image.load(EXTRA_PICTURE)
        fond_message = pygame.image.load(EXTRA_PICTURE)

        laby = Labyrinth("labyrinth.txt") #Generating a file.

        laby.generate() #Combined file with a grid for futurs movements.

        movement_mac = Movement("labyrinth.txt")
        movement_mac.position(HERO_PICTURE) #Definition of positions variables.
        movement_mac.importation_file()     #We generate file for movement from movement_class.

        game = Game("labyrinth.txt")
        game.importation_file(HERO_PICTURE)
        #We importing Movement_class and Labrynth_class into Game_class.

        ether = Object("labyrinth.txt")
        ether.importation_file(HERO_PICTURE)
        tube = Object("labyrinth.txt")
        tube.importation_file(HERO_PICTURE)
        needle = Object("labyrinth.txt")
        needle.importation_file(HERO_PICTURE)
        
        ether.random_object(ETHER_PICTURE, "ether")
        tube.random_object(TUBE_PICTURE, "tube")
        needle.random_object(NEEDLE_PICTURE, "needle")
     
      

        jeu = 1
        while jeu: #Boucle principale.


            for event in pygame.event.get(): #For all event (touch).
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE: #If we put escape, pygame quit.
                        pygame.quit()

                    if event.key == pygame.K_RIGHT:
                        movement_mac.positive_deplacement(1,20,0)
                        #If we push right arrow,
                        #we actioning right_movement from Movement class.

                        game.incrementation1(1,20,0) #If we push right arrow,
                        #we actioning incrementation1 from Game_class.
                        ether.incrementation1(1,20,0)
                        tube.incrementation1(1,20,0)
                        needle.incrementation1(1,20,0)


                    if event.key == pygame.K_LEFT:
                        movement_mac.negative_deplacement(1, -20, 0)
                        game.incrementation2(1, -20, 0)
                        ether.incrementation2(1, -20, 0)
                        tube.incrementation2(1, -20, 0)
                        needle.incrementation2(1, -20, 0)

                    if event.key == pygame.K_DOWN:
                        movement_mac.positive_deplacement(15,0,20)
                        game.incrementation3(15,0,20)
                        ether.incrementation3(15,0,20)
                        tube.incrementation3(15,0,20)
                        needle.incrementation3(15,0,20)

                    if event.key == pygame.K_UP:
                        movement_mac.negative_deplacement(15, 0, -20)
                        game.incrementation4(15, 0, -20)
                        ether.incrementation4(15, 0, -20)
                        tube.incrementation4(15, 0, -20)
                        needle.incrementation4(15, 0, -20)

                    #If we push K_SPACE, replay = True, main method start.
                    if event.key == pygame.K_SPACE:
                        play.main()

                win.fill((0, 0, 0)) #No trace on our background.
                win.blit(fond_fenetre, (0, 0)) #We put backgound.
                win.blit(fond_fenetre2, (0, 220))
                win.blit(fond_inventory, (300,0))
                win.blit(fond_message, (0,300))
                laby.display(win) #Displaying arrival.
                
                movement_mac.display(win) #Pixel drawing is allowed.
                message1 =  "Inventory: "
                game.message(win, 0, 300, message1)
                
                #Displaying about item picture (after be randomly placed).
            
                ether.display_item(ETHER_PICTURE,PICK_PICTURE, 80,301, win)
                
                tube.display_item(TUBE_PICTURE,PICK_PICTURE, 120,301, win)
                needle.display_item(NEEDLE_PICTURE,PICK_PICTURE, 160,301, win)

                


                   
               
                #If hero pixel move on positionement:
                                   #display message, increment self.counter...
                ether.pickup_item()
 
                tube.pickup_item()
                    
                needle.pickup_item()
                   
                
                
                game.counters(ether.pickup_item(), "ether", COUNTER)
                game.counters(tube.pickup_item(), "tube", COUNTER)
                game.counters(needle.pickup_item(), "needle", COUNTER)

                
                game.end(COUNTER,"ether","needle","tube", win)
                
                

            pygame.display.flip()



if __name__ == "__main__":

    play = Play()
    
    play.main()

