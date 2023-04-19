# MesaRedonda3.py
# 10/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase MesaRedonda3

from Mesa3 import Mesa3
from math import pi


class MesaRedonda3(Mesa3):
    """Clase MesaRedonda3 la cual hereda a la clase abstracta Mesa3
    """

    def __init__(self, cubierta: str, radio: float, pedestal: str):
        """Constructor que inicializa todos los parámetros de la clase

        --------------------------------------------------------------
        Parameters
        ----------
        cubierta: str
            Material de la cubierta de la mesa
        radio: float
            Radio de la mesa
        pedestal: str
            Material del pedestal de la mesa
        """
        super().__init__('Mesa Redonda', cubierta)

        if (radio < 0.0):
            raise ValueError("Error: El valor del radio no puede ser negativo")

        self.__radio = radio
        self.__pedestal = pedestal
        Mesa3._contadorMesas += 1
        self._numMesa = Mesa3._contadorMesas

    def calculaArea(self):
        """Calcula el área de la mesa

        -----------------------------
        Returns
        -------
        float
            Área de la mesa
        """
        return pi * (self.__radio ** 2)

    def calculaCosto(self):
        """Calcula el costo de la mesa

        ------------------------------
        Returns
        -------
        float
            Costo de la mesa
        """
        return (self.calculaArea() * MesaRedonda3._costos[self._cubierta]) + MesaRedonda3._costos[self.__pedestal]

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return super().__str__() + f', radio: {self.__radio:.2f}, material pedestal: {self.__pedestal}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return super().__repr__() + f', radio: {self.__radio:.2f}, material pedestal: {self.__pedestal}'


if (__name__ == '__main__'):
    mesasRedondas = []

    try:
        mesaRedonda = MesaRedonda3('Cubierta Pino', 0.5, 'Pedestal Pino')
        mesasRedondas.append(mesaRedonda)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')

    try:
        mesaRedonda = MesaRedonda3('Cubierta Pino', -0.6, 'Pedestal Pino')
        mesasRedondas.append(mesaRedonda)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')

    try:
        mesaRedonda = MesaRedonda3('Cubierta Pino', 0.6, 'Pedestal Pino')
        mesasRedondas.append(mesaRedonda)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')

    try:
        mesaRedonda = MesaRedonda3('Cubierta Cedro', 0.75, 'Pedestal Cedro')
        mesasRedondas.append(mesaRedonda)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')

    try:
        mesaRedonda = MesaRedonda3('Cubierta Cedro', -0.75, 'Pedestal Cedro')
        mesasRedondas.append(mesaRedonda)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')

    print(f'\nNúmero de mesas creadas = {MesaRedonda3.contadorMesas()}\n')

    for mesa in mesasRedondas:
        print(mesa)
        print(f'Área = {mesa.calculaArea():.2f}')
        print(f'Costo = {mesa.calculaCosto():.2f}\n')
