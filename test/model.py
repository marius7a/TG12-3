from pydantic import BaseModel, Field, field_validator

class iPad(BaseModel):
    name: str = Field(..., min_lengt=3, max_length=5)
    gigabyte: int = Field(default=64, ge=64, le=512)
    farbe: str = Field(default="silber", min_lenght=2, max_length=10)

    @field_validator("farbe")

    def check(cls, value):
       erlaubt = {"blau","weiss","silber","schwarz"} 
       if value not in erlaubt:
           raise ValueError (f"Ungültige Farbe:{value}")
       return value
    

