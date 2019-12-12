import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the decimal value for ship's horizonal position
        self.x = float(self.rect.x)
        # Movement flag
        self.move_right = False
        self.move_left = False
    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update ship's x value, not the rect value
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left >0:
            self.x -= self.settings.ship_speed
        # Update rect object
        self.rect.x = self.x
