# PruebaMesa3.py
# 5/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo de prueba para las clases Mesa3, MesaRedonda3 y MesaRectangular3

from MesaRedonda3 import MesaRedonda3
from MesaRectangular3 import MesaRectangular3

mesas = []

try:
    mesaRedonda = MesaRedonda3('Cubierta Pino', 0.5, 'Pedestal Pino')
    mesas.append(mesaRedonda)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesaRedonda = MesaRedonda3('Cubierta Pino', -0.6, 'Pedestal Pino')
    mesas.append(mesaRedonda)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesaRedonda = MesaRedonda3('Cubierta Pino', 0.6, 'Pedestal Pino')
    mesas.append(mesaRedonda)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesaRedonda = MesaRedonda3('Cubierta Cedro', 0.75, 'Pedestal Cedro')
    mesas.append(mesaRedonda)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesaRedonda = MesaRedonda3('Cubierta Cedro', -0.75, 'Pedestal Cedro')
    mesas.append(mesaRedonda)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesa = MesaRectangular3('Cubierta Pino', 1.0, 1.0, 'Pata Pino')
    mesas.append(mesa)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesa = MesaRectangular3('Cubierta Pino', 1.0, 1.2, 'Pata Pino')
    mesas.append(mesa)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesa = MesaRectangular3('Cubierta Pino', -1.0, 1.5, 'Pata Pino')
    mesas.append(mesa)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesa = MesaRectangular3('Cubierta Cedro', 1.2, 1.5, 'Pata Cedro')
    mesas.append(mesa)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

try:
    mesa = MesaRectangular3('Cubierta Cedro', 1.2, -1.5, 'Pata Cedro')
    mesas.append(mesa)
except ValueError as ve:
    print(f'No se pudo crear la mesa {ve}')

print(f'\nNúmero de mesas creadas = {MesaRedonda3.contadorMesas()}\n')

for mesa in mesas:
    print(mesa)
    print(f'Área = {mesa.calculaArea():.2f}')
    print(f'Costo = {mesa.calculaCosto():.2f}\n')
