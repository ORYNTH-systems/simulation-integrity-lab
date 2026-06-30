from dataclasses import dataclass


@dataclass
class Intent:
    action: str
    allowed: bool = True

    def admissible(self):
        return self.allowed
