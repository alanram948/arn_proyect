import app.db.database as database
from sqlalchemy.orm import Session
from app.models.resultado import Resultado
from app.models.secuencia import Secuencia
from motor_ia.predictor import predict

class analisis():
    def __init__(self, id_cadena: int, db: Session):
        self.db = db
        self.id_cadena=id_cadena
        self.dato_cadena=db.query(Secuencia).filter(Secuencia.id==self.id_cadena).first()
        self.cadena_arn = self.dato_cadena.cadena
    def limpieza(self):
        self.cadena_arn = self.cadena_arn.replace(" ", "")
        self.cadena_arn = self.cadena_arn.upper()
        return self.cadena_arn

    def validacion(self):
        cadena = self.limpieza()
        for i in cadena:
            if i != 'A' and i != 'U' and i != 'G' and i != 'C':
                return False
        
        return True
    
    def paso_a_ia(self):
        if self.validacion():
            #modulo de ia
            respuesta=predict(self.cadena_arn)
        else:
            #detecta error y genera solucion(pendiente)
            pass
        return respuesta
    
    def genera_dato(self):
        respuesta=self.paso_a_ia()
        construccion_base=Resultado(tipo=respuesta[0], probabilidad=respuesta[1], cadena_id= self.id_cadena)
        return construccion_base    
    def guardar_dato(self):
        data=self.genera_dato()
        self.db.add(data)
        return data
        