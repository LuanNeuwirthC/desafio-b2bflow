from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    phone: str

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()
        if not name or not phone:
            raise ValueError(f"Contato com dados incompletos: {data}")
        return cls(name=name, phone=phone)
