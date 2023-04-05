from secuenciaADN import SecuenciaADN
from random import randint


class Secuenciador():
    def __init__(self):
        self.__longitud = 0
        self.__secuencia = []
    
    def set_longitud(self, longitud):
        if isinstance(longitud, int):
            self.__longitud = longitud
        else:
            print("El tipo de dato no es aceptable")
            self.__longitud = 0
    
    def get_longitud(self):
        return self.__longitud
    
    def get_secuencia(self):
        return self.__secuencia
    
    def generar_secuencia(self):
        num = self.__longitud + randint(0, 10)
        for i in range (0, num):
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