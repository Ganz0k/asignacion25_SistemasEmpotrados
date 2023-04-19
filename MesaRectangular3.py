# MesaRectangular3.py
# 10/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase MesaRectangular3

from Mesa3 import Mesa3


class MesaRectangular3(Mesa3):
    """Clase MesaRectangular3 la cual hereda a la clase abstracta Mesa3
    """

    def __init__(self, cubierta: str, ancho: float, largo: float, pata: str):
        """Constructor que inicializa todos los parámetros de la clase

        --------------------------------------------------------------
        Parameters
        ----------
        cubierta: str
            Material de la cubierta de la mesa
        ancho: float
            Ancho de la cubierta
        largo: float
            Largo de la cubierta
        pata: str
            Material de las patas de la mesa
        """
        super().__init__('Mesa Rectangular', cubierta)

        if (ancho < 0.0 or largo < 0.0):
            raise ValueError(
                "Error: El valor del ancho y/o largo no puede ser negativo")

        self.__ancho = ancho
        self.__largo = largo
        self.__pata = pata
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
        return self.__ancho * self.__largo

    def calculaCosto(self):
        """Calcula el costo de la mesa

        ------------------------------
        Returns
        -------
        float
            Costo de la mesa
        """
        return (self.calculaArea() * MesaRectangular3._costos[self._cubierta]) + (MesaRectangular3._costos[self.__pata] * 4)

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return super().__str__() + f', ancho: {self.__ancho:.2f}, largo: {self.__largo:.2f}, material pata: {self.__pata}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return super().__repr__() + f', ancho: {self.__ancho:.2f}, largo: {self.__largo:.2f}, material pata: {self.__costoPata}'


if (__name__ == '__main__'):
    mesasRectangulares = []

    try:
        mesa = MesaRectangular3('Cubierta Pino', 1.0, 1.0, 'Pata Pino')
        mesasRectangulares.append(mesa)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')

    try:
        mesa = MesaRectangular3('Cubierta Pino', 1.0, 1.2, 'Pata Pino')
        mesasRectangulares.append(mesa)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')
    
    try:
        mesa = MesaRectangular3('Cubierta Pino', -1.0, 1.5, 'Pata Pino')
        mesasRectangulares.append(mesa)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')
    
    try:
        mesa = MesaRectangular3('Cubierta Cedro', 1.2, 1.5, 'Pata Cedro')
        mesasRectangulares.append(mesa)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')

    try:
        mesa = MesaRectangular3('Cubierta Cedro', 1.2, -1.5, 'Pata Cedro')
        mesasRectangulares.append(mesa)
    except ValueError as ve:
        print(f'No se pudo crear la mesa {ve}')

    print(f'\nNúmero de mesas creadas = {MesaRectangular3.contadorMesas()}\n')

    for mesa in mesasRectangulares:
        print(mesa)
        print(f'Área = {mesa.calculaArea():.2f}')
        print(f'Costo = {mesa.calculaCosto():.2f}\n')
