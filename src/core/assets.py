import pygame
import os

class AssetLoader:
    """
    Centralized utility to manage game resources.
    Prevents redundant I/O operations and provides fallbacks.
    """
    _images = {}
    _sounds = {}
    _fonts = {}

    @classmethod
    def get_image(cls, path):
        if path not in cls._images:
            if os.path.exists(path):
                cls._images[path] = pygame.image.load(path).convert_alpha()
            else:
                # Fallback: Create a magenta placeholder
                surf = pygame.Surface((16, 16))
                surf.fill((255, 0, 255))
                cls._images[path] = surf
        return cls._images[path]

    @classmethod
    def get_font(cls, name, size):
        key = f"{name}_{size}"
        if key not in cls._fonts:
            try:
                # Try loading from assets, then system
                font_path = os.path.join("assets", "fonts", name)
                if os.path.exists(font_path):
                    cls._fonts[key] = pygame.font.Font(font_path, size)
                else:
                    cls._fonts[key] = pygame.font.SysFont(name, size)
            except:
                cls._fonts[key] = pygame.font.SysFont("monospace", size)
        return cls._fonts[key]
