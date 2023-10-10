import pygame as p

WIDTH, HEIGHT = 900, 500
WIN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("F")

white = (255, 255, 255)

def main():
    
    run = True
    while run:
        
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
        WIN.fill(white)
        p.display.update()
    
    

    p.quit(white)
    
    

main()