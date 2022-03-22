"""Diseñe un sistema para un Hotel.
El Hotel puede tener varios tipos de habitaciones, puede ser Estándar, Suite, o Presidencial.
Cada habitación tiene su propio precio, y su propia cantidad de posibles personas que lo pueden ocupar.
Por ejemplo, la Estándar tiene un costo de 1000$ y puede ser ocupada por 4 personas;
la Suite, 2000$ y puede estar ocupada por 2 personas
y la Presidencial 4000$ y puede ser ocupada por 2.
Además, el sistema debe permitir un sistema de reservas.
A los clientes, se les asigna una habitación y una fecha."""

from abc import ABC, abstractmethod

class Habitacion:

    def __init__(self, numero):
        self.numero = numero
# una vez reservada la habitacion se crea una lista (o dicc) con el nro de habitacion y la fecha
    @abstractmethod
    def reservarHabitacion(self, fecha):
        #if self.numero in habitaciones:
            #if self.fecha not in habitacionesUsadas[self.numero]
        pass

class Estandar(Habitacion):

    precio = 1000

    habitacionesUsadas = {1: [], 2: [], 3: [], 4: [] }

    def __init__(self, numero):
        super().__init__(numero)

    def reservarHabitacion(self, fecha):
        if self.numero in self.habitacionesUsadas:
            if fecha not in self.habitacionesUsadas[self.numero]:
                self.habitacionesUsadas[self.numero].append(fecha)
            else:
                return "Fecha en uso"
        else:
            return "No existe la habitación"

H1 = Estandar(1)
H1.reservarHabitacion(1)
print(Estandar.habitacionesUsadas)

