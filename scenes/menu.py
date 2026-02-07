import pygame
import sys
from core.constants import GAME_RES, COLOR_BG, COLOR_ACCENT
from core.scene_base import Scene
from ui.button import Button
from scenes.adventure import AdventureScene

class MenuScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        btn_w = 80
        btn_h = 24
        self.start_btn = Button(GAME_RES[0]//2 - btn_w//2, 80, btn_w, btn_h, "START", 
                               lambda: self.manager.switch_to(AdventureScene(self.manager)))
        self.exit_btn = Button(GAME_RES[0]//2 - btn_w//2, 110, btn_w, btn_h, "QUIT", 
                              lambda: (pygame.quit(), sys.exit()))

    def handle_events(self, events):
        for event in events:
            self.start_btn.handle_event(event)
            self.exit_btn.handle_event(event)

    def draw(self, screen):
        screen.fill(COLOR_BG)
        font = pygame.font.SysFont("monospace", 16, bold=True)
        title = font.render("PIXEL QUEST", True, COLOR_ACCENT)
        screen.blit(title, (GAME_RES[0]//2 - title.get_width()//2, 30))
        
        self.start_btn.draw(screen)
        self.exit_btn.draw(screen)
