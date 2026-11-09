from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class Ruolo(str, Enum):
    ADMIN = "admin"
    USER = "user"

class Indirizzo(BaseModel):
    via: str = Field(min_length=1)
    citta: str = Field(min_length=1)
    cap: str = Field(pattern="^[0-9]{5}$")

class Utente(BaseModel):
    id: int
    nome: str = Field(min_length=2, max_length=50)
    email: EmailStr
    eta: int | None = Field(default=None, gt=0, lt=130)
    ruolo: Ruolo = Field(default=Ruolo.USER)
    tags: list[str] = Field(default_factory=list)
