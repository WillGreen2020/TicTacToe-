import pygame as pg
import pygame.gfxdraw

pg.init()
pg.font.init()
CLOCK = pg.time.Clock()
WIN = pg.display.set_mode((450, 500))
pg.display.set_caption("Tic Tac Toe")
pg.display.set_icon(pg.image.load('icon.png'))
font = pg.font.Font('freesansbold.ttf', 32)


def main():
    FPS = 60
    scale = 133
    player1 = 'X'
    player2 = "O"

    board = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    currentPlayer = player1
    winner = 'TIE'
    isWin = False
    movesCounter = 0

    RUN = True
    while RUN:
        if board[0][0] == board[0][1] == board[0][2]:
                if currentPlayer == player1:
                    winner = f'Player {player2} has won!'
                else:
                    winner = f'Player {player1} has won!'
                isWin = True
        elif board[1][0] == board[1][1] == board[1][2]:
                if currentPlayer == player1:
                    winner = f'Player {player2} has won!'
                else:
                    winner = f'Player {player1} has won!'
                isWin = True
        elif board[2][0] == board[2][1] == board[2][2]:
                if currentPlayer == player1:
                    winner = f'Player {player2} has won!'
                else:
                    winner = f'Player {player1} has won!'
                isWin = True
        elif board[0][0] == board[1][1] == board[2][2]:
                if currentPlayer == player1:
                    winner = f'Player {player2} has won!'
                else:
                    winner = f'Player {player1} has won!'
                isWin = True
        elif board[0][2] == board[1][1] == board[2][0]:
                if currentPlayer == player1:
                    winner = f'Player {player2} has won!'
                else:
                    winner = f'Player {player1} has won!'
                isWin = True
        elif movesCounter == 9:
            isWin = True


        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUN = False
                pg.font.quit()
                pg.quit()
                raise SystemExit


            if event.type == pg.KEYDOWN:
                if pg.key.get_pressed()[pg.K_r]:
                    board = [
                        ['a', 'b', 'c'],
                        ['d', 'e', 'f'],
                        ['g', 'h', 'i']
                    ]
                    currentPlayer = player1
                    winner = 'TIE'
                    isWin = False
                    movesCounter = 0

                    
            if not isWin:
                for i in range(3):
                    for j in range(3):
                        if pg.draw.rect(WIN, 'white', ((scale * i) + 25, (scale * j) + 25, scale - 30, scale - 30), 0).collidepoint(pg.mouse.get_pos()):
                            if pg.mouse.get_pressed()[0]:
                                if board[j][i] != 'X' and board[j][i] != 'O':
                                    movesCounter += 1
                                    board[j][i] = currentPlayer
                                    if currentPlayer == 'X':
                                        currentPlayer = 'O'
                                    else:
                                        currentPlayer = 'X'
                text = font.render(f'Player {currentPlayer}', True, 'black')
            else:
                text = font.render(winner, True, 'black')
            textRect = text.get_rect()
            textRect.center = (450 // 2, 450)

                                   
        WIN.fill('white')
        for i in range(3):
            for j in range(3):
                spot = board[j][i]
                pg.draw.rect(WIN, 'black', ((scale * i) + 25, scale * j, scale, scale), 1)

                if spot == player1:
                    pg.draw.line(WIN, 'black', ((scale * i) + 40, (scale * j) + 15), ((scale * (i + 1)) + 10, (scale * (j + 1)) - 15), width=5)
                    pg.draw.line(WIN, 'black', ((scale * i) + 40, (scale * (j + 1)) - 15), ((scale * (i + 1)) + 10, (scale * j) + 15), width=5)
                elif spot == player2:
                    pg.draw.ellipse(WIN, "black", ((scale * i) + 40, (scale * j) + 15, scale - 30, scale - 30), 4)
        WIN.blit(text, textRect)
        pg.display.flip()


        CLOCK.tick(FPS)

if __name__ == "__main__":
    main()
