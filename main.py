import pygame
from sys import exit
from random import randint

def draw_text(text, color):
    rendered_text = pixel_font_120.render(text, False, color)
    text_rect = rendered_text.get_rect(center = (400,300))
    screen.blit(rendered_text, text_rect)

def draw_input():
    rendered_input_text = pixel_font_60.render(typed_text, False, (150, 150, 150))
    text_rect = rendered_input_text.get_rect(center = (400,350))
    screen.blit(rendered_input_text,text_rect)

def draw_score():
    rendered_score = pixel_font_30.render(f'Score: {score}', False, (0,255,0))
    score_rect = rendered_score.get_rect(topleft = (10,30))
    screen.blit(rendered_score,score_rect)

def draw_fails():
    global words_wrong
    cross = pygame.image.load('assets/cross2.png')
    cross_overlay = pygame.image.load('assets/cross1.png')
    if words_wrong == 0:
        screen.blit(cross_overlay,(770,30))
        screen.blit(cross_overlay,(750,30))
        screen.blit(cross_overlay,(730,30))
    if words_wrong == 1:
        screen.blit(cross_overlay,(770,30))
        screen.blit(cross_overlay,(750,30))
        screen.blit(cross,(730,30))
    if words_wrong == 2:
        screen.blit(cross_overlay,(770,30))
        screen.blit(cross,(750,30))
        screen.blit(cross,(730,30))
    if words_wrong == 3:
        screen.blit(cross,(770,30))
        screen.blit(cross,(750,30))
        screen.blit(cross,(730,30))

def calc():
    global typed_text, score, dummy_words, word_index, word
    if typed_text == word:
        scoresound = pygame.mixer.Sound('assets/audio/scoreup.mp3')
        scoresound.play()
        score += 1
        word_index += 1
        typed_text = ''
        if word_index < len(dummy_words):word = dummy_words[word_index]
        else:
            word_index = 0
            word = dummy_words[word_index]
        timer_line.width = 800
        
def draw_timer_line():
    global timer_line, word, words_wrong, typed_text, score, dummy_words, word_index, word
    if timer_line.width > 533:
        pygame.draw.rect(screen,(51, 204, 51),timer_line)
    elif timer_line.width > 267:
        pygame.draw.rect(screen,(255, 102, 0),timer_line)
    elif timer_line.width > 0:
        pygame.draw.rect(screen,(255, 0, 0),timer_line)
    
    if timer_line.width <= 0:
        fail.play()
        timer_line.width = 800
        words_wrong += 1
        wrong_word_list.append(word)
        word_index += 1  
        typed_text = ''
        if word_index < len(dummy_words):word = dummy_words[word_index]
        else:
            word_index = 0
            word = dummy_words[word_index]

def get_number():
    global alpha, add_mode
    if add_mode:alpha += 5
    else:alpha -= 5
    if alpha == 255:add_mode = False
    if alpha == 0:add_mode = True


# Ini
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Typer')

clock = pygame.time.Clock()
running = False

# Fonts
default_font = pygame.font.Font(None, 60)
pixel_font_120 = pygame.font.Font('assets/font/Pixeltype.ttf', 120)
pixel_font_90 = pygame.font.Font('assets/font/Pixeltype.ttf', 90)
pixel_font_60 = pygame.font.Font('assets/font/Pixeltype.ttf', 60)
pixel_font_30 = pygame.font.Font('assets/font/Pixeltype.ttf', 30)


# Game Backgrounds music
bg = pygame.mixer.Sound('assets/audio/bgm.mp3')
fail = pygame.mixer.Sound('assets/audio/fail.mp3')
fail.set_volume(.3)
bg.set_volume(.2)
bg.play(loops= -1)

# START / END TEXTS
game_text = pixel_font_120.render('WordRush V2', False, (0, 114, 199))
game_text_rect = game_text.get_rect(center = (400,200))

start_input_text = pixel_font_60.render("Press ENTER to start.", False, (0, 114, 199))
start_input_text_rect = start_input_text.get_rect(center = (400, 420))

alpha = 0
add_mode = True

dummy_words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'giraffe', 'horse', 'iguana', 'jellyfish']
word_index = 0
word = dummy_words[word_index]
score = 0
words_wrong = 0
wrong_word_list = []

typed_text = ''

timer_line = pygame.Rect(0,0,800,10)
TIMER_EVENT = pygame.USEREVENT + 1
# Ticks every 4 milli seconds, so if i remove a pixel every 4 ms, thats 3200 ms to get it all
pygame.time.set_timer(TIMER_EVENT,4)

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == TIMER_EVENT:
                timer_line.width -= 1

            elif event.type == pygame.KEYDOWN:
                if running:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

                    elif event.key == pygame.K_RETURN:
                        fail.play()
                        word_index += 1
                        typed_text = ''
                        words_wrong += 1
                        if word_index < len(dummy_words):word = dummy_words[word_index]
                        else:
                            word_index = 0
                            word = dummy_words[word_index]
                    
                    elif event.key == pygame.K_BACKSPACE:
                        typed_text = typed_text[:-1]
                    
                    elif event.unicode.isalpha():
                        typed_text += event.unicode.lower()
                else:
                    if event.key == pygame.K_RETURN:
                        # resets
                        timer_line.width = 800
                        words_wrong = 0
                        wrong_word_list = []
                        score = 0
                        running = True

            
    if running:
        screen.fill('#062130')
        draw_fails()
        draw_timer_line()
        draw_text(word,(150,150,150))
        draw_input()
        draw_score()
        calc()
        if words_wrong == 3: running = False
        else: running = True
    else:
        
        # End/start screen
        screen.fill((0,0,0))
        screen.blit(game_text,game_text_rect)

        start_input_text.set_alpha(alpha)
        screen.blit(start_input_text,start_input_text_rect)
        get_number()

        if score != 0:
            rendered_score = pixel_font_60.render(f'Score: {score}', True, (0,255,0))
            score_rect = rendered_score.get_rect(center = (400,350))
            screen.blit(rendered_score,score_rect)
    # Screen Update
    pygame.display.update()
    clock.tick(60)