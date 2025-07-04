import pygame

from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, shots)

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock =  pygame.time.Clock()
    dt = 0

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    a_field = AsteroidField()




    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for item in updatable:
            item.update(dt)


        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                raise SystemExit
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
            

            
        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()
        
        dt = clock.tick(60)/1000




    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()