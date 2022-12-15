
import pandas as pd
import pygame
import math

def print_tail_positions(tail_positions,screen,block_size,tail_c):
    for pos in tail_positions:
        pygame.draw.rect(screen, tail_c, [pos[0], pos[1], block_size,block_size])

def rope_part2(dir,distance):
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
    yellow = (255, 255, 0)
    orange = (255, 165, 0)
    violet = (148, 0, 211)
    head_c = green
    start_c = blue
    tail_c = red
    speed = 60
    knots_num = 10
    tail_positions = []
    knots= []
    milisecs = 50
    instruction = 1
    block_size = 5
    df_movements = pd.DataFrame({'dir':dir,'steps':distance})
    steps = df_movements.iloc[0]['steps']
    dist = steps
    max_steps = int(max(df_movements.steps))
    while max_steps*block_size > res[0]:
        block_size = int( block_size / 2)
    head_x = round(int(res[0]/2) - int((max_steps * block_size ) / 2),-2)
    head_y = round(int(res[1]/2) + int((max_steps * block_size ) / 2),-2)
    start_x = head_x
    start_y = head_y
    for i in range(knots_num):
        knots.append([head_x,head_y])
    tail_positions.append((knots[9][0],knots[9][1]))
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
         
        if int(pygame.time.get_ticks() / milisecs) > time and started:
            time = int(pygame.time.get_ticks() / milisecs)
            if key[pygame.K_r]: # restart
                tail_positions = []
                knots= []
                instruction = 1
                head_x = round(int(res[0]/2) - int((max_steps * block_size ) / 2),-2)
                head_y = round(int(res[1]/2) + int((max_steps * block_size ) / 2),-2)
                start_x = head_x
                start_y = head_y
                for i in range(knots_num):
                    knots.append([head_x,head_y])
                df_movements = pd.DataFrame({'dir':dir,'steps':distance})
                steps = df_movements.iloc[0]['steps']
                dist = steps
                time += 1
            if key[pygame.K_p]: # pause
                started = False
            if ((knots[9][0],knots[9][1]) not in tail_positions):
                tail_positions.append((knots[9][0],knots[9][1]))
            if len(df_movements) == 0 and steps == dist:
                if key[pygame.K_q]: # quit
                    running = False
                screen.fill((65, 25, 64))
                pygame.draw.rect(screen, start_c, [start_x, start_y, block_size,block_size])         
                pygame.draw.rect(screen, head_c, [knots[0][0], knots[0][1], block_size,block_size])
                print_tail_positions(tail_positions,screen,block_size,orange)
                for i in range(1,knots_num):
                    if (math.dist([knots[i][0],knots[i][1]],[knots[i-1][0],knots[i-1][1]]) > 14):
                        if knots[i][0] < knots[i-1][0]:
                            knots[i][0] += int(abs(knots[i][0] - knots[i-1][0])/2)
                        if knots[i][0] > knots[i-1][0]:
                            knots[i][0] -= int(abs(knots[i][0] - knots[i-1][0])/2)
                        if knots[i][1] < knots[i-1][1]:
                            knots[i][1] += int(abs(knots[i][1] - knots[i-1][1])/2)
                        if knots[i][1] > knots[i-1][1]:
                            knots[i][1] -= int(abs(knots[i][1] - knots[i-1][1])/2)
                    else:
                        if (knots[i][0] < knots[i-1][0] - block_size):
                            knots[i][0] = knots[i-1][0] - block_size
                            if knots[i][1] != knots[i-1][1]:
                                knots[i][1] = knots[i-1][1]
                        if (knots[i][0] > knots[i-1][0] + block_size):
                            knots[i][1] = knots[i-1][1]
                            knots[i][0] = knots[i-1][0] + block_size
                        if (knots[i][1] < knots[i-1][1] - block_size):
                            knots[i][0] = knots[i-1][0]
                            knots[i][1] = knots[i-1][1] - block_size
                        if (knots[i][1] > knots[i-1][1] + block_size):
                            knots[i][0] = knots[i-1][0]
                            knots[i][1] = knots[i-1][1] + block_size
                    if (i == 8):
                        pygame.draw.rect(screen, yellow, [knots[i][0], knots[i][1], block_size,block_size])
                    elif (i == 9):
                        pygame.draw.rect(screen, violet, [knots[i][0], knots[i][1], block_size,block_size])
                    else:
                        pygame.draw.rect(screen, tail_c, [knots[i][0], knots[i][1], block_size,block_size])
                if ((knots[9][0],knots[9][1]) not in tail_positions):
                    tail_positions.append((knots[9][0],knots[9][1]))
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
                        knots[0][0] += direction * block_size
                    else:
                        knots[0][1] += direction * block_size
                else:
                    direction = -1
                    if movement['dir'] == 'L':
                        knots[0][0] += direction * block_size
                    else:
                        knots[0][1] += direction * block_size

                pygame.draw.rect(screen, start_c, [start_x, start_y, block_size,block_size])
                pygame.draw.rect(screen, head_c, [knots[0][0], knots[0][1], block_size,block_size])
                print_tail_positions(tail_positions,screen,block_size,orange)
                for i in range(1,knots_num):
                    if (math.dist([knots[i][0],knots[i][1]],[knots[i-1][0],knots[i-1][1]]) > 14):
                        if knots[i][0] < knots[i-1][0]:
                            knots[i][0] += int(abs(knots[i][0] - knots[i-1][0])/2)
                        if knots[i][0] > knots[i-1][0]:
                            knots[i][0] -= int(abs(knots[i][0] - knots[i-1][0])/2)
                        if knots[i][1] < knots[i-1][1]:
                            knots[i][1] += int(abs(knots[i][1] - knots[i-1][1])/2)
                        if knots[i][1] > knots[i-1][1]:
                            knots[i][1] -= int(abs(knots[i][1] - knots[i-1][1])/2)
                    #    knots[i] = knots[i-1]
                    else:
                        if (knots[i][0] < knots[i-1][0] - block_size):
                            knots[i][0] = knots[i-1][0] - block_size
                            if knots[i][1] != knots[i-1][1]:
                                knots[i][1] = knots[i-1][1]
                        if (knots[i][0] > knots[i-1][0] + block_size):
                            knots[i][1] = knots[i-1][1]
                            knots[i][0] = knots[i-1][0] + block_size
                        if (knots[i][1] < knots[i-1][1] - block_size):
                            knots[i][0] = knots[i-1][0]
                            knots[i][1] = knots[i-1][1] - block_size
                        if (knots[i][1] > knots[i-1][1] + block_size):
                            knots[i][0] = knots[i-1][0]
                            knots[i][1] = knots[i-1][1] + block_size
                    if (i == 8):
                        pygame.draw.rect(screen, yellow, [knots[i][0], knots[i][1], block_size,block_size])
                    elif (i == 9):
                        pygame.draw.rect(screen, violet, [knots[i][0], knots[i][1], block_size,block_size])
                    else:
                        pygame.draw.rect(screen, tail_c, [knots[i][0], knots[i][1], block_size,block_size])
                    
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

