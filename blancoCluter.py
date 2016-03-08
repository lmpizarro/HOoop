import Blanco

class Blancocluter(Blanco):
    """
    Define un Blancocluter a ser detectado por un radar

    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        #TODO: completar con la inicializacion de los parametros del objeto
        pass
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        #TODO ver como se encajan los timepos del blanco y del intervalo de tiempo
        # senal.insert(self.instante, senal[instante]+self.amplitud)
        # modificar la senal conlos parametros del blanco
        pass
