from pydantic import BaseModel, Field, field_validator

class Spieler(BaseModel):
    name: str = Field(..., min_length=2, max_length=30)
    alter: int = Field(..., ge=16, le=40)
    position: str = Field(default="unbekannt")
    tore: int = Field(default=0, ge=0)

    @field_validator("position")
    def check_position(cls, value):
        erlaubte_positionen = {"Torwart", "Innenverteidiger","Außenverteidiger", "Zentrales Mittelfeld","Flügelspieler", "Stürmer"}
        if value not in erlaubte_positionen:
            raise ValueError(f"Ungültige Position: {value}")
        return value

    model_config = {"validate_assignment": True}



