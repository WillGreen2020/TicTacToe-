import pygame as pg

pg.init()
CLOCK = pg.time.Clock()
WIN = pg.display.set_mode((399, 399))
pg.display.set_caption("Tic Tac Toe")
pg.display.set_icon(pg.image.load('icon.png'))

FPS = 60
scale = 133
player1 = 'X'
player2 = "O"

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def main():        
    currentPlayer = player1
    RUN = True
    while RUN:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUN = False
                pg.quit()
                raise SystemExit

            for i in range(3):
                for j in range(3):
                    spot = board[j][i]
                    if pg.draw.rect(WIN, 'white', (scale * i, scale * j, scale, scale), 0).collidepoint(pg.mouse.get_pos()):
                        if pg.mouse.get_pressed()[0]:
                            if board[j][i] != 'X' and board[j][i] != 'O':
                                board[j][i] = currentPlayer
                                if currentPlayer == 'X':
                                    currentPlayer = 'O'
                                else:
                                    currentPlayer = 'X'
       
        WIN.fill('white')
        for i in range(3):
            for j in range(3):
                spot = board[j][i]
                pg.draw.rect(WIN, 'black', (scale * i, scale * j, scale, scale), 1)
                if spot == player1:
                    pg.draw.line(WIN, 'black', (scale * i, scale * j), (scale * (i + 1), scale * (j + 1)), width=4)
                    pg.draw.line(WIN, 'black', (scale * i, scale * (j + 1)), (scale * (i + 1), scale * j), width=4)
                elif spot == player2:
                    pg.draw.ellipse(WIN, "black", (scale * i, scale * j, scale, scale), 3)
        pg.display.flip()

        CLOCK.tick(FPS)

if __name__ == "__main__":
    main()
