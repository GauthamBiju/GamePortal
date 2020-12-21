import pygame
import sys
import random
import math
from pygame import mixer
mixer.init()

pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
brown = (100, 40, 0)
dis_width = 600
dis_height = 400

# the styles and fonts

font = pygame.font.SysFont('comicsans', 40)
font_answer = pygame.font.SysFont('comicsans', 60)
font_result = pygame.font.SysFont('comicsans', 100)
font_result_correct_answer = pygame.font.SysFont('comicsans', 50)
font_title_opening = pygame.font.SysFont('lucida calligraphy', 100, italic=True)
medium_font = pygame.font.SysFont('showcard gothic', 30, True)
large_font = pygame.font.SysFont('chiller', 60, True, True)


def portal():
    dis = pygame.display.set_mode((900, 500))
    dis.fill(white)
    a = large_font.render("The Gaming Portal", True, black)
    b = medium_font.render("Snake", True, red)
    c = medium_font.render("Hangman", True, red)

    e = a.get_rect()
    f = b.get_rect()
    g = c.get_rect()


    e.center = (450, 50)
    f.center = (200, 200)
    g.center = (700, 200)

    pygame.draw.circle(dis, black, (200, 200), 70)
    pygame.draw.circle(dis, black, (700, 200), 70)


    dis.blit(a, e)
    dis.blit(b, f)
    dis.blit(c, g)

    pygame.display.set_caption('Game Portal ')

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > g.left and x < g.right:
                    if y > g.top and y < g.bottom:
                        hangman()
                if x > f.left and x < f.right:
                    if y > f.top and y < f.bottom:
                        snakeGame()

        pygame.display.update()

#game loop for snakeGame
def snakeGame():
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    brown = (100, 40, 0)
    dis_width = 600
    dis_height = 400
    # assigning the font and colour to different variable
    medium_font = pygame.font.SysFont('showcard gothic', 30, True)
    large_font = pygame.font.SysFont('chiller', 60, True, True)
    intermediate_font = pygame.font.SysFont('showcard gothic', 50, True)

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game ')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 10


    score_font = pygame.font.SysFont("comicsansms", 35)
#creating the game initiation window
    def start_game():
        dis = pygame.display.set_mode((dis_width, dis_height))
        dis.fill(white)
        # Creating a surface object from the text
        start_font1 = large_font.render("Snake Game", True, black)
        start_font2 = medium_font.render("Play Game", True, red)
        start_font3 = medium_font.render("Back", True, red)
        start_font4 = medium_font.render("Quit", True, red)
        # creating a rectangular surface for each of the text
        start_font1_rect = start_font1.get_rect()
        start_font2_rect = start_font2.get_rect()
        start_font3_rect = start_font3.get_rect()
        start_font4_rect = start_font4.get_rect()

        start_font1_rect.center = (300, 100)
        start_font2_rect.center = (300, 200)
        start_font3_rect.center = (550, 20)
        start_font4_rect.center = (300, 250)

        dis.blit(start_font1, start_font1_rect)
        dis.blit(start_font2, start_font2_rect)
        dis.blit(start_font3, start_font3_rect)
        dis.blit(start_font4, start_font4_rect)

        pygame.display.set_caption('Snake Game ')

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameLoop()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # creating interactive buttons
                    x, y = event.pos
                    if x > start_font3_rect.left and x < start_font3_rect.right:
                        if y > start_font3_rect.top and y < start_font3_rect.bottom:
                            portal()
                    if x > start_font2_rect.left and x < start_font2_rect.right:
                        if y > start_font2_rect.top and y < start_font2_rect.bottom:
                            gameLoop()
                    if x > start_font4_rect.left and x < start_font4_rect.right:
                        if y > start_font4_rect.top and y < start_font4_rect.bottom:
                            pygame.quit()
                            sys.exit()

            pygame.display.update()

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, yellow)
        pygame.draw.line(dis, green, (0, 40), (600, 40))
        pygame.draw.line(dis, yellow, (540, 0), (540, 40))
        # displaying the score
        dis.blit(value, [0, 0])

    def our_snake(snake_block, snake_list):
        n = 0
        for x in snake_list:
            if n == (len(snake_list) - 1):
                pygame.draw.circle(dis, brown, (x[0], x[1]), 10)
                # head of snake
            elif n == 0:
                pygame.draw.circle(dis, red, (x[0], x[1]), 5)
                # tail of snake
            else:
                pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
                # increasing the length of snake
            n = n + 1

    # defining the game
    def gameLoop():
        game_over = False
        game_close = False
        # initial position of snake
        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1
        # position of food

        foodx = round(random.randrange(10, 590, 10))
        foody = round(random.randrange(70, 400, 10))

        while not game_over:

            while game_close == True:
                dis.fill(blue)
                # display of 'game over' window
                mesg = intermediate_font.render('GAME OVER', True, red)
                dis.blit(mesg, [190, 100])
                C = medium_font.render('Press C to continue playing ', True, red)
                dis.blit(C, [150, 300])
                back = medium_font.render('Back', True, red)
                back_rect = back.get_rect()
                back_rect.center = (570, 20)
                dis.blit(back, back_rect)

                Your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if x > back_rect.left and x < back_rect.right:
                            if y > back_rect.top and y < back_rect.bottom:
                                snakeGame()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    # movement of snake using keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
                        # creating back button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > back_rect.left and x < back_rect.right:
                        if y > back_rect.top and y < back_rect.bottom:
                            snakeGame()
                # condition to lose game
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <= 40:
                game_close = True
                pygame.mixer.music.load('lost.mp3')
                pygame.mixer.music.play(0)
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.circle(dis, red, (foodx, foody), 7)
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:  # another situation to lose game
                if x == snake_Head:
                    game_close = True
                    pygame.mixer.music.load('lost.mp3')
                    pygame.mixer.music.play(0)

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
            back = medium_font.render('Back', True, red)
            back_rect = back.get_rect()
            back_rect.center = (570, 20)
            dis.blit(back, back_rect)

            pygame.display.update()
            #  condition to gain points
            if x1 == foodx and y1 == foody:
                # assigning a new position to food
                foodx = round(random.randrange(10, 590, 10))
                foody = round(random.randrange(70, 400, 10))
                Length_of_snake += 1
                # increasing the length of snake
                pygame.mixer.music.load('snake.mp3')
                pygame.mixer.music.play(0)
            # increasing the speed of the snake after a particular score
            if (Length_of_snake - 1)<5:
                speed=snake_speed
            elif (Length_of_snake - 1) < 10:
                speed = snake_speed + 5
            else:
                speed = snake_speed+15

            clock.tick(speed)
        pygame.quit()
        quit()

    start_game()
    gameLoop()

