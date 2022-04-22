import pygame
import random
import os
import numpy as np

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dog VLT")

EFFECT = pygame.mixer.Sound(os.path.join("assets", "roll01.ogg"))
# to fix pic error (magick mogrify *.png)
INDY_PIC = pygame.image.load(os.path.join("assets", "blk01.png")).convert()
WINNY_PIC = pygame.image.load(os.path.join("assets", "blk02.png")).convert()
INDY2_PIC = pygame.image.load(os.path.join("assets", "blk03.png")).convert()
INDY3_PIC = pygame.image.load(os.path.join("assets", "blk04.png")).convert()
W_PIC = pygame.image.load(os.path.join("assets", "blk05.png")).convert()
I_PIC = pygame.image.load(os.path.join("assets", "blk06.png")).convert()
J_PIC = pygame.image.load(os.path.join("assets", "blk07.png")).convert()
R_PIC = pygame.image.load(os.path.join("assets", "blk08.png")).convert()
WINNY2_PIC = pygame.image.load(os.path.join("assets", "blk09.png")).convert()
WILD_PIC = pygame.image.load(os.path.join("assets", "blk10.png")).convert()
BGT = pygame.image.load(os.path.join("assets", "bgtop.png")).convert()
BGB = pygame.image.load(os.path.join("assets", "bgbottom.png")).convert()
BGL = pygame.image.load(os.path.join("assets", "bgleft.png")).convert()
BGR = pygame.image.load(os.path.join("assets", "bgright.png")).convert()
BGC = pygame.image.load(os.path.join("assets", "bgmid.png")).convert()


class Block:
    BLOCK_PIC = {
        1: W_PIC,
        2: I_PIC,
        3: J_PIC,
        4: R_PIC,
        5: INDY_PIC,
        6: WINNY_PIC,
        7: INDY2_PIC,
        8: WINNY2_PIC,
        9: INDY3_PIC,
        0: WILD_PIC
    }

    def __init__(self, x, y, pic):
        self.x = x
        self.y = y
        self.block_img = self.BLOCK_PIC[pic]

    def draw(self, window):
        window.blit(self.block_img, (self.x, self.y))

    def move(self, val):
        self.y += val


class Winners:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.w, self.h), 8)

    def move(self, val):
        self.y += val


