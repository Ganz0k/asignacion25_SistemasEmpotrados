# Mesa3.py
# 10/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase abstracta Mesa3

import abc


class Mesa3(abc.ABC):
    """Clase abstracta Mesa3
    """

    _costos = {'Cubierta Pino': 100.0,
               'Cubierta Cedro': 200.0,
               'Pedestal Pino': 500.0,
               'Pedestal Cedro': 800.0,
               'Pata Pino': 60.0,
               'Pata Cedro': 80.0}

    _contadorMesas = 0

    def __init__(self, tipoMesa: str, cubierta: str):
        """Constructor que inicializa todos los parámetros

        --------------------------------------------------
        Parameters
        ----------
        tipoMesa: str
            Tipo de la mesa
        cubierta: str
            Material de la cubierta de la mesa
        """
        self._tipoMesa = tipoMesa
        self._cubierta = cubierta

    @classmethod
    def contadorMesas(cls):
        """Regresa el número de mesas creadas

        -------------------------------------
        Returns
        -------
        int
            Número de mesas creadas
        """
        return cls._contadorMesas

    @abc.abstractmethod
    def calculaArea(self):
        """Calcula el área de la mesa

        -----------------------------
        Returns
        -------
        float
            Área de la mesa
        """

    @abc.abstractmethod
    def calculaCosto(self):
        """Calcula el costo de la mesa

        ------------------------------
        Returns
        -------
        float
            Costo de la mesa
        """

    @abc.abstractmethod
    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return f'Tipo de mesa: {self._tipoMesa}, Material de la cubierta: {self._cubierta}'

    @abc.abstractmethod
    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return f'{self.__module__}, {self.__class__.__name__}, Tipo de mesa: {self._tipoMesa}, Material de la cubierta: {self._cubierta}'
