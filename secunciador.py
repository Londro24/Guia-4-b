"""Se importa la clase con la que trabajara y un generador pseudo"""
from random import randint
from secuenciaadn import SecuenciaADN


class Secuenciador():
    """La clase se encarga de crear una secuencia de nucleoticos"""
    def __init__(self):
        self.__longitud = 0
        self.__secuencia = []
    def set_longitud(self, longitud):
        """Se encarga de definir la longitud de la secuencia"""
        if isinstance(longitud, int):
            self.__longitud = longitud
        else:
            print("El tipo de dato no numerico, intente nuevamente")
            self.__longitud = 0
    def get_longitud(self):
        """Se encarga de devolver la longitud de la secuencia"""
        return self.__longitud
    def get_secuencia(self):
        """Se encarga de devolver la secuencia"""
        return self.__secuencia
    def generar_secuencia(self):
        """Genera una secuencia aleatoria en conjunto a la funcion randint"""
        num = self.__longitud + randint(0, 10)
        for _ in range (0, num):
            nucleotido_num = randint(1,4)
            match nucleotido_num:
                case 1:
                    self.__secuencia.append("A")
                case 2:
                    self.__secuencia.append("T")
                case 3:
                    self.__secuencia.append("C")
                case 4:
                    self.__secuencia.append("G")
    def usar_cadena(self, selec):
        """Funciona como menu para usar una secuencia de nucleoticos"""
        adn = SecuenciaADN()
        adn_complemento = SecuenciaADN()
        adn.set_cadena(self.__secuencia)
        match selec:
            case 1:
                adn.mostrar_cadena()
            case 2:
                adn.contar_nucleotidos()
            case 3:
                adn_complemento.set_cadena(adn.get_complemento_inverso())
                adn_complemento.mostrar_cadena()
            case 4:
                adn_complemento.set_cadena(adn.get_complemento_inverso())
                adn_complemento.contar_nucleotidos()
            case 5:
                adn.encontrar_patron()
            case 6:
                adn.calcular_peso_molecular()
