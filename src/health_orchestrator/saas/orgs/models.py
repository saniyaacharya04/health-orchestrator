from dataclasses import dataclass
import uuid

@dataclass
class Organization:
    id: str
    name: str
    plan: str  # free | premium

    @staticmethod
    def create(name: str, plan: str = "free"):
        return Organization(
            id=str(uuid.uuid4()),
            name=name,
            plan=plan
        )
