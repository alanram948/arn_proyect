from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import app.models.resultado as res 
import app.models.secuencia as sec
import app.db.database as database 
from app.services.analysis_service import analisis

sec.Base.metadata.create_all(bind=database.motor)
res.Base.metadata.create_all(bind=database.motor)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/Secuencias/analisis")
def insertar_cadena(nombre: str, cadena: str, db: Session = Depends(get_db)):
    sec_nueva=sec.Secuencia(nombre=nombre, cadena=cadena)
    db.add(sec_nueva)
    db.flush()
    ia=analisis(id_cadena=sec_nueva.id, db=db)
    resultado_ia=ia.guardar_dato()
    db.commit()
    resultado={"id_Secuencia":sec_nueva.id,
     "Secuencia":sec_nueva.cadena, 
     "id_resultado":resultado_ia.id, 
     "tipo":resultado_ia.tipo, 
     "probabilidad":resultado_ia.probabilidad
    }
    return resultado

@app.get("/mostrar cadenas")
def mostrar_cadenas(db: Session = Depends(get_db)):
    cadenas=db.query(sec.Secuencia).all()
    return cadenas

@app.get("/buscar por id")
def lista_cadenas(id: int, db: Session = Depends(get_db)):
    cadenas=db.query(sec.Secuencia).filter(sec.Secuencia.id==id).first()
    return cadenas
    
#función aproximada (estructura / familia)