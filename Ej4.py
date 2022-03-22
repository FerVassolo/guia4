"""Se desea implementar un sistema de tarjetas de viaje,
donde cada tarjeta tiene un saldo que se puede cargar
y a medida que se viaja se va descontando del mismo.
Además, se quiere agregar dos tipos de tarjetas adicionales con descuento.
Una para Jubilados, que tiene un 20% de descuento en todos los gastos,
y una para estudiantes, que tiene un 80% en los dos primeros viajes que realice en un día.
Todas las tarjetas tienen un descubierto autorizado de hasta 10$,
que la administración podría decidir cambiar en cualquier momento.
"""

class Tarjeta:

    precio_p_km = 1
    descubierto = -10
    PILAR = 0
    SAN_ISIDRO = 40
    CAPITAL = 100

    def __init__(self, saldo):
        self.saldo = saldo

    def viaje(self, inicio, destino):
        distancia = inicio - destino

