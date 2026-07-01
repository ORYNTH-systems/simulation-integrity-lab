from dataclasses import dataclass


@dataclass
class Delegation:
    delegation_id: str
    delegator_id: str
    delegatee_id: str
    authority_scope: str
    active: bool = True
    expires_at_tick: int | None = None

    def valid_at(self, tick):
        if not self.active:
            return False

        if self.expires_at_tick is not None and tick > self.expires_at_tick:
            return False

        return True
