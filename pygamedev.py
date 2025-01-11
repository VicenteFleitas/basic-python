import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))

mario_image = pygame.image.load('mario.png').convert_alpha()
# mario_image = pygame.transform.scale(
#     mario_image, 
#     (mario_image.get_width() * 2, mario_image.get_height() * 2)
# )
running = True
x = 10
clock = pygame.time.Clock()

delta_time =  0.1

font = pygame.font.Font(None, size=30)
moving = False

sound = pygame.mixer.Sound('beep.mp3')

while running:
    screen.fill((255, 255, 255))
    screen.blit(mario_image, (x,10))

    if moving:
        x += 50 * delta_time

    text = font.render("Hello world!", True, (0,0,0))
    screen.blit(text, (300,290))

    hitbox = pygame.Rect(x, 30, mario_image.get_width(), mario_image.get_height())

    mpos = pygame.mouse.get_pos()

    target = pygame.Rect(300, 0, 160, 280)
    collision = hitbox.colliderect(target)
    m_collision = target.collidepoint(mpos)
    pygame.draw.rect(screen, (255 * collision, 255 * m_collision, 0), target)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving = True
            if event.key == pygame.K_f:
                sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving = False

    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()