class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        #TODO: completar con la inicializacion de los parametros del objeto
        pass
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final


    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        # tiempo_inicial del radar encendido
        # tiempo final del radar encendido
        detected = False
        if tiempo_inicial <= self.tiempo_inicial:
           if tiempo_final >= self.tiempo_final:
              detected = True


        return detected
        
