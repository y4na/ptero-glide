import pygame
import random
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1100, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ptero Glide")

icon = pygame.image.load("assets/sprites/ptero_png.png") 
pygame.display.set_icon(icon)

scroll = 0
speed = 0.3

jump_sound = pygame.mixer.Sound("assets/sfx/jump.wav")
death_sound = pygame.mixer.Sound("assets/sfx/die.wav")

NEW_SPRITE_WIDTH = 80       
NEW_SPRITE_HEIGHT = 60
sprite_run = []
for i in range(1, 4):
    sprite_run_path = os.path.join("assets/sprites/fly", f"{i}.png")
    sprite_img_run = pygame.image.load(sprite_run_path)
    sprite_img_run = pygame.transform.scale(sprite_img_run, (NEW_SPRITE_WIDTH, NEW_SPRITE_HEIGHT))
    sprite_run.append(sprite_img_run)
    
sprite_jump = pygame.image.load(os.path.join("assets/sprites/flap", "3.png"))
sprite_jump = pygame.transform.scale(sprite_jump, (NEW_SPRITE_WIDTH, NEW_SPRITE_HEIGHT)) 

tree = []
NEW_TREE_WIDTH = 50 
NEW_TREE_HEIGHT = 100
for i in range(1, 4):
    tree_image_path = os.path.join("assets/foreground/obstacles/trees", f"tree_{i}.png")
    tree_img = pygame.image.load(tree_image_path)
    tree_img = pygame.transform.scale(tree_img, (NEW_TREE_WIDTH, NEW_TREE_HEIGHT))
    tree.append(tree_img)

rock = []
NEW_ROCK_WIDTH = 100
NEW_ROCK_HEIGHT = 120
for i in range(1, 3):
    rock_image_path = os.path.join("assets/foreground/obstacles/rocks", f"middle_lane_rock1_{i}.png")
    rock_img = pygame.image.load(rock_image_path)
    rock_img = pygame.transform.scale(rock_img, (NEW_ROCK_WIDTH, NEW_ROCK_HEIGHT))    
    rock.append(rock_img)

ground_image = pygame.image.load("assets/foreground/ground.png").convert_alpha()
ground_image = pygame.transform.scale(ground_image, (WIDTH, ground_image.get_height()))
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 5):
    bg_image_path = os.path.join("assets/background/clouds2", f"{i}.png")
    bg_image = pygame.image.load(bg_image_path)
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
    bg_images.append(bg_image)

bg_width = bg_images[0].get_width()

bg_images2 = []
for i in range(1, 5):
    bg_image_path2 = os.path.join("assets/background/clouds7", f"{i}.png")
    bg_image2 = pygame.image.load(bg_image_path2)
    bg_image2 = pygame.transform.scale(bg_image2, (WIDTH, HEIGHT))
    bg_images2.append(bg_image2)

bg_width2 = bg_images2[0].get_width()

bg_images3 = []
for i in range(1, 5):
    bg_image_path3 = os.path.join("assets/background/clouds3", f"{i}.png")
    bg_image3 = pygame.image.load(bg_image_path3)
    bg_image3 = pygame.transform.scale(bg_image3, (WIDTH, HEIGHT))
    bg_images3.append(bg_image3)

bg_width3 = bg_images3[0].get_width()


switch_bg_sound = pygame.mixer.Sound("assets/sfx/whoosh2.wav")

current_bg_set = 1
    
