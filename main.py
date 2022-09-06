import pygame as pg

DIM = [1000, 700]
vec3 = pg.Vector3




if __name__ == '__main__':
    disp = pg.display.set_mode(DIM)

    running = 1
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = 0

        disp.fill((0,0,0))





        pg.display.update()        

    pass
