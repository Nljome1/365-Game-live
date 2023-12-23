import pygame
import sys
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("射击小游戏")

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 玩家
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - 2 * player_size
player_speed = 10

# 子弹
bullet_size = 10
bullet_speed = 15
bullets = []

# 敌人
enemy_size = 50
enemy_speed = 5
enemies = []

# 计分
score = 0
font = pygame.font.Font(None, 36)

# 游戏主循环
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = {
                    'x': player_x + player_size // 2 - bullet_size // 2,
                    'y': player_y,
                }
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # 移动子弹
    for bullet in bullets:
        bullet['y'] -= bullet_speed

    # 移动敌人
    for enemy in enemies:
        enemy['y'] += enemy_speed
        if enemy['y'] > screen_height:
            enemies.remove(enemy)
            score += 1

    # 生成新的敌人
    if random.randint(1, 20) == 1:
        enemy = {'x': random.randint(0, screen_width - enemy_size), 'y': 0}
        enemies.append(enemy)

    # 检测碰撞
    for enemy in enemies:
        for bullet in bullets:
            if (
                bullet['x'] < enemy['x'] + enemy_size
                and bullet['x'] + bullet_size > enemy['x']
                and bullet['y'] < enemy['y'] + enemy_size
                and bullet['y'] + bullet_size > enemy['y']
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10

    # 绘制背景
    screen.fill(black)

    # 绘制玩家
    pygame.draw.rect(screen, white, [player_x, player_y, player_size, player_size])

    # 绘制子弹
    for bullet in bullets:
        pygame.draw.rect(screen, white, [bullet['x'], bullet['y'], bullet_size, bullet_size])

    # 绘制敌人
    for enemy in enemies:
        pygame.draw.rect(screen, red, [enemy['x'], enemy['y'], enemy_size, enemy_size])

    # 绘制得分
    score_text = font.render("得分: " + str(score), True, white)
    screen.blit(score_text, [10, 10])

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(30)

# 退出游戏
pygame.quit()
sys.exit()
