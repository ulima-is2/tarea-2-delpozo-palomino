#!/usr/bin/python
# -*- coding: utf8 -*-
import sys

# Patrón COMPOSITE -> Permite trabajar con un objeto por la composición de sus hijos,
# se implementa los métodos listar_peliculas y listar_funciones debido a que estos son los hijos principales de todo CINE,
# entonces con esto, se puede listar las peliculas y funciones de TODOS los cines
class ComponenteCine:
    def listar_peliculas(self):
        pass

    def listar_funciones(self):
        pass

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class CinePlaneta:
    def __init__(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaD = Pelicula(3, 'Desparecido')
        peliculaDeep = Pelicula(4, 'Deep El Pulpo')

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []

    def listar_peliculas(self):
        print('********************')
        for pelicula in self.lista_peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************')

    def listar_funciones(self, pelicula_id):
        print('********************')
        for funcion in self.lista_peliculas[int(pelicula_id) - 1].funciones:
            print('Función: {}'.format(funcion))
        print('********************')


    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)



class CineStark:
    def __init__(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


    def listar_peliculas(self):
        print('********************')
        for pelicula in self.lista_peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************')

    def listar_funciones(self, pelicula_id):
        print('********************')
        for funcion in self.lista_peliculas[int(pelicula_id) - 1].funciones:
            print('Función: {}'.format(funcion))
        print('********************')

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)


# Patrón FACTORY METHOD -> Permite la creación de instancias apartir de una condición dada por un FLAG,
# esto desacopla la lógica del condicional
class CineFactory():

    CINE_PLANETA = '1'
    CINE_STARK = '2'

    def crear_cine(self,tipo_cine):
        if tipo_cine == self.CINE_PLANETA:
            return CinePlaneta()
        elif tipo_cine == self.CINE_STARK:
            return CineStark()
        else:
            return None


# Patrón DECORATOR -> Permite agregar funcionalidad a un método envolviéndolo en otro,
# esto no altera el primero por lo cual se respeta el prinicio Open Close
class Mensaje():

    def __init__(self):
        pass

    # Función a decorar
    def armar_mensaje(self, *oraciones):
        cad = ''
        for oracion in oraciones:
            cad = cad + oracion + "\n"
        return cad


    # Función decoradora
    def decorar_mensaje(self, imprimir_mensaje):
        def decorador(*oraciones):
            cad = '********************\n'
            cad = cad + self.armar_mensaje(*oraciones)
            cad = cad + '********************'
            return cad
        return decorador


# Patrón FACADE -> Permite abstraer toda la capa de lógica en una clase encargada de gestionarla,
# esta es la única entrada para acceder a todo el ejercicio del Cine, por lo que aplica una capa de seguridad, mayor poder de gestión
# desacoplamiento y mantenibilidad
class GestorCine():

    def __init__(self):
        self.terminado = False;
        self.cine_factory = CineFactory()
        self.gestor_mensaje = Mensaje()


    def realizar_accion(self):
        decorador = self.gestor_mensaje.decorar_mensaje(self.gestor_mensaje.armar_mensaje)

        while not self.terminado:
            mensaje = self.gestor_mensaje.armar_mensaje(
                'Ingrese la opción que desea realizar',
                '(1) Listar cines',
                '(2) Listar cartelera',
                '(3) Comprar entrada',
                '(0) Salir')
            print(mensaje)
            opcion = input('Opción: ')

            if opcion == '1':
                cad = decorador(
                    'Lista de cines',
                    '1: CinePlaneta',
                    '2: CineStark')
                print(cad)
            elif opcion == '2':
                cad = decorador(
                    'Lista de cines',
                    '1: CinePlaneta',
                    '2: CineStark')
                print(cad)

                cine = input('Primero elija un cine:')
                cine = self.cine_factory.crear_cine(cine)
                cine.listar_peliculas()



            elif opcion == '3':
                cad = decorador(
                    'COMPRAR ENTRADA',
                    'Lista de cines',
                    '1: CinePlaneta',
                    '2: CineStark')
                print(cad)
                cine = input('Primero elija un cine:')
                cine = self.cine_factory.crear_cine(cine)
                cine.listar_peliculas()

                pelicula_elegida = input('Elija pelicula:')
                #pelicula = obtener_pelicula(id_pelicula)
                print('Ahora elija la función (debe ingresar el formato hh:mm): ')
                cine.listar_funciones(pelicula_elegida)
                funcion_elegida = input('Funcion:')
                cantidad_entradas = input('Ingrese cantidad de entradas: ')
                codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
                print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
            elif opcion == '0':
                terminado = True
            else:
                print(opcion)



def main():
    gestor_cine = GestorCine()
    gestor_cine.realizar_accion()

if __name__ == '__main__':
    main()
