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
        #se eliminan espacios y se normaliza a mayusculas
        self.cadena_arn = self.cadena_arn.replace(" ", "")
        self.cadena_arn = self.cadena_arn.upper()
        return self.cadena_arn

    def validacion(self):
        #marca si la cadena contiene los caracteres esperados
        caracteres={"A", "U", "G", "C"}
        cadena = self.limpieza()
        if not 20<len(cadena)<10000:
            return False
        if all(base in caracteres for base in cadena):
            return True
        return False
        
    
    def paso_a_ia(self):
        if self.validacion():
            #modulo de ia
            respuesta=predict(self.cadena_arn)
        else:
            return False;
        return respuesta
    
    def genera_dato(self):
        respuesta=self.paso_a_ia()
        if respuesta==False:
            return False
        else:
            construccion_base=Resultado(tipo=respuesta[0], probabilidad=respuesta[1], cadena_id= self.id_cadena)
        return construccion_base    
    def guardar_dato(self):
        data=self.genera_dato()
        if data==False:
            return False
        else:
            self.db.add(data)
        return data
        