def rope_part2_simple(dir,distance):
    knots_num = 10
    tail_positions = []
    knots= []
    df_movements = pd.DataFrame({'dir':dir,'steps':distance})
    steps = df_movements.iloc[0]['steps']
    dist = steps
    head_x = 0
    head_y = 0
    for i in range(knots_num):
        knots.append([head_x,head_y])
    tail_positions.append(str((head_x,head_y)))
    while len(df_movements) >= 0 and steps <= dist:
        if (str((knots[9][0],knots[9][1])) not in tail_positions):
            tail_positions.append(str((knots[9][0],knots[9][1])))
        if steps == dist and len(df_movements) > 0:
            movement = df_movements.iloc[0]
            df_movements = df_movements.iloc[1: , :]
            dist = movement['steps']
            steps = 1
        else:
            steps += 1
        if movement['dir'] == 'R' or movement['dir'] == 'U':
            direction = 1
            if movement['dir'] == 'R':
                knots[0][0] += direction
            else:
                knots[0][1] += direction
        else:
            direction = -1
            if movement['dir'] == 'L':
                knots[0][0] += direction
            else:
                knots[0][1] += direction
        for i in range(1,knots_num):
            if (math.dist([knots[i][0],knots[i][1]],[knots[i-1][0],knots[i-1][1]]) > 2.8):
                if knots[i][0] < knots[i-1][0]:
                    knots[i][0] += int(abs(knots[i][0] - knots[i-1][0])/2)
                if knots[i][0] > knots[i-1][0]:
                    knots[i][0] -= int(abs(knots[i][0] - knots[i-1][0])/2)
                if knots[i][1] < knots[i-1][1]:
                    knots[i][1] += int(abs(knots[i][1] - knots[i-1][1])/2)
                if knots[i][1] > knots[i-1][1]:
                    knots[i][1] -= int(abs(knots[i][1] - knots[i-1][1])/2)
            else:
                if (knots[i][0] < knots[i-1][0] - 1):
                    knots[i][0] = knots[i-1][0] - 1
                    if knots[i][1] != knots[i-1][1]:
                        knots[i][1] = knots[i-1][1]
                if (knots[i][0] > knots[i-1][0] + 1):
                    knots[i][1] = knots[i-1][1]
                    knots[i][0] = knots[i-1][0] + 1
                if (knots[i][1] < knots[i-1][1] - 1):
                    knots[i][0] = knots[i-1][0]
                    knots[i][1] = knots[i-1][1] - 1
                if (knots[i][1] > knots[i-1][1] + 1):
                    knots[i][0] = knots[i-1][0]
                    knots[i][1] = knots[i-1][1] + 1
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
print("Unique tail positions:",rope_part2(dir,steps))