def main():
    pygame.init()
    run = True
    spin = True
    fps = 50
    clock = pygame.time.Clock()
    cash = 25
    bet = 0
    win = 0
    count_up = 0
    count_too = 0
    last_time = 0
    win_display = 0
    spin_time = 0
    main_font = pygame.font.SysFont("comicsans", 21)
    rows = [[9, 9], [9, 9], [9, 9], [9, 9], [9, 9]]
    reel1 = []
    reel2 = []
    reel3 = []
    reel4 = []
    reel5 = []
    wins = []
    block_num = 18

    def win_test(a, b, c, d=0, e=0):
        the_win = [a, b, c, d, e]
        the_win.sort(reverse=True)
        if the_win[0] == 0:
            the_win[0] = 10
        elif 5 > the_win[0] > 0:
            the_win[0] = 1
        return the_win[0]

    def redraw_window():
        WIN.fill((0, 0, 0))
        for pics in reel1:
            pics.draw(WIN)
        for pics in reel2:
            pics.draw(WIN)
        for pics in reel3:
            pics.draw(WIN)
        for pics in reel4:
            pics.draw(WIN)
        for pics in reel5:
            pics.draw(WIN)
        WIN.blit(BGT, (0, 0))
        WIN.blit(BGB, (0, 621))
        WIN.blit(BGR, (1057, 165))
        WIN.blit(BGL, (0, 165))
        WIN.blit(BGC, (300, 165))
        WIN.blit(BGC, (490, 165))
        WIN.blit(BGC, (680, 165))
        WIN.blit(BGC, (867, 165))
        for mark in wins:
            mark.draw(WIN)
        cash_label = main_font.render(f"CREDITS {cash}", True, (255, 255, 255))
        bet_label = main_font.render(f"BET {bet}", True, (255, 255, 255))
        win_label = main_font.render(f"WIN {win_display}", True, (255, 255, 255))
        WIN.blit(cash_label, (10, 765))
        WIN.blit(bet_label, (770, 765))
        WIN.blit(win_label, (890, 765))
        pygame.display.update()

    while run:
        clock.tick(fps)
        times = pygame.time.get_ticks()
        if spin:
            EFFECT.play()
            cash -= 25
            r1 = []
            r2 = []
            r3 = []
            r4 = []
            r5 = []
            hold = []
            for i in range(5):
                rows[i] = [9, 9]

            for i in range(block_num):
                pic1 = random.randrange(0, 10)
                pic2 = random.randrange(0, 10)
                pic3 = random.randrange(0, 10)
                pic4 = random.randrange(0, 10)
                pic5 = random.randrange(0, 10)
                reel1_img = Block(119, i * -120 + 40, pic1)
                reel2_img = Block(310, i * -120 + 40, pic2)
                reel3_img = Block(500, i * -120 + 40, pic3)
                reel4_img = Block(690, i * -120 + 40, pic4)
                reel5_img = Block(878, i * -120 + 40, pic5)
                if 1 < i < 6:
                    r1.append(pic1)
                if 5 < i < 10:
                    r2.append(pic2)
                if 9 < i < 14:
                    r3.append(pic3)
                if 12 < i < 17:
                    r4.append(pic4)
                if 13 < i < 19:
                    r5.append(pic5)
                reel1.append(reel1_img)
                reel2.append(reel2_img)
                reel3.append(reel3_img)
                reel4.append(reel4_img)
                reel5.append(reel5_img)
            hold.append(r1)
            hold.append(r2)
            hold.append(r3)
            hold.append(r4)
            hold.append(r5)
            rls = np.array(hold)
            win_step = 0
            # ********** row 1 and 2 ************
            if rls[0][0] == rls[1][1] or rls[0][0] == 0 or rls[1][1] == 0:
                # *********** row 3 ************
                if rls[1][1] == rls[2][2] or rls[1][1] == 0 and rls[0][0] == rls[2][2] or rls[2][2] == 0 or \
                        rls[0][0] == 0 and rls[1][1] == 0:
                    rows[4] = [4, 3]
                    win_step += win_test(rls[0][0], rls[1][1], rls[2][2])
                    # ************ row 4 *************
                    if rls[2][2] == rls[3][1] or rls[3][1] == 0 or rls[2][2] == 0 and rls[1][1] == rls[3][1] or \
                            rls[2][2] == 0 and rls[0][2] == rls[3][1]:
                        rows[4] = [4, 4]
                        win_step += win_test(rls[0][0], rls[1][1], rls[2][2], rls[3][1]) * 2
                        # **********  row 5 ************
                        if rls[3][1] == rls[4][0] or rls[4][0] == 0:
                            rows[4] = [4, 5]
                            win_step += win_test(rls[0][0], rls[1][1], rls[2][2], rls[3][1], rls[4][0]) * 3
                win += win_step

            for i in range(4):
                win_step = 0
                # ********** row 1 and 2 ************
                if rls[0][i] == rls[1][i] or rls[0][i] == 0 or rls[1][i] == 0:
                    # *********** row 3 ************
                    if rls[1][i] == rls[2][i] or rls[1][i] == 0 and rls[0][i] == rls[2][i] or rls[2][i] == 0 or \
                            rls[0][i] == 0 and rls[1][i] == 0:
                        rows[i] = [i, 3]
                        win_step += win_test(rls[0][i], rls[1][i], rls[2][i])
                        # ************ row 4 *************
                        if rls[2][i] == rls[3][i] or rls[3][i] == 0 or rls[2][i] == 0 and rls[1][i] == rls[3][i] or \
                                rls[2][i] == 0 and rls[0][i] == rls[3][i]:
                            rows[i] = [i, 4]
                            win_step += win_test(rls[0][i], rls[1][i], rls[2][i], rls[3][i]) * 2
                            # **********  row 5 ************
                            if rls[3][i] == rls[4][i] or rls[4][i] == 0:
                                rows[i] = [i, 5]
                                win_step += win_test(rls[0][i], rls[1][i], rls[2][i], rls[3][i], rls[4][i]) * 3
                    win += win_step
            spin_time = 148
            spin = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    cash += 25
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if cash > 0:
                if spin_time == 0:
                    wins = []
                    win = 0
                    bet = 1
                    win_display = 0
                    count_up = 0
                    spin = True

        if spin_time > 100:
            for blk in reel1:
                blk.move(15)
            for blk in reel2:
                blk.move(15)
            for blk in reel3:
                blk.move(15)
            for blk in reel4:
                blk.move(15)
            for blk in reel5:
                blk.move(15)
            spin_time -= 1
        elif spin_time > 68:
            for blk in reel2:
                blk.move(15)
            for blk in reel3:
                blk.move(15)
            for blk in reel4:
                blk.move(15)
            for blk in reel5:
                blk.move(15)
            spin_time -= 1
        elif spin_time > 36:
            for blk in reel3:
                blk.move(15)
            for blk in reel4:
                blk.move(15)
            for blk in reel5:
                blk.move(15)
            spin_time -= 1
        elif spin_time > 12:
            for blk in reel4:
                blk.move(15)
            for blk in reel5:
                blk.move(15)
            spin_time -= 1
        elif spin_time > 0:
            for blk in reel5:
                blk.move(10)
            if spin_time == 1:
                for played in reel1[:]:
                    if played.y > HEIGHT:
                        reel1.remove(played)
                for played in reel2[:]:
                    if played.y > HEIGHT:
                        reel2.remove(played)
                for played in reel3[:]:
                    if played.y > HEIGHT:
                        reel3.remove(played)
                for played in reel4[:]:
                    if played.y > HEIGHT:
                        reel4.remove(played)
                for played in reel5[:]:
                    if played.y > HEIGHT:
                        reel5.remove(played)
                for m in rows:
                    if m[0] == 0:
                        if m[1] == 3:
                            winny = Winners(119, 520, 562, 120)
                            wins.append(winny)
                        elif m[1] == 4:
                            winny = Winners(119, 520, 753, 120)
                            wins.append(winny)
                        elif m[1] == 5:
                            winny = Winners(119, 520, 939, 120)
                            wins.append(winny)
                    if m[0] == 1:
                        if m[1] == 3:
                            winny = Winners(119, 400, 562, 120)
                            wins.append(winny)
                        elif m[1] == 4:
                            winny = Winners(119, 400, 753, 120)
                            wins.append(winny)
                        elif m[1] == 5:
                            winny = Winners(119, 400, 939, 120)
                            wins.append(winny)
                    if m[0] == 2:
                        if m[1] == 3:
                            winny = Winners(119, 280, 562, 120)
                            wins.append(winny)
                        elif m[1] == 4:
                            winny = Winners(119, 280, 753, 120)
                            wins.append(winny)
                        elif m[1] == 5:
                            winny = Winners(119, 280, 939, 120)
                            wins.append(winny)
                    if m[0] == 3:
                        if m[1] == 3:
                            winny = Winners(119, 160, 562, 120)
                            wins.append(winny)
                        elif m[1] == 4:
                            winny = Winners(119, 160, 753, 120)
                            wins.append(winny)
                        elif m[1] == 5:
                            winny = Winners(119, 160, 939, 120)
                            wins.append(winny)
                    if m[0] == 4:
                        if m[1] == 3:
                            winny = Winners(119, 520, 180, 120)
                            wins.append(winny)
                            winny = Winners(310, 400, 180, 120)
                            wins.append(winny)
                            winny = Winners(500, 280, 180, 120)
                            wins.append(winny)
                        elif m[1] == 4:
                            winny = Winners(119, 520, 180, 120)
                            wins.append(winny)
                            winny = Winners(310, 400, 180, 120)
                            wins.append(winny)
                            winny = Winners(500, 280, 180, 120)
                            wins.append(winny)
                            winny = Winners(690, 400, 180, 120)
                            wins.append(winny)
                        elif m[1] == 5:
                            winny = Winners(119, 520, 180, 120)
                            wins.append(winny)
                            winny = Winners(310, 400, 180, 120)
                            wins.append(winny)
                            winny = Winners(500, 280, 180, 120)
                            wins.append(winny)
                            winny = Winners(690, 400, 180, 120)
                            wins.append(winny)
                            winny = Winners(878, 520, 180, 120)
                            wins.append(winny)
                EFFECT.stop()
                count_too = win * 25 * bet
                for i in range(4):
                    rows[i] = [0, 0]
            spin_time -= 1
        if times > last_time + 10:
            if count_up < count_too:
                count_up += 1
                win_display = count_up
                cash += 1
            else:
                count_too = 0
            last_time = times

        redraw_window()


main()
