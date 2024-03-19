import pygame

def draw_word(word):
    word_surface = font.render(word, True, (255,0,0))
    word_rect = word_surface.get_rect(center = (400,300))
    screen.blit(word_surface,word_rect)

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Typer')
clock = pygame.time.Clock()


font = pygame.font.Font(None,60)
pixel_font_120 = pygame.font.Font('assests/font/Pixeltype.ttf', 120)


render = pixel_font_120.render('Hello Word', False, (255,0,0)).convert_alpha()
render_rect = render.get_rect(center = (400,300))


word_list = ['apple','banana','cat','dog']
word_list_index = 0
word = word_list[word_list_index]

typed_word = ''

# Timer
timer_line = pygame.Rect(0,0,800,10)

TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 2)

TIMER_RESET = pygame.USEREVENT + 2
pygame.time.set_timer(TIMER_RESET, 2000)



def change_var():
  global no
  no = (no + 1) % 256
no = 1
running = True
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    word_list_index += 1
                    if word_list_index < len(word_list): word = word_list[word_list_index]
                    else:
                        word_list_index = 0
                        word = word_list[word_list_index]
            # for timer            
            elif event.type == TIMER_EVENT:
                timer_line.width -= 1
            elif event.type == TIMER_RESET:
                timer_line.width = 800

    screen.fill((255,255,255))
    render.set_alpha(no)
    change_var()
    print(no)
    screen.blit(render,render_rect)
    # pygame.draw.rect(screen, (255, 0, 0), timer_line)
    # draw_word(word)
    pygame.display.update()
    clock.tick(60)


