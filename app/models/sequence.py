from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import database
Base = database.Base

class secuencia(Base):
    __tablename__="secuencias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    cadena=Column(String, nullable=False)

    resultados = relationship("Resultado", back_populates="dueno", cascade="all, delete")
