import pygame

class Scene:
    def __init__(self, manager):
        self.manager = manager
    def handle_events(self, events): pass
    def update(self, dt): pass
    def draw(self, screen): pass

class SceneManager:
    def __init__(self, initial_scene_class):
        self.scene = initial_scene_class(self)
    
    def switch_to(self, next_scene):
        self.scene = next_scene
        
    def handle_events(self, events):
        self.scene.handle_events(events)
        
    def update(self, dt):
        self.scene.update(dt)
        
    def draw(self, screen):
        self.scene.draw(screen)
