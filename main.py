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
main()