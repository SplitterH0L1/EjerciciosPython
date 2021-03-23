
def incentivos (palabra): #defino la funcion para no tener que repetirla una y otra vez
     numero = int(input("porfavor introduzca la cuota del dia " + palabra + " del trabajador"))
     return numero
     

def run ():
    lz = incentivos("lunes")
    mz = incentivos ("martes")
    ms = incentivos("miercoles")
    js = incentivos("jueves")
    vs = incentivos ("viernes")
    so = incentivos("sabado")
    cuota = lz+mz+ms+js+vs+so
    produccion = 100

    if produccion <= cuota:
        print ("el trabajador recibe incentivos por la produccion")
    
    else: 
        print ("el trabajador no recibe incentivos por la produccion")
    



if __name__ == "__main__":
    print ("bienvenidos al sistema de incentivos de la empresa")
    run ()


#El ejercicio: 

#Se tiene registrado la producción (unidades) logradas por un operario a lo
#largo de la semana (lunes a sábado). Elabore un algoritmo que nos muestre o
#nos diga si el operario recibirá incentivos sabiendo que el promedio de
#producción mínima es de 100 unidades.