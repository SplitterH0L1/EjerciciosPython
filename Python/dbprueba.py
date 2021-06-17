
import mysql.connector

# def dato(dto):
#     dato = input("ingrese su " + dto)
#     return dato

midb = mysql.connector.connect (
    host="localhost",
    # host="localhost",
    # port="8000",
    user='beats8',
    password='29855853',
    database='Prueba'
)
"""conexion para base de datos"""


cursor=midb.cursor() #lo que permite interactuar con la base de datos mediante el lenguaje sql

                        #PARA MOSTRAR UNA TABLA
#cursor.execute('select * from usuario') #para consulta, seleccion de todos los datos en la tabla usuario
#resultado= cursor.fetchone() #sirve para traer un dato en concreto de la base de datos
#print(resultado) # mostras en consola la consulta

                        #PARA MOSTRAR UNA TABLA LIMITADA
#cursor.execute('select * from usuario LIMIT 2') #para consulta, seleccion de todos los datos en la tabla usuario
#resultado= cursor.fetchone() #sirve para traer un dato en concreto de la base de datos
#print(resultado) # mostras en consola la consulta

                    # PARA VER LA DEFINICION DE UNA TABLA
#cursor.execute ('show create table usuario') #Para mostrar la estructura de una tabla
#resultado=cursor.fetchall() #guardar en la variable una consulta de tipo all (todo)
#print (resultado)
                        #INSERTAR DATOS

#sql = 'insert into usuario (username, email, password) values (%s, %s, password(%s))'
#values = (dato("username"), dato("email"), dato("password"))
#print (values nb)

#cursor.execute (sql, values)

#midb.commit()

# #print (cursor.rowcount)

                        # ACTUALIZAR DATOS
# sql='update usuario set username = %s where id = %s'#aqui para actualizar algun dato de la lista
# values = ('larrypro44', 4) #para definir los valores que hay arriba
# cursor.execute(sql, values) #metod para ejecutar las variables que hay dentro de los parentesis

# midb.commit() #para efectuar cambios

                        #PARA BORRAR DATOS
# sql = 'delete from usuario where id = %s' #aqui para borrar algun dato de la lista
# values = (1, ) #para definir los valores que hay arriba
# cursor.execute(sql, values) #metod para ejecutar las variables que hay dentro de los parentesis

# midb.commit() #para efectuar cambios

#pd = para borrar siempre colocar una coma despues de introducir el valor porque el sql lee lista solamente

