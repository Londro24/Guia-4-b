from secunciador import Secuenciador


def main():
    x = "Hola Mundo"
    print(x.find("Hola"))
    
    interruptor = True
    animal = Secuenciador()
    print("Ingrese la longitud de la cadena")
    while animal.get_longitud() <= 0:
        animal.set_longitud(int(input()))
    animal.generar_secuencia()
    
    while interruptor:
        selec = -1
        while selec < 0 or selec > 3:
            print(
                "\n> Seleccione una opcion"
                "\n>> 1) mostrar secuencia" 
                "\n>> 2) calcular la longitud de la secuencia"
                "\n>> 3) hacer el complemento de la secuencia"
                "\n>> 4) mostrar secuencia complementaria"
                "\n>> 5) calcular la longitud de la secuencia complementaria"
                "\n>> 6) peso molecular de la secuencia"
                "\n>> 0) Salir"
                )
            
            try:
                selec = int(input())
                print("\n")
                if selec < 0 or selec > 3:
                    print("Valor invalido")
            except:
                print("Valor invalido")
        
        match selec:
            case 0:
                interruptor = False
            case 1:
                animal.usar_cadena(selec)
            case 2:
                animal.usar_cadena(selec)
            case 3:
                animal.usar_cadena(selec)
            case 4:
                animal.usar_cadena(selec)
            case 5:
                animal.usar_cadena(selec)
            case 6:
                animal.usar_cadena(selec)


if __name__ == "__main__":
    main()