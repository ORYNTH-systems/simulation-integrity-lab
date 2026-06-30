from dataclasses import dataclass


@dataclass
class ResourceClaim:
    resource_id: str
    available: bool = True

    def admissible(self):
        return self.available
