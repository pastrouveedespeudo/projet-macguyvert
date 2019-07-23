#-*- coding: utf-8 -*-

"""
here is the movement class or we define an image that we will move from the txt file.
"""


import pygame #Import pygame module.

from labyrinth_class import* #Import labyrinth_class class.


class Movement:
    """Here we call get_rect() fonction for moving picture hero,
    thank to labyrinth_class we generate structure with place
    where he can moves or not"""

    def __init__(self, file): #Creating constructor.
        self.file = file

        self.structure = []

    def position(self, image):
        """  Definition of positon method with initialization of picture. """

        self.image = image
        self.perso = pygame.image.load(self.image)

        #We put picture into a rectangle for move it.
        self.position = self.perso.get_rect()

        #This variable will go into list, and we will add to it for see if it's possible to move.
        self.x = 0

    def importation_file(self):
        """ Importation of the list from labyrinth class. """

        Labyrinth.generate(self)



    def positive_deplacement(self, nombre_case, deplacement_x, deplacement_y):

        self.nombre_case = nombre_case
        self.deplacement_x = deplacement_x
        self.deplacement_y = deplacement_y
        
        if self.structure[self.x + self.nombre_case][1] != "1":
            self.x += self.nombre_case
            self.position = self.position.move(deplacement_x, deplacement_y)

        elif self.structure[self.x + self.nombre_case][1] == "1":
            self.x += 0


    def negative_deplacement(self, nombre_case, deplacement_x, deplacement_y ):
        """ Definition of left movement. """

        self.nombre_case = nombre_case
        self.deplacement_x = deplacement_x
        self.deplacement_y = deplacement_y

        
        if self.structure[self.x - self.nombre_case][1] != "1":
            self.x -= self.nombre_case
            self.position = self.position.move(deplacement_x, deplacement_y)

        elif self.structure[self.x - self.nombre_case][1] == "1":
            self.x -= 0















    def display(self, window):
        """ Display picture to window. """

        window.blit(self.perso, self.position)
        pygame.display.flip()
