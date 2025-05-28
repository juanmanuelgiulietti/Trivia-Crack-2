import random
import json
import time

def modoDesafio(nombre):
    niveles = [5, 10, 15, 20]
    nivel_actual = 0
    racha = 0

    print(f"\n🔥 Bienvenido al DESAFÍO, {nombre.upper()}!")
    print("🎯 Tu objetivo: responder correctamente 5, luego 10, luego 15 y finalmente 20 preguntas ¡sin fallar!\n")

    categorias = ["Arte", "Geografia", "Historia", "Deportes", "Entretenimiento", "Ciencia"]

    while nivel_actual < len(niveles):
        objetivo = niveles[nivel_actual]
        categoria = random.choice(categorias)
        print(f"🎯 Nivel {nivel_actual + 1}: {objetivo} respuestas correctas seguidas")

        pregunta = generarPreguntasYMostrarlas(categoria)
        esCorrecta = comprobarResultado(pregunta, nombre)

        if esCorrecta:
            racha += 1
            print(f"🔥 Racha actual: {racha}/{objetivo}\n")

            if racha == objetivo:
                print(f"✅ ¡Completaste el Nivel {nivel_actual + 1}!\n")
                nivel_actual += 1
                racha = 0
        else:
            print("❌ Fallaste... ¡volvés al principio!\n")
            racha = 0
            nivel_actual = 0
            time.sleep(1)

    print(f"\n🏆 ¡{nombre.upper()}, completaste el desafío de un jugador! ¡Sos una bestia de la trivia! 🧠🎉")


def determinarGanador(categoriasGanadasJugador, categoriasGanadasComputadora, nombre, rachaJugador, rachaComputadora, rondasJugadas):
    print("\n🎉 FIN DEL JUEGO 🎉")
    print("=" * 30)
    print("🏅 Resultados finales:")

    print(f"👤 {nombre}")
    print(f"- Categorías ganadas: {len(categoriasGanadasJugador)}")
    print(f"- Categorías: {categoriasGanadasJugador}")

    print("🤖 Computadora")
    print(f"- Categorías ganadas: {len(categoriasGanadasComputadora)}")
    print(f"- Categorías: {categoriasGanadasComputadora}")

    if len(categoriasGanadasJugador) > len(categoriasGanadasComputadora):
        print(f"\n🏆 ¡GANADOR: {nombre.upper()}! 🎉")
    elif len(categoriasGanadasJugador) < len(categoriasGanadasComputadora):
        print("\n🏆 ¡GANADOR: COMPUTADORA! 🤖") 
    else:
        print("\n🤝 ¡EMPATE! Ambos jugadores consiguieron la misma cantidad de coronas.")

    print("\n📊 Detalles de la partida:")
    print(f"- Rondas jugadas: {rondasJugadas}")
    print(f"- Racha máxima de {nombre}: {rachaJugador}")
    print(f"- Racha máxima de la computadora: {rachaComputadora}")
    print("=" * 30)

def jugarPorCorona(turno, nombre, categoriasGanadasJugador, categoriasGanadasComputadora, categorias):
    categoria = obtencionDeCorona(categorias, categoriasGanadasJugador, categoriasGanadasComputadora, turno, nombre)
    pregunta = generarPreguntasYMostrarlas(categoria)
    turno, esCorrecta = comprobarResultado(pregunta, turno, nombre)

    if esCorrecta:
        if turno == nombre:
            categoriasGanadasJugador.append(categoria)
            print(f"🎉 ¡FELICITACIONES, {nombre.upper()}! Ganaste la corona de {categoria.upper()} 🏆\n")
        else:
            categoriasGanadasComputadora.append(categoria)
            print(f"🤖 La computadora respondió correctamente... ¡y ganó la corona de {categoria}! 👑\n")
    else:
        if turno == nombre:
            print("😢 Fallaste la pregunta por la corona. ¡La próxima será!\n")
        else:
            print("🤖 La computadora falló la pregunta por la corona. ¡Zafaste por esta vez! 😅\n")
    
    return turno

def obtencionDeCorona(categorias, categoriasGanadasJugador, categoriasGanadasComputadora, turno, nombre):
    print("\n👑 Categorías disponibles para elegir:\n")

    categoriasDisponibles = []
    if turno == nombre:
        for cat in categorias:
            if cat not in categoriasGanadasJugador:
                categoriasDisponibles.append(cat)
    else:
        for cat in categorias:
            if cat not in categoriasGanadasComputadora:
                categoriasDisponibles.append(cat)

    for i, opcion in enumerate(categoriasDisponibles, 1):
        print(f"{i}. {opcion}")

    if turno == nombre:
        try:
            eleccion = int(input("Ingrese el número de la categoría por la que desea jugar: "))
            while eleccion < 1 or eleccion > len(categoriasDisponibles):
                print("Número inválido.")
                eleccion = int(input("Elija nuevamente: "))
            return categoriasDisponibles[eleccion - 1]
        except ValueError as e:
            print(f"Entrada no valida: {e}")
    else:
        return random.choice(categoriasDisponibles)

