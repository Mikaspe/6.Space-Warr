import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, style, direction='right'):
        super().__init__()

        self.style = style
        self.direction = direction
        self.hp = 1
        self.speed = 2

        self.image = pygame.image.load(f'img/enemy/enemy{self.style}.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)  # Useful for fast pixel perfect collision detection
        self.rect = self.image.get_rect(center=(pos_x, pos_y + 40))

        if style == 1:
            self.hp = 1
            self.shoot_ratio = 150
        elif style == 2:
            self.hp = 5
            self.shoot_ratio = 160
        elif style == 3:
            self.hp = 3
            self.shoot_ratio = 100
        elif style == 4:
            self.hp = 400
            self.shoot_ratio = 100
            self.speed = 4

    def move(self):
        if self.direction == 'left':
            self.rect.x -= round(self.speed)
        elif self.direction == 'right':
            self.rect.x += round(self.speed)

