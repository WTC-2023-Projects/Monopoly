import pygame as p

WIDTH, HEIGHT = 900, 500
WIN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("F")

white = (255, 255, 255)
FPS = 60

def draw_window():
    WIN.fill(white)
    p.display.update()
    
    
def main():
    clock = p.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
        
        draw_window()
    
    p.quit(white)
    
    

main()