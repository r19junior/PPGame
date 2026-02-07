import pygame
import sys
from src.core.constants import GAME_RES, WINDOW_RES, FPS, SCALE
from src.core.scene_base import SceneManager
from src.scenes.menu import MenuScene

def main():
    """
    Main Game Loop & Initialization.
    Optimized for Global Game Jam performance.
    """
    pygame.init()
    
    # Initialization
    window = pygame.display.set_mode(WINDOW_RES)
    pygame.display.set_caption("GGJ Template - Pixel Adventure")
    display = pygame.Surface(GAME_RES)
    clock = pygame.time.Clock()
    
    # Scene Logic
    manager = SceneManager(MenuScene)
    
    running = True
    while running:
        # 1. Timing
        dt = clock.tick(FPS) / 1000.0
        
        # 2. Events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        # 3. Logic & Update
        manager.handle_events(events)
        manager.update(dt)
        
        # 4. Drawing
        manager.draw(display)
        
        # 5. Scaling (Pixel Perfect)
        scaled_display = pygame.transform.scale(display, WINDOW_RES)
        window.blit(scaled_display, (0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
