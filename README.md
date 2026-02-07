# 🚀 Global Game Jam Pygame Template

Este es un template profesional diseñado para competencias de desarrollo de juegos (Game Jams) y proyectos escalables. Combina una arquitectura modular con optimizaciones de rendimiento y una estética pixel-art "perfecta".

## 📁 Estructura del Proyecto

```text
/
├── main.py              # Punto de entrada principal (Loop de juego)
├── assets/              # Carpeta para recursos externos
│   ├── fonts/           # Tipografías (.ttf)
│   ├── images/          # Sprites y Backgrounds (.png)
│   └── sounds/          # SFX y Música (.wav, .mp3)
└── src/                 # Código fuente organizado
    ├── core/            # Núcleo del motor
    │   ├── assets.py    # Gestor de carga inteligente (AssetLoader)
    │   ├── constants.py # Ajustes globales y resoluciones
    │   └── scene_base.py# Clase base para niveles y pantallas
    ├── ui/              # Componentes de interfaz
    │   ├── button.py    # Botones interactivos con hover
    │   └── theme.py     # Sistema de estilos y colores globales
    └── scenes/          # Definición de niveles y menús
        ├── menu.py      # Lógica del menú principal
        └── adventure.py # Lógica de la pantalla de juego
```

## 🛠️ Cómo Utilizar este Template

### 1. Añadir Assets
Coloca tus archivos en la carpeta `assets/`. El `AssetLoader` se encarga de:
- Pre-cargar recursos.
- Evitar lecturas de disco repetitivas.
- Proporcionar un **fallback magenta** si un archivo no existe, para que el juego nunca se rompa en pleno concurso.

### 2. Cambiar la Estética
Edita `src/ui/theme.py`. Puedes cambiar la paleta de colores de todo el juego instantáneamente, lo cual es vital para adaptarse a la temática secreta de una Game Jam.

### 3. Crear Nuevas Escenas
1. Crea un archivo en `src/scenes/mi_nivel.py`.
2. Hereda de `Scene` y define `draw`, `update` y `handle_events`.
3. Usa `self.manager.switch_to(NuevClase(self.manager))` para cambiar de pantalla.

## 🤖 Información para IAs (Developer Note)
- **Escalado**: El juego usa una resolución nativa de 320x180. Al dibujar, hazlo pensando en estas coordenadas. El motor escala automáticamente a 1280x720 (4x).
- **Imports**: Para evitar dependencias circulares, importa las clases de escenas *dentro* de las funciones o métodos si es necesario (ej: en `handle_events`).
- **Assets**: Usa siempre `AssetLoader.get_image()` o `AssetLoader.get_font()` para asegurar la compatibilidad y los fallbacks.

## 🏁 Requisitos
- Python 3.x
- Pygame (`pip install pygame`)

---
*Diseñado para la velocidad. Construido para ganar.*
