#-*- coding: utf-8 -*-

"""
here is the labyrinth class,
here we will generate the list that will help us to move,
to put the random objects ...
on the one hand we open the txt file,
we make a grid 15/15 boxes then we mix the two.
"""


import pygame #Import pygame module.

from constant import GARDIAN_PICTURE, SIZE_CASE #Import constant file.


class Labyrinth:
    """We generationg the structure of labyrinth system"""

    def __init__(self, file):
        """ Initialization file. """
        self.file = file

    def generate(self):
        """ We mixe the 2 last lists, element casee/element grid. """

        with open(self.file, "r") as file: #We open the file.

            casee = [] #Initialization empty list.
            grid = [] #We creating grid 15/15 cases.
            for line in file: # We go in file and add element to casee.
                for element in line:
                    if element != "\n": # If element isn't \n
                        casee.append(element) #We add element to empty case.
            for line in range(0, 15):
                for row in range(0, 15):
                    grid.append((line, row))           

    
        self.structure = [] #We mixing element file with element grid
        i = 0
        while i < len(casee):
            self.structure.append([grid[i], casee[i]])
            i += 1


    def display(self, win):
        """ Display gardian picture at position A of the file txt. """

        gardian = pygame.image.load(GARDIAN_PICTURE)

        for line in self.structure:
            if line[1] == "A":

                x_end = int(line[0][1]) * SIZE_CASE
                y_end = int(line[0][0]) * SIZE_CASE

                win.blit(gardian, (x_end, y_end))
