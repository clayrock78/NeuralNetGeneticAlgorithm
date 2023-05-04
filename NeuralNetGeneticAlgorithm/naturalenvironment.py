# Importing the library
import pygame
from individual import Individual
import random
import numpy as np
from collisions import collision
import math

WIDTH, HEIGHT = 500, 500
FOODRADIUS = 20
PLAYERWIDTH = 10
class Player():
    def __init__(self):

        self.x = random.randint(0,WIDTH  * 1000)
        self.y = random.randint(0,HEIGHT * 1000)

        self.pos = pygame.Rect(self.x, self.y, PLAYERWIDTH, PLAYERWIDTH)
        

    def move(self, dx, dy):
        self.x += dx*300
        self.y += dy*300
        self.pos.centerx = round(self.x/1000)
        self.pos.centery = round(self.y/1000)
        
        

    def display(self, color=(255,0,0)):
        pygame.draw.rect(surface, color, self.pos)

red = (255,0,0)
lime_green = (100,255,100)


# Initializing Pygame
pygame.init()
clock = pygame.time.Clock()
dt = 1

DISPLAY_STUF = True
# Initializing surface
surface = pygame.display.set_mode((WIDTH, HEIGHT))
def find_fitness(population):
    pop_size = len(population)
    food_pool = [[random.random() * WIDTH, random.random() * HEIGHT] for i in range(1)]

    player_pool = [Player() for x in range(pop_size)]
    fitness_values = [0 for _ in player_pool]
    
    for tick in range(1000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if (DISPLAY_STUF):
            surface.fill([0,0,0])
            for food in food_pool:
                #pygame.draw.rect(surface, (0,255,255), pygame.Rect(food[0], food[1], 10, 10 ))
                pygame.draw.circle(surface, lime_green, [food[0], food[1]], FOODRADIUS)

        for pop_index, player in enumerate(player_pool):

            # check bounds
            if player.pos.centerx > WIDTH or player.pos.centerx < 0 or player.pos.centery > HEIGHT or player.pos.centery < 0:
                pass
                #fitness_values[pop_index] -= 0
        
            #fitness_values[pop_index] += 0
            """
            input_layer = food_pool
            input_layer = list(np.array(input_layer).flatten())
            input_layer.append(player.x)
            input_layer.append(player.y)
            input_layer = [x/WIDTH for x in input_layer]
            """
            input_layer = [player.pos.centerx/WIDTH, player.pos.centery/HEIGHT, food_pool[0][0]/WIDTH, food_pool[0][1]/HEIGHT]
            velocity = population[pop_index].activate(input_layer)

            #player.move(velocity[0] * dt - velocity[1] * dt, velocity[2] * dt - velocity[3] * dt)
            dx = velocity[0] * dt - velocity[1] * dt
            dy = velocity[2] * dt - velocity[3] * dt
            #print(dx, dy)
            player.move(dx, dy)
            if (DISPLAY_STUF):
                player.display()
        
            dist = ((player.pos.centerx - food[0]) ** 2 + (player.pos.centery - food[1]) ** 2)**.5
            fitness_values[pop_index] = WIDTH - dist


        if (DISPLAY_STUF):
            pygame.display.flip()

    return fitness_values

    
# 527