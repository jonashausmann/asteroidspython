import random
import constants
import pygame
import circleshape
class Asteroid(circleshape.CircleShape):
    def __init__(self,x,y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity*dt)

    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            velocity_asteroid_1 = self.velocity.rotate(random_angle)
            velocity_asteroid_2 = self.velocity.rotate(-random_angle)
            new_asteroids_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
            asteroid_1.velocity = velocity_asteroid_1*1.2


            asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
            asteroid_2.velocity = velocity_asteroid_2*1.2

            


