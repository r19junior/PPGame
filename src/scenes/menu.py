import pygame
import sys
from src.core.constants import GAME_RES
from src.core.scene_base import Scene
from src.core.assets import AssetLoader
from src.ui.theme import Theme
from src.ui.button import Button
from src.scenes.adventure import AdventureScene

class MenuScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        self.title_font = AssetLoader.get_font(Theme.FONT_MAIN, Theme.FONT_SIZE_TITLE)
        
        # UI Layout
        btn_w, btn_h = 80, 24
        cx = GAME_RES[0]//2 - btn_w//2
        
        self.start_btn = Button(cx, 80, btn_w, btn_h, "START", 
                               lambda: self.manager.switch_to(AdventureScene(self.manager)))
        
        self.exit_btn = Button(cx, 110, btn_w, btn_h, "QUIT", 
                              lambda: (pygame.quit(), sys.exit()))

    def handle_events(self, events):
        for event in events:
            self.start_btn.handle_event(event)
            self.exit_btn.handle_event(event)

    def draw(self, screen):
        screen.fill(Theme.BACKGROUND)
        
        # Render Title with a small shadow for "Jam quality"
        title_surf = self.title_font.render("PIXEL QUEST", True, Theme.PRIMARY)
        shadow_surf = self.title_font.render("PIXEL QUEST", True, (0, 0, 0))
        
        title_pos = (GAME_RES[0]//2 - title_surf.get_width()//2, 30)
        screen.blit(shadow_surf, (title_pos[0]+1, title_pos[1]+1))
        screen.blit(title_surf, title_pos)
        
        self.start_btn.draw(screen)
        self.exit_btn.draw(screen)
