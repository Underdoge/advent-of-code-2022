
import pandas as pd
import pygame

def print_tail_positions(tail_positions,screen,block_size,tail_c):
    for pos in tail_positions:
        pygame.draw.rect(screen, tail_c, [pos[0], pos[1], block_size,block_size])

def rope(dir,distance):
    pygame.init()
    screen = pygame.display.set_mode()
    width, height = screen.get_size()
    res = (width -100, height -200)
    screen = pygame.display.set_mode(res)
    clock = pygame.time.Clock()
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    orange = (255, 165, 0)
    head_c = green
    start_c = blue
    tail_c = red
    speed = 60
    tail_positions = []
    milisecs = 50
    instruction = 1
    block_size = 5
    df_movements = pd.DataFrame({'dir':dir,'steps':distance})
    steps = df_movements.iloc[0]['steps']
    dist = steps
    max_steps = int(max(df_movements.steps))
    while max_steps*block_size > res[0]:
        block_size = int( block_size / 2)
    head_x = int(res[0]/2) - int((max_steps * block_size ) / 2)
    head_y = int(res[1]/2) + int((max_steps * block_size ) / 2)
    start_x = head_x
    tail_x = head_x
    start_y = head_y
    tail_y = head_y
    tail_positions.append((tail_x,tail_y))
    time = int(pygame.time.get_ticks() / milisecs)
    smallfont = pygame.font.SysFont('Anonymice Powerline', 35)
    text2 = smallfont.render(f"Press 'r' to restart, 'p' to pause or 'q' to exit ...", True, white)
    text2_x,text2_y = smallfont.size(f"Press 'r' to restart, 'p' to pause or 'q' to exit ...")
    text3 = smallfont.render(f"Press space to start...", True, white)
    text3_x,text3_y = smallfont.size(f"Press space to start...")
    text5 = smallfont.render(f"Tail steps: {len(tail_positions)}", True, white)
    text5_x,text5_y = smallfont.size(f"Tail steps: {len(tail_positions)}")
    screen.fill((65, 25, 64))
    screen.blit(text3, (res[0]/2 - (text3_x/2), res[1]-100))
    screen.blit(text5, (res[0]/2 - (text5_x/2), res[1]-700))

    key = pygame.key.get_pressed()
    running = True
    started = False
    
    while running and not key[pygame.K_q]:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            started = True
        if key[pygame.K_p]:
            if started: # pause
                started = False
            else:
                started = True

        pygame.draw.rect(screen, start_c, [start_x, start_y, block_size,block_size])
        pygame.draw.rect(screen, head_c, [head_x, head_y, block_size,block_size])   
        if int(pygame.time.get_ticks() / milisecs) > time and started:
            time = int(pygame.time.get_ticks() / milisecs)
            if key[pygame.K_r]: # restart
                tail_positions = []
                instruction = 1
                head_x = int(res[0]/2) - int((max_steps * block_size ) / 2)
                head_y = int(res[1]/2) + int((max_steps * block_size ) / 2)
                start_x = head_x
                tail_x = head_x
                start_y = head_y
                tail_y = head_y
                df_movements = pd.DataFrame({'dir':dir,'steps':distance})
                steps = df_movements.iloc[0]['steps']
                dist = steps
                time += 1
            if key[pygame.K_p]: # pause
                started = False
            if ((tail_x,tail_y) not in tail_positions):
                    tail_positions.append((tail_x,tail_y))
            if len(df_movements) == 0 and steps == dist:
                if key[pygame.K_q]: # quit
                    running = False
                screen.fill((65, 25, 64))
                pygame.draw.rect(screen, start_c, [start_x, start_y, block_size,block_size])         
                pygame.draw.rect(screen, head_c, [head_x, head_y, block_size,block_size])
                print_tail_positions(tail_positions,screen,block_size,orange)
                screen.blit(text2, (res[0]/2 - (text2_x/2), res[1]-50))
                text5 = smallfont.render(f"Tail positions: {len(tail_positions)}", True, white)
                text5_x,text5_y = smallfont.size(f"Tail positions: {len(tail_positions)}")
                screen.blit(text5, (res[0]/2 - (text5_x/2), res[1]-700))
                started = False
            else:
                if key[pygame.K_DOWN]:
                    if milisecs > 50:
                        milisecs -= 50
                if key[pygame.K_UP]:
                    milisecs += 50
                screen.fill((65, 25, 64))
                if steps == dist and len(df_movements) > 0:
                    movement = df_movements.iloc[0]
                    df_movements = df_movements.iloc[1: , :]
                    dist = movement['steps']
                    text = smallfont.render(f"{instruction}: {movement['dir']} {movement['steps']}", True, white)
                    steps = 1
                    instruction += 1
                else:
                    steps += 1

                if movement['dir'] == 'R' or movement['dir'] == 'D':
                    direction = 1
                    if movement['dir'] == 'R':
                        head_x += direction * block_size
                    else:
                        head_y += direction * block_size
                else:
                    direction = -1
                    if movement['dir'] == 'L':
                        head_x += direction * block_size
                    else:
                        head_y += direction * block_size

                pygame.draw.rect(screen, start_c, [start_x, start_y, block_size,block_size])
                pygame.draw.rect(screen, head_c, [head_x, head_y, block_size,block_size])
                print_tail_positions(tail_positions,screen,block_size,orange)
                if (tail_x < head_x - block_size):
                    tail_y = head_y
                    tail_x = head_x - block_size                        
                if (tail_x > head_x + block_size):
                    tail_y = head_y
                    tail_x = head_x + block_size
                if (tail_y < head_y - block_size):
                    tail_x = head_x
                    tail_y = head_y - block_size
                if (tail_y > head_y + block_size):
                    tail_x = head_x
                    tail_y = head_y + block_size
                pygame.draw.rect(screen, tail_c, [tail_x, tail_y, block_size,block_size])
                    
                text_x,text_y = smallfont.size(f"{instruction}: {movement['dir']} {movement['steps']}")
                screen.blit(text, (res[0]/2 - (text_x/2), res[1]-100))
                text2_x,text2_y = smallfont.size(f"Press 'r' to restart, 'p' to pause or 'q' to exit ...")
                screen.blit(text2, (res[0]/2 - (text2_x/2), res[1]-50))
                text5 = smallfont.render(f"Tail steps: {len(tail_positions)}", True, white)
                text5_x,text5_y = smallfont.size(f"Tail steps: {len(tail_positions)}")
                screen.blit(text5, (res[0]/2 - (text5_x/2), res[1]-700))
        clock.tick(speed)
        pygame.display.update()
    return len(tail_positions)


def read_head_movements(file):
    dir = []
    steps = []
    for line in open(file).readlines():
        line = line.rstrip()
        line = line.split(" ")
        dir.append(line[0])
        steps.append(int(line[1]))
    return (dir,steps)

dir,steps = read_head_movements('input9.txt')
print("Unique tail positions:",rope(dir,steps))