def draw_bg():
    global scroll, current_bg_set
    speeds = [1, 1.2, 1.5, 1.8, 2, 2.5]

    if points < 300:
        current_bg_images = bg_images
        current_bg_width = bg_width
        new_bg_set = 1
    elif 300 <= points < 600:
        current_bg_images = bg_images2
        current_bg_width = bg_width2
        new_bg_set = 2
    else:
        current_bg_images = bg_images3
        current_bg_width = bg_width3
        new_bg_set = 3

    if new_bg_set != current_bg_set:
        switch_bg_sound.play()
        current_bg_set = new_bg_set

    for idx, bg_image in enumerate(current_bg_images):
        speed = speeds[idx]

        for x in range(-1, WIDTH // current_bg_width + 2):
            SCREEN.blit(bg_image, ((x * current_bg_width) - (scroll * speed) % current_bg_width, 0))
    
    scroll += 5 * speed
    
def draw_ground():
    global scroll
    for x in range(-1, WIDTH // ground_width + 2):
        SCREEN.blit(ground_image, ((x * ground_width) - (scroll * 2.5) % ground_width, HEIGHT - ground_height))

#ptero is my character 
class ptero:
    X_POS = 80
    JUMP_VEL = 18 # how high mo jump
    OFFSET = 25
    
    def __init__(self):
        self.run_img = sprite_run
        self.jump_img = sprite_jump

        self.ptero_run = True
        self.ptero_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.ptero_rect = self.image.get_rect()
        self.ptero_rect.x = self.X_POS
        self.ptero_rect.y = HEIGHT - ground_height - self.image.get_height() - self.OFFSET
    
    def update(self, userInput):
        if self.ptero_run:
            self.run()
        if self.ptero_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0
            
        if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.ptero_jump:
            self.ptero_jump = True
            self.ptero_run = False
            jump_sound.play()
        elif not (self.ptero_jump or userInput[pygame.K_DOWN]):
            self.ptero_jump = False
            self.ptero_run = True
    
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.step_index += 1 
  
    def jump(self):
        self.image = self.jump_img
        if self.ptero_jump:
            self.ptero_rect.y -= self.jump_vel
            self.jump_vel -= 0.8 # landing

            if self.ptero_rect.y >= HEIGHT - ground_height - self.image.get_height() - self.OFFSET:
                self.ptero_rect.y = HEIGHT - ground_height - self.image.get_height() - self.OFFSET
                self.ptero_jump = False
                self.jump_vel = self.JUMP_VEL 
           
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.ptero_rect.x, self.ptero_rect.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = WIDTH
        
        self.speed = 20

    def update(self):
        self.rect.x -= self.speed * speed
        if self.rect.x < -self.rect.width:
            obstacles.remove(self)

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

        
class Tree(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, len(image) - 1)  
        super().__init__(image, self.type)
        self.rect.y = HEIGHT - ground_height - self.image[self.type].get_height() + 10

class Rock(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, len(image) - 1) 
        super().__init__(image, self.type)
        self.rect.y = HEIGHT - ground_height - self.image[self.type].get_height() + 10

        
points = 0
score_counter = 0

def score():
    global points, scroll, speed, score_counter
    font = pygame.font.Font('assets/fonts/JungleWoodRegular.ttf', 20)
    
    score_counter += 1
    if score_counter % 5 == 0:
        points += 1
        
    if points % 100 == 0 and points > 0:
        speed += 0.05
        
    text = font.render("SCORE: " + str(points), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (1000, 40)
    SCREEN.blit(text, textRect)
  
death_count = 0
     
PTERO = [pygame.image.load(os.path.join("assets/sprites", "ptero_png.png"))]
GAMEOVER = [pygame.image.load(os.path.join("assets/background", "game_over_title.png"))]

     
def menu(death_count):
    global points
    run = True

    pygame.mixer.music.load("assets/sfx/bg_music.mp3")
    pygame.mixer.music.set_volume(0.3)
    
    game_over_resize = pygame.transform.scale(GAMEOVER[0], (int(GAMEOVER[0].get_width() * 1.5), int(GAMEOVER[0].get_height() * 1.5)))

    while run:
        if death_count == 0:
            pygame.mixer.music.load("assets/sfx/bg_music.mp3")
            pygame.mixer.music.play(loops=-1)
            pygame.mixer.music.set_volume(0.3)
        
        if death_count > 0:
            draw_bg()
            draw_ground()
            font = pygame.font.Font('assets/fonts/JungleWoodRegular.ttf', 50)
            text = font.render("Press any Key to START", True, (255, 255, 176))
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, HEIGHT // 2 - 50) 
            SCREEN.blit(text, textRect)
            
            game_over_x = (WIDTH // 2) - (game_over_resize.get_width() // 2)
            game_over_y = (HEIGHT // 2) - (game_over_resize.get_height() // 2) + 10
            SCREEN.blit(game_over_resize, (game_over_x, game_over_y))
            
            score = font.render("Your Score: " + str(points), True, (255, 255, 176))
            scoreRect = score.get_rect()
            scoreRect.center = (WIDTH // 2, HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        else:
            draw_bg()
            draw_ground()
            font = pygame.font.Font('assets/fonts/JungleWoodRegular.ttf', 50)
            text = font.render("Press any Key to START", True, (255, 255, 176))
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, HEIGHT // 2)
            SCREEN.blit(text, textRect)
            
            ptero_x = (WIDTH // 2) - (PTERO[0].get_width() // 2)
            ptero_y = (HEIGHT // 2) - (PTERO[0].get_height() // 2) - 140 
            SCREEN.blit(PTERO[0], (ptero_x, ptero_y))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.play(loops=-1)
                main()
                
    pygame.quit()

def game_over():
    global death_count
    pygame.mixer.music.stop()
    menu(death_count)
          
def main():
    global scroll, points, obstacles, death_count, coins
    points = 0
    obstacles = []
    coins = []
    run = True
    clock = pygame.time.Clock()
    player = ptero()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
                
        draw_bg()
        userInput = pygame.key.get_pressed()
        
        player.draw(SCREEN)
        player.update(userInput)
        
        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(Tree(tree))
            elif random.randint(0,2) == 1:
                obstacles.append(Rock(rock))
                
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            
            if player.ptero_rect.colliderect(obstacle.rect):
                death_sound.play()
                # collision border
                # pygame.draw.rect(SCREEN, (255, 0, 0), player.ptero_rect, 2) 
                pygame.time.delay(1000) 
                death_count += 1
                menu(death_count)
        
        draw_ground()        
        score()
        
        clock.tick(30)
        pygame.display.update()

    pygame.quit()
 
menu(death_count=0)