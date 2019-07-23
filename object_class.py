import random
from pygame.locals import *   #Importing pygame modules.
import pygame
from labyrinth_class import *
from constant import *
from game_class import *



class Object:


    def __init__(self,file):
        self.file = file
        self.structure = []
        self.x = 0
        self.item_inventory = pygame.image.load(PICK_PICTURE)
        self.counter = []
        
    def importation_file(self,image):
        Labyrinth.generate(self)
        Movement.position(self,image)
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
        
    def random_object(self,image, objet):

            self.objet = objet
            self.item = pygame.image.load(image)
            
            
            rand_object = []

            for element_0 in self.structure:
                if element_0[1] == "0":
                    rand_object.append(element_0)

            
            self.random_object = random.choice(rand_object)
            self.item_indexing = self.structure.index(self.random_object)

            self.item_position_x = self.structure[self.item_indexing][0][1] * SIZE_CASE
            self.item_position_y = self.structure[self.item_indexing][0][0] * SIZE_CASE
            



    def display_item(self,item, item_inventory, pos_x, pos_y, window):
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        window.blit(self.item, (self.item_position_x, self.item_position_y))
        window.blit(self.item_inventory, (self.pos_x, self.pos_y))
        
        if self.structure[self.x] == self.random_object:

            self.item = pygame.image.load(PICK_PICTURE)
            self.item_inventory = pygame.image.load(item)
            


    def pickup_item(self):
        
        if self.structure[self.x] == self.random_object:
            self.counter.append(str(self.objet))
            if self.objet in self.counter:
                return True
        
            
        
        
            
