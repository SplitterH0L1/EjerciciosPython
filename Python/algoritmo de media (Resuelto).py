def intro(r):
    numero = float(input("Porfavor introduzca la témperatura numero " + r + ""))
    return numero


def run():

    def msjp(mediastring, s):

        return print("la temperatura numero " + s + " es mayor a la temperatura media (" + mediastring + "°)\n")

    def msjn(mediastring, s):

        return print("la temperatura numero " + s + " es menor que la temperatura media (" + mediastring + "°)\n")

    def msji(mediastring, s):

        return print("la temperatura numero " + s + " es igual que la temperatura media (" + mediastring + "°)\n")

    def calculo(opcion, s, mediastring):

        if opcion > media:
            msjp(mediastring, s)

        elif opcion < media:
            msjn(mediastring, s)

        else:
            msji(mediastring, s)

    temp1 = intro("1= ")
    temp2 = intro("2= ")
    temp3 = intro("3= ")
    temp4 = intro("4= ")
    temp5 = intro("5= ")
    # suma = (intro(1) + intro(2) + intro(3) + intro(4) + intro(5))

    suma = (temp1+temp2+temp3+temp4+temp5)
    print (str(suma))

    media = suma / 5.0
    

    print("la temperatura media es " + str(media) + "C°")

    calculo(temp1, "1", str(media))
    calculo(temp2, "2", str(media))
    calculo(temp3, "3", str(media))
    calculo(temp4, "4", str(media))
    calculo(temp5, "5", str(media))


if __name__ == "__main__":
    print("\nBienvenido al sistema de temperatura \n" +
          "le pediremos 5 temperaturas a continuacion \n")
    run()

#Tenemos N temperatura, escribir un algoritmo que muestre el promedio 
# y que diga que temperatura es alta a la promedio y cual es baja a la
#temperatura promedio.