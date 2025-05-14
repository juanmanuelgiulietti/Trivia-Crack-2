import random
import json
import time

def comprobarResultado(pregunta, turno, nombre, rachaJugador, rachaComputadora):
    if turno == nombre:
        respuesta = int(input("Ingrese su respuesta: "))
        while respuesta not in [1,2,3,4]:
            print("❌ Opción inválida. Por favor, seleccioná un número dentro de las opciones.\n")
    else:
        respuesta = random.randint(1, 4)
            
    opcionSeleccionada = pregunta["opciones"][respuesta - 1]
    
    if opcionSeleccionada == pregunta["respuesta_correcta"]:
        print("¡Correcto! ✔️")
        print(f"🧠 La respuesta era: {pregunta["respuesta_correcta"]}")
        if turno == nombre:
            rachaJugador += 1
            rachaComputadora = 0
        else:
            rachaComputadora += 1
            rachaJugador = 0
        return turno, True
    else:
        print("❌ ¡Incorrecto! ")
        print(f"🧠 La respuesta era: {pregunta["respuesta_correcta"]}")
        rachaJugador = 0
        rachaComputadora = 0
        if turno == "Computadora":
            nuevoTurno = nombre 
        else:
            nuevoTurno = "Computadora"
        return nuevoTurno, False
        
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
    # Gestion de rondas y rachas de jugadores
    maxRondas = 25
    rondasJugadas = 0
    rachaJugador = 0
    rachaComputadora = 0
    
    while rondasJugadas < maxRondas:
        anunciarTurno(nombre, turno)
        categoria = girarRuleta()
        pregunta = generarPreguntasYMostrarlas(categoria)
        turno, esCorrecta = comprobarResultado(pregunta, turno, nombre, rachaJugador, rachaComputadora)
        
        if esCorrecta:
            if turno == nombre:
                rachaJugador += 1
                rachaComputadora = 0
                print(f"🔥 Racha de {nombre}: {rachaJugador}")
                if rachaJugador == 3:
                    print("👑 ¡Ganaste la corona!")
                    rachaJugador = 0
            else:
                rachaComputadora += 1
                rachaJugador = 0
                print(f"🔥 Racha de Computadora: {rachaComputadora}")
                if rachaComputadora == 3:
                    print("👑 ¡La computadora ganó la corona!")
                    rachaComputadora = 0
        else:
            rachaJugador = 0
            rachaComputadora = 0
                
        
        time.sleep(2)
        
        rondasJugadas += 1
    print("\n🏁 ¡Se alcanzó el máximo de 25 rondas!")
    print("🎖️ El juego ha terminado. Gracias por jugar.")
    
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