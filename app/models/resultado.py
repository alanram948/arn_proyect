from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
import app.db.database as database 

Base = database.Base


class Resultado(Base):
    __tablename__="resultados"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    probabilidad = Column(Float)
    fecha = Column(Date)
    cadena_id = Column(Integer, ForeignKey("secuencias.id", ondelete="CASCADE"))

    dueno = relationship("Secuencia", back_populates="resultados")






