class EntityRegistry:

    def __init__(self):
        self.entities = {}

    def add(self, entity):
        self.entities[entity.entity_id] = entity

    def get(self, entity_id):
        return self.entities.get(entity_id)

    def all(self):
        return list(self.entities.values())

    def snapshot(self):
        return {
            entity_id: entity.snapshot()
            for entity_id, entity in self.entities.items()
        }
