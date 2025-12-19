from dataclasses import dataclass

@dataclass
class User:
    id: str
    email: str
    role: str  # admin | member | viewer
