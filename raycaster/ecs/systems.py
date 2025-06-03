from .ecs import System, Entity
from .components import Position, Velocity

class MovementSystem(System):
    def update(self, entities):
        for entity in entities:
            pos = entity.get(Position)
            vel = entity.get(Velocity)
            if pos and vel:
                pos.x += vel.dx
                pos.y += vel.dy

# Add more systems as needed (RenderingSystem, HealthSystem, etc.)