# game loop for hangman

ans = True

def hangman():
    # THE MOVIE NAMES

    list_of_movies = ["INCEPTION", 'AVATAR', 'PRESTIGE', 'MOONLIGHT', 'MATRIX', 'PARASITE', 'JOKER', 'BIRDMAN',
                      'DEADPOOL', 'AVENGERS', ]
    movie = random.choice(list_of_movies)
    response_letter = []

    # color codes

    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    # Making of the window

    breadth = 1500
    length = 800
    screen = pygame.display.set_mode((breadth, length))
    pygame.display.set_caption("Hangman(Movie Version)")

    # Buttons

    radius = 25
    space = 15
    button = []
    xco = int((breadth - (2 * radius + space) * 13) / 2)
    yco = 600
    a = 65
    for i in range(26):
        x = xco + space + ((radius * 2 + space)) * (i % 13)
        y = yco + ((i // 13) * (space + radius * 2))
        button.append([x, y, chr(a + i), True])

    # display of the result(hangman)
    def res(a):
        if a == 1:
            text = "YOU WON"
            col = green
        else:
            text = "YOU LOST"
            text2 = "THE CORRECT ANSWER WAS " + movie
            col = red
        text = font_result.render(text, 1, col)
        screen.fill(white)
        if a == 0:
            text2 = font_result_correct_answer.render(text2, 1, blue)
            screen.blit(text2, (400, 500))
        screen.blit(text, (500, 300))

        pygame.display.update()
        pygame.time.delay(2000)

    # display for hangman
    def display():
        # screen fill
        screen.fill(white)
        # title image
        screen.blit(title_image, (550, 5))
        # print image
        screen.blit(images[level], (100, 200))
        # an empty string which will be displayed
        word = ''
        for i in movie:
            if i in response_letter:
                word = word + i + " "
            else:
                word = word + "_ "
        text = font_answer.render(word, 1, black)
        screen.blit(text, (600, 200))
        for items in (button):
            x, y, letter, visibility = items
            if visibility:
                pygame.draw.circle(screen, black, (x, y), radius, 3)
                ltr = font.render(letter, 1, black)
                screen.blit(ltr, (x - ltr.get_width() / 2, y - ltr.get_height() / 2))

        pygame.display.update()

    # Hangman diagrams uploading

    level = 0
    images = []
    title_image = pygame.image.load("hangman.png")
    for i in range(7):
        diag = pygame.image.load("hangman" + str(i) + ".png")
        images.append(diag)
    images.append(diag)

    # Showing the title screen before the game start
    title = "Welcome To Hangman!!!"
    screen.fill(black)
    title = font_title_opening.render(title, 1, green)
    screen.blit(title, (100, 300))
    pygame.display.update()
    pygame.time.delay(1500)
    ans = True
    while ans:
        display()
        for response in pygame.event.get():
            if response.type == pygame.QUIT:
                ans = False
            if response.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()

                for items in button:
                    x, y, letter, visibility = items
                    distance = math.sqrt((x - mousex) ** 2 + (y - mousey) ** 2)
                    if (distance < radius):
                        items[3] = False
                        response_letter.append(letter)
                        if letter not in movie:
                            level += 1
        check = True
        for words in movie:
            if words not in response_letter:
                check = False
                break
        if check:
            var = 1
            res(var)
            break
        if level == 6:
            var = 0
            res(var)
            break
    pygame.quit()

portal()

