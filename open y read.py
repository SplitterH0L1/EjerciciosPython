#c=open("/home/beats7/github/ejerciciosPython/lecturadetexto.txt", "a" )# "a" sirve para gregar al final de este mas texto "r" sirve para leer
#"w" sirve para modificar todo el archivo y en caso de que no existalo va crear "x" para crear un archivo

#print(c.read()) #para leer un archivo

#for i in c:
#    print(i)
# c.write("agregando una nueva linea")
# c.close()

# x= open("/home/beats7/github/ejerciciosPython/lecturadetexto.txt")

# print(x.read())
# x.close()

import os
if os.path.exists ("/home/beats7/github/ejerciciosPython/lecturadetexto.txt"):
    os.remove("/home/beats7/github/ejerciciosPython/lecturadetexto.txt")

else:
    print("no existe el archivo")

os.rmdir("/home/beats7/github/ejerciciosPython/")