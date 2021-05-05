from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circulo(start, end):
    "Draw circle from start to end."
    distancia = end.x - start.x
    begin_fill()
    circle(distancia)
    end_fill()

#Adrian
def rectangle(start, end): # Esta funcion crea un rectangulo con la key "R"
    "Draw rectangle from start to end." 
    L = end.x - start.x  # Largo de rectangulo
    begin_fill()  # Iniciar relleno
    for count in range(4):  # For de 4 loops para 4 lineas del rectangulo
        if(count % 2): # IF para diferenciar los lados del rectangulo
            forward(L)
        else:
            forward(L/2) # Ancho de Rectangulo
        left(90)  # LLamada de funcion para vuelta a la izquierda de 90 grados
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    #Ricardo Triangulo
    L = end.x - start.x       #Distancia para los lados
    begin_fill()              #Iniciar relleno
    for count in range(3):    #Crean un trazo de 3 lineas de 120 
        forward(L)
        left(120)             #Angulo de vuelta
    end_fill()
        
    

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('#F5B7B1'), 'Q') #Color Maestra
onkey(lambda: color('#00ffff'), 'Y') #Color Ricardo
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
