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
        condition1 = self.tiempo_final > tiempo_inicial
        condition2 = self.tiempo_inicial < tiempo_final 
        if condition1 and condition2 :
              t = self.tiempo_final - self.tiempo_inicial
              if self.tiempo_final > tiempo_final:
                  t = tiempo_final - self.tiempo_inicial
              if self.tiempo_inicial < tiempo_inicial:
                  t = self.tiempo_final - tiempo_inicial


        return t
        
