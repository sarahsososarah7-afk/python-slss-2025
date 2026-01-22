# Author: Sarah

import pygame
import random

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
PINK  = (255, 255, 255)
BLACK= (  0,   0,   0)
YELOW  = (255,   0,   0)
GREEN = (  0, 255,   0)
BROWN = (  0,   0, 255)
GREY  = (128, 128, 128)


class Block(pygame.sprite.Sprite):
    def __init__(self, colour: pygame.Color, width: int, height: int):
        """A fruits of any colour"""
        super().__init__()

# Game settings
FPS = 60
FRUIT_FALL_SPEED = 5
FRUIT_SIZE = 15
FRUIT_DROP_INTERVAL = 100

# images

# Visual representation of our image
self.image = pygame.Surface((width, height))
# change the colour of self.image
self.image.fill(colour)

# A Rect tells you two things:
#   - how big the hitbox is (width, height)
#   - where it is (x, y)
self.rect = self.image.get_rect()
self.rect.centerx = 100
self.rect.centery = 100

self.point_value = 10

def level_up(self, val: int):
    """Incr point value"""
    self.point_value *= val

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """The player"""
        super().__init__()


        # Right version of Mario and Left version
        self.image_right =  pygame.image.load("8-bit-retro-game-background-free-vector.jpg")
        self.fruit_image =  pygame.image.load("set-fruits-in-cartoon-style-for-video-game-isolated-on-white-background-2R9N3XM.jpg")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        #Drop fruit
     if frame_count % FRUIT_DROP_INTERVAL == 0:
        fruit_x=random.randint(0,width-50)
        fruit.append(pygame.Rect(fruit_x,0,50,50))

        # Move fruit down
        for fruit in fruits:
fruit.y += FRUIT_FALL_SPEED
if fruit.cooliderect(mairo_react):
    print("Fruit hit Mario!")
    rubbing = False
    # Remove fruits if it falls down
    elif fruit.y > HEIGHT:
        fruits.remove(fruit)

 self.image = self.image_right
 self.rect = self.image.get_rect()

 self.previous_x = 0               # help with direction
 self.health = 100
 self.points = 0


def incr_score(self, amt: int) -> int:
 """Increases player score by amt
 Returns:
     Score"""
 self.points += amt
 return self.points

def get_damage_percentage(self) -> float:
 return self.health / 100

def update(self):
 """Update Mario's location based on the mouse pos
 Update Mario's image based on where he's going"""
 self.rect.center = pygame.mouse.get_pos()

 # If Mario's previous x less than current x
 #   Then Mario is facing Right
 # If Mario's previous x is greater than current x
 #   Then Mario is facing Left
 if self.previous_x < self.rect.x:
     self.image = self.image_right
 elif self.previous_x > self.rect.x:
     self.image = self.image_left

 self.previous_x = self.rect.x

class Enemy(pygame.sprite.Sprite):
def __init__(self):
 super().__init__()
 self.image = pygame.image.load("assets/goomba-nes.png")
 self.rect = self.image.get_rect()

 self.vel_x = 0
 self.vel_y = 0

 self.damage = 1

def update(self):
 # movement in the x- and y-axis
 self.rect.x += self.vel_x
 self.rect.y += self.vel_y

def level_up(self):
 # increase damage
 self.damage *= 2

class HealthBar(pygame.Surface):
def __init__(self, width: int, height: int):
 self._width = width
 self._height = height
 super().__init__((width, height))

 self.fill(YELLOW)

def update_info(self, percentage: float):
 """Updates the healthbar with the given percentage"""
 self.fill(YELLOW)
 pygame.draw.rect(self, GREEN, (0, 0, percentage * self._width, self._height))

