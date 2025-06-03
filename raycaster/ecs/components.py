from .ecs import Component

class Position(Component):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Health(Component):
    def __init__(self, hp: int):
        self.hp = hp

class Velocity(Component):
    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

# Add more components as needed (Renderable, Inventory, etc.)