# 🔠 Trivia Crack Python Edition 🎲

Una versión en consola del clásico juego **Trivia Crack**, creada en Python. Poné a prueba tus conocimientos en múltiples categorías y enfrentate a la computadora o al modo desafío individual. ¡Ideal para divertirte mientras aprendés!

## 🎮 Modos de juego

### 1. Modo Clásico (Por turnos)

* Juega por turnos contra la computadora.
* Se gira una ruleta para elegir una categoría.
* Al responder 3 preguntas seguidas correctamente, podés competir por una corona.
* Gana quien obtenga más coronas en 25 rondas.

### 2. Modo Desafío Diario (Un jugador)

* Tu objetivo es superar 4 niveles de dificultad consecutiva:

  * Nivel 1: 5 respuestas correctas seguidas
  * Nivel 2: 10 respuestas seguidas
  * Nivel 3: 15 respuestas seguidas
  * Nivel 4: 20 respuestas seguidas
* Si fallás, ¡volvés a empezar desde el primer nivel!

---

## 📂 Categorías disponibles

* 🎨 Arte
* 🌍 Geografía
* 🌺 Historia
* ⚽ Deportes
* 🎬 Entretenimiento
* 🧪 Ciencia

---

## 📁 Estructura del proyecto

```
Trivia/
├── preguntas.json
├── trivia.py
└── README.md
```

* `preguntas.json`: archivo con todas las preguntas organizadas por categoría.
* `trivia.py`: archivo principal del juego.
* `README.md`: este archivo.

---

## 📦 Requisitos

* Python 3.6 o superior

---

## ▶️ Cómo jugar

1. Cloná el repositorio o descargá los archivos.
2. Asegurate de tener el archivo `preguntas.json` en el mismo directorio que el script.
3. Ejecutá el juego con:

```bash
python trivia.py
```

4. Ingresá tu nombre y seleccioná el modo de juego.
5. ¡A jugar!

---

## 📝 Formato del archivo `preguntas.json`

Cada pregunta debe tener el siguiente formato:

```json
{
  "categoria": "Historia",
  "pregunta": "¿Quién fue el primer presidente de Argentina?",
  "opciones": ["Manuel Belgrano", "Domingo Sarmiento", "Bernardino Rivadavia", "Juan Manuel de Rosas"],
  "respuesta_correcta": "Bernardino Rivadavia"
}
```

> Asegurate de mantener las categorías con nombres consistentes y de incluir **exactamente 4 opciones** por pregunta.

---

## 📌 Funciones destacadas

* `modoClasico()`: lógica de juego multijugador contra la computadora.
* `modoDesafio()`: reto progresivo de un jugador.
* `girarRuleta()`: simula la ruleta con emojis.
* `generarPreguntasYMostrarlas()`: elige y muestra una pregunta aleatoria por categoría.
* `comprobarResultado()`: verifica si la respuesta es correcta.

---

## 🧪 Próximas mejoras

* 🖼️ Interfaz gráfica con Tkinter (en desarrollo)
* 📊 Estadísticas de jugador
* 🌍 Soporte para más idiomas
* 🧩 Más preguntas y categorías

---

## 👩‍💻 Autor

Desarrollado por **\[Juan Manuel Giulietti]**
Inspirado en el juego *Trivia Crack*
Con ❤️ por el aprendizaje y el juego justo

---

¿Querés colaborar? ¡Pull requests y nuevas preguntas son bienvenidas!