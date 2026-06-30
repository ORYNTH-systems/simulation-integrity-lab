from dataclasses import dataclass


@dataclass
class Authority:
    level: str = "standard"
    active: bool = True

    def admissible(self):
        return self.active
