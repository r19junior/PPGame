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
        self.ui_font = AssetLoader.get_font(Theme.FONT_MAIN, Theme.FONT_SIZE_UI)
        self.small_font = AssetLoader.get_font(Theme.FONT_MAIN, Theme.FONT_SIZE_SMALL)
        
        # UI Layout (Native 320x180)
        btn_w, btn_h = 60, 16
        gap = 10
        total_w = (btn_w * 2) + gap
        start_x = GAME_RES[0]//2 - total_w//2
        
        self.start_btn = Button(start_x, 110, btn_w, btn_h, "START", 
                               lambda: self.manager.switch_to(AdventureScene(self.manager)))
        
        self.lb_btn = Button(start_x + btn_w + gap, 110, btn_w, btn_h, "LEADERBOARD", 
                               lambda: print("Leaderboard clicked"))
        self.time = 0

    def update(self, dt):
        self.time += dt

    def handle_events(self, events):
        for event in events:
            self.start_btn.handle_event(event)
            self.lb_btn.handle_event(event)

    def draw(self, screen):
        screen.fill(Theme.BACKGROUND)
        
        # 1. Decorations - Header
        # Dead Smiley (Top Left)
        self._draw_dead_smiley(screen, (30, 20))
        
        # Text Box (Top Center)
        msg = "YOU ONLY GET ONE LIFE. WORK HARD PLAY HARD. LIVE IT TO THE MAX"
        self._draw_text_box(screen, msg, (90, 15), 140)
        
        # Audio Indicator (Top Right)
        audio_text = self.small_font.render("AUDIO ON", True, Theme.SECONDARY)
        screen.blit(audio_text, (GAME_RES[0] - 60, 15))

        # 2. Decorations - Globe (Right)
        self._draw_wireframe_globe(screen, (GAME_RES[0] - 60, 70), 30)

        # 3. Decorations - Footer
        pygame.draw.rect(screen, Theme.SECONDARY, (20, GAME_RES[1] - 25, GAME_RES[0] - 40, 1), 1)
        meta_text = self.small_font.render("6/21/24  +  TELETECH  +  MRV0.3", True, Theme.SECONDARY)
        screen.blit(meta_text, (GAME_RES[0]//2 - meta_text.get_width()//2, GAME_RES[1] - 20))

        # 4. Title
        title_text = "< TELETECH INRAVERS />"
        title_surf = self.title_font.render(title_text, True, Theme.PRIMARY)
        title_pos = (GAME_RES[0]//2 - title_surf.get_width()//2, 70)
        screen.blit(title_surf, title_pos)
        
        # 5. Buttons
        self.start_btn.draw(screen)
        self.lb_btn.draw(screen)

        # 6. FX - Scanlines
        flicker = (pygame.time.get_ticks() // 50) % 2 == 0
        alpha = 10 if flicker else 5
        for y in range(0, GAME_RES[1], 2):
            pygame.draw.line(screen, (5, 0, alpha), (0, y), (GAME_RES[0], y))

    def _draw_dead_smiley(self, screen, pos):
        x, y = pos
        pygame.draw.circle(screen, Theme.PRIMARY, (x, y), 15, 1)
        # Eyes X X
        pygame.draw.line(screen, Theme.PRIMARY, (x-6, y-6), (x-2, y-2), 1)
        pygame.draw.line(screen, Theme.PRIMARY, (x-2, y-6), (x-6, y-2), 1)
        pygame.draw.line(screen, Theme.PRIMARY, (x+2, y-6), (x+6, y-2), 1)
        pygame.draw.line(screen, Theme.PRIMARY, (x+6, y-6), (x+2, y-2), 1)
        # Mouth
        pygame.draw.arc(screen, Theme.PRIMARY, (x-8, y, 16, 8), 3.14, 0, 1)

    def _draw_text_box(self, screen, text, pos, width):
        x, y = pos
        # Wrap text manually if needed, but here we just render small
        words = text.split()
        lines = []
        curr_line = ""
        for word in words:
            test_line = curr_line + word + " "
            if self.small_font.size(test_line)[0] < width - 10:
                curr_line = test_line
            else:
                lines.append(curr_line)
                curr_line = word + " "
        lines.append(curr_line)

        h = len(lines) * 10 + 10
        pygame.draw.rect(screen, Theme.PRIMARY, (x, y, width, h), 1, border_radius=5)
        
        for i, line in enumerate(lines):
            surf = self.small_font.render(line.strip(), True, Theme.SECONDARY)
            screen.blit(surf, (x + 5, y + 5 + i * 10))

    def _draw_wireframe_globe(self, screen, pos, radius):
        x, y = pos
        pygame.draw.circle(screen, Theme.SECONDARY, pos, radius, 1)
        # Vertical ellipses
        for i in range(1, 4):
            r_w = radius * (i / 3)
            pygame.draw.ellipse(screen, Theme.SECONDARY, (x - r_w, y - radius, r_w * 2, radius * 2), 1)
        # Horizontal lines
        for i in range(-2, 3):
            h_y = y + (i * (radius / 3))
            w = (radius**2 - (h_y - y)**2)**0.5 if radius**2 > (h_y - y)**2 else 0
            pygame.draw.line(screen, Theme.SECONDARY, (x - w, h_y), (x + w, h_y), 1)
