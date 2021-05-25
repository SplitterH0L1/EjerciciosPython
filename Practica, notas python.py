# tipos de datos en python
# tipo de dato string entero y flotante

# string= "hola"
# Entero = 5
# flotante = 5.5
# Complejo = 1j


# declaracion de listas
# lista = [1, 2, 3] #las lista son cambiables a diferencia de las tuplas no#
# lista2 = ['saludo:hola mundo', 'saludo2 : hola wey']
# tupla = ('hola', 'mundo', 'somos', 'una tupla')

# diccionario = {
#     'Dragones': 'black'
#     }

# print (diccionario.get('Dragones'))
# print (diccionario ["Dragones"])

# diccionario anidado

# diccionario = {
#     "larry" : {
#         "Age" : " 20 ",
#         "cargo": "junior enginner"}

# }
# print (diccionario.get("larry"))


#             METODOS 

# lista.append = agrega elemento
# lista.clear = limpia elemtos en una variable
# lista.copy = copia una variable, lista, tupla
# lista.count() = cuenta cuantas veces se repite un elemnto
# len(lista) = cuenta cuantos elementos hay en una lista
# lista.pop() elimina el ultimo elemento
# lista.remove () elimina un elemnto de la lista
# lista.reverse = cambia al revez el orden de una lista
# lista.sort = ordena una lista pero deben ser del mismo tipo de dato
# tupla.index () muestra en que posicion se encuentra un elemento
# diccionario.get("nombre de el elemento")

# FUNCIONES

# try = captura una logica 
# except = captura el error de una logica
# exit() cierra la operacion
# if= si cumple una condicion
# elif= o si cumple otra condicion
# else=si no cumple las condiciones anteriores

# BUCLES
# while = mientras se cumplan la condicion se ejecutara while
# for = recorrer o itinerar
# break = detener el bucle
# continue = salta una linea si el if se cumple

#     i=0
#     While i<5
#         i += 1
#         if i == 3
#         continue
#     print ("i")

# para acceder a un elemento en python usar sintaxis siguiente
# diccionarios y listas

# Lista = [1,2,3]
# print = (lista(1))

# diccionario = ['dragon' : 'azul']
# print (diccionarios.get ('dragon'))
# print (diccionarios ["dragon"])



# asignar elementos listas luego de definir
# diccionarios ["nombre"] = "fluffy"

# OTRAS NOTAS DE SHURMAN


# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
#     print('El dato existe:', dato)
# else:
#     print('El dato no existe :(', dato)

# primero = input('Ingrese primer número: ')

# try:
#     primero = int(primero)
# except:
#     primero = 'chanchito feliz'

# if primero == 'chanchito feliz':
#     print('El valor ingresado no es un entero')
#     exit()

# segundo = input('Ingrese segundo número: ')

# try:
#     segundo = int(segundo)
# except:
#     segundo = 'chanchito feliz'

# if segundo == 'chanchito feliz':
#     print('El valor ingresado no es un entero')
#     exit()

# simbolo = input('ingrese operación: ')

# if simbolo == '+':
#     print('Suma:', primero + segundo)
# elif simbolo == '-':
#     print('Resta:', primero - segundo)
# elif simbolo == '*':
#     print('Multiplicación:', primero * segundo)
# elif simbolo == '/':
#     print('División:', primero / segundo)
# else:
#     print('El símbolo ingresado no es válido')


# CLASES AL FIIIIIINNNN XD :V 

class Usuario:                  # cuando se crea una clase la primera letra debe ser mayuscula y las instancias en miniscula
    def __init__(self, nombre, apellido):
        self.nombre = nombre            #self hace referencia a las instancias que tienen las clases
        self.apellido = apellido        #pero es mejor utilizarlo porque es una buena practica
    
    def saludo(self):
        print ("hola, mi nombre es", self.nombre, self.apellido)

# def saludo(nombre, apellido): #funcion de prueba
#         print ("hola, mi nombre es" + nombre + apellido)

class Admin(Usuario): #creando una clase con herencia, cuando se crea una clase con herencia se hereda el metodo init
    def superSaludo(self): #lo que hace es copiar la logica de Usuario solo que sin escribirla de nuevo
        print ("hola, me llamo,", self.nombre, 'y soy administrador')

# usuario = Usuario("felipe","feliz")
# # del usuario.nombre # aqui borro una propiedad de la class
# #del usuario ##aqui borro la class/objeto completa/o
# usuario.saludo()
# usuario.nombre= "chanchito" #aqui cambiamos el valor de felipe que se encuentra arriba
# usuario.saludo()

# admin= Admin('larry', 'Feliz')
# admin.saludo()

# admin.superSaludo()

class Animal:
    def __init__(self, tipo, onomatopeya):
        self.tipo = tipo
        self.onomatopeya = onomatopeya
        
    def saludo(self):
        print ("soy un", self.tipo, "me llamo", self.nombre, "y mi sonido es el", self.onomatopeya)
         
class Perro (Animal):
      nombre="stuar"
      def __init__(self,tipo,onomatopeya): #ignorando el metodo init de la clase padre y poniendo un metodo init distinto
        Animal.__init__(self,tipo,onomatopeya) #llamando el metodo init de la clase padre si queremos mantener el comportamiento
        print("soy un perro extendido")

class Ave(Animal):
    nombre="papau"
    def __init__(self,nombre,onomatopeya):
        super().__init__(nombre,onomatopeya) #otra forma de llamar al metodo init de  la clase padre
        print("instanciando un ave")

class Gato (Animal):
    nombre="fifi"

class Periquito (Animal):
    nombre= "roro"

# perro=Perro("Perro","ladrido")
# perro.saludo()

# gato= Gato("gato","maullido")
# gato.saludo()

# periquito=Periquito("periquito", "silvido")
# periquito.saludo()

# pajaro=Ave("ave", "silvido")
# pajaro.saludo()