import datetime
import radar
import generador
import detector
import medio
import blanco


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #TODO construir un nuevo genrador de senales
    mi_generador = generador.Generador(amplitud, fase, frecuencia)

    #TODO construir un detector
    mi_detector = detector.Detector()
    

    #TODO construir un nuevo radar
    mi_radar = radar.Radar(mi_generador, mi_detector)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    #TODO contruir un nuevo blanco
    mi_blanco = blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco, tiempo_final_del_blanco)

    #TODO contruir un medio

    mi_medio = medio.Medio(mi_blanco)

    #TODO llamar a la funcion detectar del  radar

    mi_radar.detectar(mi_medio, tiempo_inicial, tiempo_final)

if __name__ == "__main__":
    main()
