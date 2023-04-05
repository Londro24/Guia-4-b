class SecuenciaADN():
    def __init__(self):
        self.__cadena = []

    def set_cadena(self, cadena):
        self.__cadena = cadena

    def mostrar_cadena(self):
        if self.__cadena != []:
            cadena_str = ""
            for i in range(len(self.__cadena)):
                cadena_str = cadena_str + self.__cadena[i]
            print(cadena_str)
        else:
            print("No cadena complementaria")

    def contar_nucleotidos(self):
        if self.__cadena != []:
            print(f"Hay {len(self.__cadena)} nucleotidos")
        else:
            print("No cadena complementaria")
        
    def get_complemento_inverso(self):
        cadena_complemento = []
        cadena_inversa = []
        for i in range(len(self.__cadena)):
            if self.__cadena[i] == "A":
                cadena_complemento.append("T")
            elif self.__cadena[i] == "T":
                cadena_complemento.append("A")
            elif self.__cadena[i] == "C":
                cadena_complemento.append("G")
            elif self.__cadena[i] == "G":
                cadena_complemento.append("C")
            else:
                cadena_complemento.append(self.__cadena[i])
        for i in range(len(cadena_complemento)):
            cadena_inversa.append(cadena_complemento[len(cadena_complemento)-1-i])
        return cadena_inversa
    
    def encontrar_patron(self):
        patron = input("Ingrese el patron: ").upper()
        posiciones_encontradas = []
        cadena_str = ""
        for i in range(len(self.__cadena)):
            cadena_str = cadena_str + self.__cadena[i]
        while cadena_str != 0:
            posiciones_encontradas.apend(cadena_str.find(patron) + 1)
            cadena_str.replace(patron, patron.lower())
        if len(posiciones_encontradas) > 0:
            print(f"Hay {len(posiciones_encontradas)} posiciones")
            print(f"Encontradas: {posiciones_encontradas}")
        else:
            print("No hay ninguna posicion")
    
    def calcular_peso_molecular(self):
        peso_molecular = 0
        for i in range(len(self.__cadena)):
            match self.__cadena[i]:
                case "A":
                    peso_molecular = peso_molecular + 313.21
                case "T":
                    peso_molecular = peso_molecular + 304.2
                case "C":
                    peso_molecular = peso_molecular + 289.18
                case "G":
                    peso_molecular = peso_molecular + 329.21
            peso_molecular = peso_molecular + self.__cadena.count(self.__cadena[i])
        print(f"Peso molecula de la cadena es: {peso_molecular}")
        