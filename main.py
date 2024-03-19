import pygame
from sys import exit
from random import randint

def draw_text(text, color):
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center = (400,300))
    screen.blit(rendered_text, text_rect)

def draw_input():
    rendered_input_text = font.render(typed_text, True, GREY)
    text_rect = rendered_input_text.get_rect(center = (400,350))
    screen.blit(rendered_input_text,text_rect)

def draw_score():
    rendered_score = font.render(f'Score: {score}', True, GREEN)
    score_rect = rendered_score.get_rect(center = (400,250))
    screen.blit(rendered_score,score_rect)

def draw_words_wrong():
    rendered_wrong_score = font.render(f'Fails: {words_wrong}', True, RED)
    score_rect = rendered_wrong_score.get_rect(center = (400,350))
    screen.blit(rendered_wrong_score,score_rect)
def calc():
    global typed_text, score, dummy_words, word_index, word
    if typed_text == word:
        score += 1
        word_index += 1
        typed_text = ''
        if word_index < len(dummy_words):word = dummy_words[word_index]
        else:
            word_index = 0
            word = dummy_words[word_index]
        timer_line.width = 800
        
def draw_timer_line():
    global timer_line, word, words_wrong
    if timer_line.width > 533:
        pygame.draw.rect(screen,(51, 204, 51),timer_line)
    elif timer_line.width > 267:
        pygame.draw.rect(screen,(255, 102, 0),timer_line)
    elif timer_line.width > 0:
        pygame.draw.rect(screen,(255, 0, 0),timer_line)
    
    if timer_line.width <= 0:
        timer_line.width = 800
        words_wrong += 1
        wrong_word_list.append(word)

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Typer')
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()
running = True

# Colors
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                elif event.key == pygame.K_RETURN:
                    word_index += 1
                    typed_text = ''
                    if word_index < len(dummy_words):word = dummy_words[word_index]
                    else:
                        word_index = 0
                        word = dummy_words[word_index]
                
                elif event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]
                
                elif event.unicode.isalpha():
                    typed_text += event.unicode.lower()
            
    
    screen.fill((255,255,255))
    draw_words_wrong()
    draw_timer_line()
    draw_text(word,RED)
    draw_input()
    draw_score()
    calc()

    # Screen Update
    pygame.display.update()
    clock.tick(60)