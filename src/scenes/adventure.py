import pygame
from src.core.constants import GAME_RES
from src.core.scene_base import Scene
from src.core.assets import AssetLoader
from src.ui.theme import Theme

class AdventureScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        self.font_main = AssetLoader.get_font(Theme.FONT_MAIN, Theme.FONT_SIZE_TITLE)
        self.font_small = AssetLoader.get_font(Theme.FONT_MAIN, Theme.FONT_SIZE_SMALL)

    def draw(self, screen):
        screen.fill((40, 60, 40)) # Jungle Green
        
        text = self.font_main.render("Exploring World...", True, Theme.TEXT)
        screen.blit(text, (GAME_RES[0]//2 - text.get_width()//2, GAME_RES[1]//2))
        
        back_text = self.font_small.render("Press ESC for Menu", True, (150, 150, 150))
        screen.blit(back_text, (10, GAME_RES[1] - 20))

    def handle_events(self, events):
        from src.scenes.menu import MenuScene # Local import
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.switch_to(MenuScene(self.manager))
