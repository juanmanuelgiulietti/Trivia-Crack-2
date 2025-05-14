import random
import json
import time

def comprobarResultado(pregunta, turno, nombre):
    respuesta = int(input("Ingrese su respuesta: "))
    while respuesta not in [1,2,3,4]:
        print("❌ Opción inválida. Por favor, seleccioná un número dentro de las opciones.\n")
    opcionSeleccionada = pregunta["opciones"][respuesta - 1]
    
    if opcionSeleccionada == pregunta["respuesta_correcta"]:
        print("¡Correcto! ✔️")
        print(f"🧠 La respuesta era: {pregunta["respuesta_correcta"]}")
        return turno
    else:
        print("❌ ¡Incorrecto! ")
        print(f"🧠 La respuesta era: {pregunta["respuesta_correcta"]}")
        if turno == nombre:
            return "Computadora"
        else:
            return nombre
        
def generarPreguntasYMostrarlas(categoria):
    with open("preguntas.json", "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)
    preguntasPorCategoria = [pregunta for pregunta in preguntas if pregunta["categoria"].lower() == categoria.lower()]
    for pregunta in preguntasPorCategoria:
        print(f"📚 Categoría: {categoria}")
        print(f"🤔 Pregunta: {pregunta["pregunta"]}")
        for i, opcion in enumerate(pregunta["opciones"], 1):
            print(f"{i}. {opcion}")
    return pregunta

def girarRuleta():
    categorias = ["Arte", "Geografia", "Historia", "Deportes", "Entretenimiento", "Ciencia"]
    emojis_categorias = {
    "Arte": "🎨",
    "Ciencia": "🧪",
    "Deportes": "⚽",
    "Entretenimiento": "🎬",
    "Geografia": "🌍",
    "Historia": "🏺",
    "Corona": "👑"
    }
    categoria = random.choice(categorias)
    print("🎡 Girando la ruleta...")
    time.sleep(1)
    print(f"🎡 La ruleta giró... ¡y cayó en {emojis_categorias[categoria]} {categoria.capitalize()}!")
    return categoria

def anunciarTurno(nombre, turno):
    if turno == "Computadora":
        print("🤖 Turno de la computadora...\n")
    else:
        print(f"👤 Es tu turno, {nombre}!\n")
        
# Comenzar a jugar (Modo Clasico)
def modoClasico(nombre, turno):    
    anunciarTurno(nombre, turno)
    categoria = girarRuleta()
    pregunta = generarPreguntasYMostrarlas(categoria)
    turno = comprobarResultado(pregunta, turno, nombre)
    time.sleep(2)
    
# Dar bienvenida al usuario
def darBienvenida():
    nombre = str(input("Ingrese su nombre: ")).capitalize()
    while nombre == "":
        print("No se ha ingresado un nombre. Vuelve a intentarlo.")
        nombre = str(input("Ingrese su nombre: ")).capitalize()
    return nombre

def main():
    # Dar bienvenida al usuario
    nombre = darBienvenida()
    print(f"🙌 ¡Hola {nombre}, crack de la trivia!\n")
    print("🧩 ¿Estás listo para demostrar cuánto sabés?")
    print("🎯 Girá la ruleta, respondé preguntas y ¡conseguí todas las coronas!\n")
    modosDeJuego = ["Modo Clasico (Por turnos)", "Desafío Diario (Un jugador)"]
    print("¡Escoge tu modo de juego!\n")
    for i, modo in enumerate(modosDeJuego, 1):
        print(f"{i}. {modo}")
        
    # Comenzar a jugar
    jugar = int(input("Escoge el modo de juego que desee: "))
    while jugar not in [1, 2]:
        print("❌ Opción inválida. Por favor, seleccioná un número del menú.\n")
    turno = nombre
    if jugar == 1:
        modoClasico(nombre, turno)
    else:
        print("🔧 Modo Desafío Diario aún no está disponible.")
main()