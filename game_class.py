#-*- coding: utf-8 -*-

"""
This is the class game, here we make appear randomly objects.
The hero must pick up the objects, so we count them,
if the hero has the 3 objects (ether, needle, tube) and arrives at the point of arrival he wins,
else he looses.
"""

import pygame #Import pygame module.
import random #Import random module.

from movement_class import * #Import movement_class.
from constant import * #Import constant class.
from object_class import *

COUNTER = []
class Game:
    """Game class, display, end condition, inventory"""
    def __init__(self, file): #Initialization constructor.
        """ we initialize the file and the variables for later. """

        self.file = file #File initialization

        #Counter of object,(if compteur has the 3 objects, hero wins).
        self.counter = []

        #We initiate member structure.
        self.structure = []

        #We initiate member self.x.
        self.x = 0

        #We charging inventory by black picture
        self.item_inventory = pygame.image.load(PICK_PICTURE)

        self.random_object = 0
        self.end_condition = 0


        
    def importation_file(self, image):
        """ Importation file labyrinth for recover the structure for random object. """

        Labyrinth.generate(self)
        Movement.position(self, image) #We importing position from Movement.
        self.image = image
        self.perso = pygame.image.load(self.image)
        
    def incrementation1(self, nombre_case, deplacement_x, deplacement_y):
        """ We increment or not x from movement_class for the method pickup,
            (right_side)"""

        Movement.positive_deplacement(self, nombre_case, deplacement_x, deplacement_y)
        self.nombre_case = nombre_case
        self.deplacement_x = deplacement_x
        self.deplacement_y = deplacement_y

    def incrementation2(self, nombre_case, deplacement_x, deplacement_y):
        """ We increment or not x from movement_class for the method pickup,
            (left_side)"""

        Movement.negative_deplacement(self, nombre_case, deplacement_x, deplacement_y)
        self.nombre_case = nombre_case
        self.deplacement_x = deplacement_x
        self.deplacement_y = deplacement_y


    def incrementation3(self, nombre_case, deplacement_x, deplacement_y):
        """ We increment or not x from movement_class for the method pickup,
            (down side)."""

        Movement.positive_deplacement(self, nombre_case, deplacement_x, deplacement_y)

        self.nombre_case = nombre_case
        self.deplacement_x = deplacement_x
        self.deplacement_y = deplacement_y

    def incrementation4(self, nombre_case, deplacement_x, deplacement_y):
        """ We increment or not x from movement_class for the method pickup,
            (top side)."""

        Movement.negative_deplacement(self, nombre_case, deplacement_x, deplacement_y)
        self.nombre_case = nombre_case
        self.deplacement_x = deplacement_x
        self.deplacement_y = deplacement_y



#-----------------------Part object-----------------------------------


    def message(self, window, x_pos, y_pos,message):
        """ We have put message inventory for item picked."""
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        
        police_window_message = pygame.font.SysFont("BradBunR.ttf", 20)
        window_message = police_window_message.render(message,
                                                      True, (255, 10, 20))
        #window.blit(window_message, (0, 300))
        window.blit(window_message, (self.x_pos, self.y_pos))


#----------------------------------------------------------------------------
    def counters(self, one,un, liste):
        self.liste = liste
        self.one = one
        self.un = un

        if self.one == True :
            self.liste.append(self.un)
        

    def end(self,liste,item1, item2, item3, window):
        message2 = "LOOSE! Re-start? Press space, else ESC"
        message3 = "WIN! Re-start? Press space, else ESC"
        self.liste = liste
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        if self.structure[self.x][1] == "A":
            if self.item1 in self.liste and \
            self.item2 in self.liste and \
            self.item3 in self.liste:
                Game.message(self, window, 20, 350,message3)
                
            else:
                #If hero hasn't got all items we display loose message.
                Game.message(self, window, 20, 350,message2)
   



    
