import pygame
from core.constants import SCALE, COLOR_TEXT, COLOR_BUTTON, COLOR_HIGHLIGHT, COLOR_ACCENT

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.is_hovered = False
        self.font = pygame.font.SysFont("monospace", 12, bold=True)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Scale mouse pos back to game resolution
            mx, my = event.pos
            mx //= SCALE
            my //= SCALE
            self.is_hovered = self.rect.collidepoint(mx, my)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered:
                self.callback()

    def draw(self, screen):
        color = COLOR_HIGHLIGHT if self.is_hovered else COLOR_BUTTON
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, COLOR_ACCENT, self.rect, 1) # Border
        
        text_surf = self.font.render(self.text, True, COLOR_TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
