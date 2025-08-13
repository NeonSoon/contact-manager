from dataclasses import dataclass, asdict
from typing import Dict

@dataclass
class Contact:
    id: int
    name: str
    email: str = ""
    phone: str = ""

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)

    @staticmethod
    def from_dict(d: Dict[str, str]) -> "Contact":
        return Contact(
            id=int(d.get("id", 0)),
            name=d.get("name", ""),
            email=d.get("email", ""),
            phone=d.get("phone", ""),
        )