def comprobarResultado(pregunta, turno, nombre):
    if turno == nombre:
        respuesta = int(input("Ingrese su respuesta: "))
        while respuesta not in [1, 2, 3, 4]:
            print("❌ Opción inválida. Por favor, seleccioná un número dentro de las opciones.\n")
            respuesta = int(input("Ingrese su respuesta: "))
    else:
        respuesta = random.randint(1, 4)

    opcionSeleccionada = pregunta["opciones"][respuesta - 1]

    if opcionSeleccionada == pregunta["respuesta_correcta"]:
        print("\n✅ ¡Correcto!")
        print(f"🧠 La respuesta era: {pregunta['respuesta_correcta']}\n")
        return turno, True
    else:
        print("\n❌ ¡Incorrecto!")
        print(f"🧠 La respuesta era: {pregunta['respuesta_correcta']}\n")

        if turno == "Computadora":
            nuevoTurno = nombre
        else:
            nuevoTurno = "Computadora"

        return nuevoTurno, False

def generarPreguntasYMostrarlas(categoria):
    with open("preguntas.json", "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)

    preguntasPorCategoria = []
    for p in preguntas:
        if p["categoria"].lower() == categoria.lower():
            preguntasPorCategoria.append(p)
    
    if not preguntasPorCategoria:
        print(f"⚠️ No hay preguntas disponibles para la categoría {categoria}. Elegí otra.")
        return generarPreguntasYMostrarlas(random.choice(["Arte", "Geografia", "Historia", "Deportes", "Entretenimiento", "Ciencia"]))

    pregunta = random.choice(preguntasPorCategoria)

    print(f"\n📚 Categoría: {categoria}")
    print(f"🤔 Pregunta: {pregunta['pregunta']}")
    for i, opcion in enumerate(pregunta["opciones"], 1):
        print(f"{i}. {opcion}")

    return pregunta

def girarRuleta():
    categorias = ["Arte", "Geografia", "Historia", "Deportes", "Entretenimiento", "Ciencia", "Corona"]
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

    print("\n🎡 Girando la ruleta...")
    time.sleep(1)

    if categoria == "Corona":
        print("👑¡Te ha salido la corona!")

    print(f"🎯 La ruleta cayó en {emojis_categorias[categoria]} {categoria}\n")

    return categoria, categorias

def anunciarTurno(nombre, turno):
    if turno == "Computadora":
        print("🤖 Turno de la computadora...\n")
    else:
        print(f"👤 Es tu turno, {nombre}!\n")

def modoClasico(nombre, turno, categoriasGanadasJugador, categoriasGanadasComputadora, rachaJugador, rachaComputadora, rondasJugadas):
    maxRondas = 25
    rondasJugadas = 0
    rachaJugador = 0
    rachaComputadora = 0
    categoriasGanadasJugador = []
    categoriasGanadasComputadora = []

    while rondasJugadas < maxRondas:
        anunciarTurno(nombre, turno)
        categoria, categorias = girarRuleta()
        if categoria == "Corona":
            print("👑 ¡Te ha tocado jugar por una corona directamente desde la ruleta!")
            turno = jugarPorCorona(turno, nombre, categoriasGanadasJugador, categoriasGanadasComputadora, categorias)
            rondasJugadas += 1
            continue
        
        pregunta = generarPreguntasYMostrarlas(categoria)
        turno, esCorrecta = comprobarResultado(pregunta, turno, nombre)

        if esCorrecta:
            if turno == nombre:
                rachaJugador += 1
                rachaComputadora = 0
                print(f"🔥 Racha de {nombre}: {rachaJugador}")
                
                if rachaJugador == 3:
                    print("🏆 ¡Has ganado una racha de 3! Vas a jugar por una corona.")
                    turno = jugarPorCorona(turno, nombre, categoriasGanadasJugador, categoriasGanadasComputadora, categorias)

            else:
                rachaComputadora += 1
                rachaJugador = 0
                print(f"🔥 Racha de la computadora: {rachaComputadora}")

                if rachaComputadora == 3:
                    turno = jugarPorCorona(turno, nombre, categoriasGanadasJugador, categoriasGanadasComputadora, categorias)
        else:
            rachaJugador = 0
            rachaComputadora = 0

        time.sleep(0.5)
        rondasJugadas += 1

    print("\n🏁 ¡Se alcanzó el máximo de 25 rondas!")
    determinarGanador(categoriasGanadasJugador, categoriasGanadasComputadora, nombre, rachaJugador, rachaComputadora, rondasJugadas)
    print("🎖️ El juego ha terminado. ¡Gracias por jugar!\n")

def darBienvenida():
    nombre = input("Ingrese su nombre: ").capitalize()

    while nombre == "":
        print("No se ha ingresado un nombre. Vuelve a intentarlo.")
        nombre = input("Ingrese su nombre: ").capitalize()

    return nombre

def main():
    
    nombre = darBienvenida()

    print(f"\n🙌 ¡Hola {nombre}, crack de la trivia!")
    print("🧩 ¿Estás listo para demostrar cuánto sabés?")
    print("🎯 Girá la ruleta, respondé preguntas y ¡conseguí todas las coronas!\n")

    modos = ["Modo Clásico (Por turnos)", "Desafío Diario (Un jugador)"]

    for i, modo in enumerate(modos, 1):
        print(f"{i}. {modo}")

    jugar = int(input("\nEscoge el modo de juego que desees: "))

    while jugar not in [1, 2]:
        print("❌ Opción inválida. Por favor, seleccioná un número válido.")
        jugar = int(input("\nEscoge el modo de juego que desees: "))

    turno = nombre

    if jugar == 1:
        modoClasico(nombre, turno)
    else:
        modoDesafio(nombre)
main()