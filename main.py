import pygame as pg


DIM = (30*10, 30*10)
TILESIZE = (30, 30)



class Game():
    def __init__(self) -> None:
        pg.init()
        self.disp = pg.display.set_mode(DIM)
        self.mainloop()
        pass

    
    def setup(self):

        pass


    def mainloop(self):
        while True:
            self.disp.fill((100, 100, 100))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()


            





            pg.display.update()

    



    def quit(self):
        pg.quit()
        quit()


if __name__ == '__main__':
    Game()