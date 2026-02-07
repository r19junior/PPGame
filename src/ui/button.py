import pygame
from src.core.constants import SCALE
from src.ui.theme import Theme
from src.core.assets import AssetLoader

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.is_hovered = False
        self.font = AssetLoader.get_font(Theme.FONT_MAIN, Theme.FONT_SIZE_UI)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            mx, my = event.pos
            mx //= SCALE
            my //= SCALE
            self.is_hovered = self.rect.collidepoint(mx, my)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered:
                self.callback()

    def draw(self, screen):
        # Outline Color
        color = Theme.ACCENT if self.is_hovered else Theme.PRIMARY
        
        # In the reference, buttons are transparent but have a pink outline
        # On hover, they might have a slight glow or darker pink bg
        if self.is_hovered:
            pygame.draw.rect(screen, Theme.UI_HOVER, self.rect, border_radius=1)
            
        pygame.draw.rect(screen, color, self.rect, 1, border_radius=1)
        
        text_surf = self.font.render(self.text, True, color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
