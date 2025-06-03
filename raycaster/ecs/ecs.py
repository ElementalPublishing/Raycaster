from typing import Type, Dict, Any, List

class Component:
    """Base class for all components."""
    pass

class Entity:
    _next_id = 1

    def __init__(self):
        self.id = Entity._next_id
        Entity._next_id += 1
        self.components: Dict[Type[Component], Component] = {}

    def add(self, component: Component):
        self.components[type(component)] = component

    def get(self, component_type: Type[Component]) -> Any:
        return self.components.get(component_type)

    def has(self, component_type: Type[Component]) -> bool:
        return component_type in self.components

class System:
    """Base class for all systems."""
    def update(self, entities: List[Entity]):
        raise NotImplementedError

class World:
    def __init__(self):
        self.entities: List[Entity] = []
        self.systems: List[System] = []

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def add_system(self, system: System):
        self.systems.append(system)

    def update(self):
        for system in self.systems:
            system.update(self.entities)