def game():
pygame.init()

   # CONSTANTS
   WIDTH = 800
   HEIGHT = 600
   SIZE = (WIDTH, HEIGHT)

   # Creating the Screen
   screen = pygame.display.set_mode(SIZE)
   pygame.display.set_caption("Collect Fruits")

   # Variables
   done = False
   clock = pygame.time.Clock()
   num_enemies = 8
   num_blocks = 50
   health_bar = HealthBar(200, 10)
   level = 1

   # Create a Sprite Group
   all_sprites_group = pygame.sprite.Group()
   block_sprites_group = pygame.sprite.Group()
   enemy_sprites_group = pygame.sprite.Group()

   # Create Enemies
   for _ in range(num_enemies):
       # Create an enemy
       enemy = Enemy()
       # Randomize movement
       random_x = random.choice([-5, -3, -1, 1, 3, 5])
       random_y = random.choice([-5, -3, -1, 1, 3, 5])
       enemy.vel_x, enemy.vel_y = random_x, random_y
       # Start them in the middle
       enemy.rect.center = (WIDTH/2, HEIGHT/2)

       all_sprites_group.add(enemy)
       enemy_sprites_group.add(enemy)

   # Create 100 fruits
   # Randomly place them throughout the screen
   for _ in range(num_fruits):
       fruits = Fruit(PINK, 20, 10)
       # Choose a random position for it
       block.rect.centerx = random.randrange(0, WIDTH)
       block.rect.centery = random.randrange(0, HEIGHT)

       all_sprites_group.add(block)
       block_sprites_group.add(block)

   # Create a player
   player = Mario()
   player.rect.center = (WIDTH / 2, HEIGHT / 2)
   # Add the player to the sprite group
   all_sprites_group.add(player)

   # ------------ MAIN GAME LOOP
   while not done:
       # ------ MAIN EVENT LISTENER
       # when the user does something
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               done = True

       # ------ GAME LOGIC
       all_sprites_group.update()

       # Keep enemies in screen
       for enemy in enemy_sprites_group:
           if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
               enemy.vel_x = -enemy.vel_x
           if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
               enemy.vel_y = -enemy.vel_y

       # Collision between Player and Blocks
       fruit_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
       # if the blocks_collided list has something in it
       # print Mario has collided with a block!
       for fruit in fruit_collided:
           if type(fruit) is Fruit:
               print("Player score: ", player.incr_score(block.point_value))

       # Fill blocks if block list is empty
       # Add more blocks and add one enemy
       if not block_sprites_group:
           level += 1

           for _ in range(num_blocks):
               block = Block(BROWN, 20, 10)
               # Choose a random position for it
               block.rect.centerx = random.randrange(0, WIDTH)
               block.rect.centery = random.randrange(0, HEIGHT)

               block.level_up(level)

               all_sprites_group.add(block)
               block_sprites_group.add(block)

           enemy = Enemy()
           random_x = random.choice([-5, -3, -1, 1, 3, 5])
           random_y = random.choice([-5, -3, -1, 1, 3, 5])
           enemy.vel_x, enemy.vel_y = random_x, random_y
           # Start them in the middle
           enemy.rect.center = (WIDTH/2, HEIGHT/2)
           all_sprites_group.add(enemy)
           enemy_sprites_group.add(enemy)

           for enemy in enemy_sprites_group:
               enemy.level_up()

       # Collision between Player and Enemies
       enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites_group, False)
       for enemy in enemies_collided:
           # decrease mario's life
           player.calc_damage(enemy.damage)

       health_bar.update_info(player.get_damage_percentage())

       # Game ends when Player's health is zero or less
       if player.health <= 0:
           done = True

       # ------ DRAWING TO SCREEN
       screen.fill(GREY)
       all_sprites_group.draw(screen)
       screen.blit(health_bar, (10, 10))

       # Update screen
       pygame.display.flip()

       # ------ CLOCK TICK
       clock.tick(60) # 60 fps

   # Display final score:
   print("Thanks for playing!")
   print("Final score is:", player.points)

   pygame.quit()

if __name__ == "__main__":
   game()
