import pygame
from core.constants import GAME_RES, COLOR_TEXT
from core.scene_base import Scene

class AdventureScene(Scene):
    def draw(self, screen):
        screen.fill((40, 60, 40)) # Jungle Green
        font = pygame.font.SysFont("monospace", 16, bold=True)
        text = font.render("Exploring World...", True, COLOR_TEXT)
        screen.blit(text, (GAME_RES[0]//2 - text.get_width()//2, GAME_RES[1]//2))
        
        back_font = pygame.font.SysFont("monospace", 10)
        back_text = back_font.render("Press ESC for Menu", True, (150, 150, 150))
        screen.blit(back_text, (10, GAME_RES[1] - 20))

    def handle_events(self, events):
        from scenes.menu import MenuScene # Local import to avoid circular dependency
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.switch_to(MenuScene(self.manager))
