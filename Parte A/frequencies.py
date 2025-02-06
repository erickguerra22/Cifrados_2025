import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

print("-"*40)
print("ANÁLISIS DE FRECUENCIAS")
print("-"*40)

alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Frecuencias teóricas en español
theorical = {
    'a': 0.1253,
    'b': 0.0142,
    'c': 0.0468,
    'd': 0.0586,
    'e': 0.1368,
    'f': 0.0069,
    'g': 0.0101,
    'h': 0.0070,
    'i': 0.0625,
    'j': 0.0044,
    'k': 0.0002,
    'l': 0.0497,
    'm': 0.0315,
    'n': 0.0671,
    'ñ': 0.0031,
    'o': 0.0868,
    'p': 0.0251,
    'q': 0.0088,
    'r': 0.0687,
    's': 0.0798,
    't': 0.0463,
    'u': 0.0393,
    'v': 0.0090,
    'w': 0.0001,
    'x': 0.0022,
    'y': 0.0090,
    'z': 0.0052
}

# text = input("Ingresa el texto plano: ")

text = """Del buen suceso que el valeroso Don Quijote tuvo en la espantable y jamás imaginada aventura de los molinos de viento, con otros sucesos dignos de felice recordación

En esto, descubrieron treinta o cuarenta molinos de viento que hay en aquel campo, y así como Don Quijote los vio, dijo a su escudero:

—La ventura va guiando nuestras cosas mejor de lo que acertáramos a desear; porque ves allí, amigo Sancho Panza, donde se descubren treinta, o pocos más, desaforados gigantes, con quien pienso hacer batalla y quitarles a todos las vidas, con cuyos despojos comenzaremos a enriquecer.

—¿Qué gigantes? —dijo Sancho Panza.

—Aquellos que allí ves —respondió su amo—, de los brazos largos, que los suelen tener algunos de casi dos leguas.

—Mire vuestra merced —respondió Sancho— que aquellos que allí se parecen no son gigantes, sino molinos de viento, y lo que en ellos parecen brazos son las aspas, que, volteadas del viento, hacen andar la piedra del molino.

—Bien parece —respondió Don Quijote— que no estás cursado en esto de las aventuras. ¡Ellos son gigantes! Y si tienes miedo, quítate de ahí y ponte en oración, que yo voy a entrar con ellos en fiera y desigual batalla.

Y diciendo esto, dio de espuelas a su caballo Rocinante, sin atender a las voces que su escudero Sancho le daba, advirtiéndole que, sin duda, eran molinos de viento y no gigantes aquellos que iba a acometer.

Pero él iba tan puesto en que eran gigantes, que ni oía las voces de su escudero Sancho, ni echaba de ver, aunque estaba ya bien cerca, lo que eran. Antes bien, iba diciendo en voz alta:

—No huyáis, cobardes y viles criaturas, que un solo caballero es el que os acomete.

En esto, se levantó un poco de viento y las grandes aspas comenzaron a moverse. Viéndolo Don Quijote, dijo:

—Pues aunque mováis más brazos que los del gigante Briareo, me lo habéis de pagar.

Y diciendo esto, encomendándose de todo corazón a su señora Dulcinea, y pidiendo su favor, bien cubierto de su rodela y con la lanza en ristre, arremetió a todo galope de Rocinante y embistió con el primer molino que estaba delante.

Diole una lanzada en el aspa, pero el viento la hizo dar en la lanza con tanta fuerza que la hizo pedazos, llevando tras sí al caballo y al caballero, que rodaron por el campo, muy maltrechos.

Sancho Panza acudió a socorrerle a todo correr de su asno, y cuando llegó halló a Don Quijote sin poder moverse, tan grande fue el golpe que dio con él Rocinante.

—¡Válgame Dios! —dijo Sancho—. ¿No le dije yo a vuestra merced que mirase bien lo que hacía? Que no eran sino molinos de viento, y solo el viento lo podía haber vuelto a vuestra merced patas arriba.

—Calla, amigo Sancho —respondió Don Quijote—. Que las cosas de la guerra, más que otras, están sujetas a continua mudanza. Y, más que en mi opinión, aquel sabio Frestón, que me robó el aposento y los libros, ha convertido a estos gigantes en molinos para quitarme la gloria de su vencimiento."""

def compareFrequencies(text):
    experimental = getFrequencies(text)
    
    maxTheorical = max(theorical, key=theorical.get)
    maxExperimental = max(experimental, key=experimental.get)
    
    analysis = [[key,f"{theorical[key]} {"🌟" if maxTheorical == key else ""}",f"{experimental[key]} {"🌟" if maxExperimental == key else ""}"] for key, _ in theorical.items()]

    print("\n📊 FRECUENCIAS:")
    print(tabulate(analysis, headers=["Letra", "Frecuencia Teórica", "Frecuencia Experimental"], tablefmt="grid"))
    
    labels = list(theorical.keys())
    theoricalFrequencies = list(theorical.values())
    experimentalFrequencies = list(experimental.values())

    x = np.arange(len(labels))
    width = 0.5

    _, ax = plt.subplots()
    ax.bar(x - width/2, theoricalFrequencies, width, label="Frecuencias Teóricas", color="blue")
    ax.bar(x + width/2, experimentalFrequencies, width, label="Frecuencias Experimentales", color="orange")

    ax.set_xlabel("Caracteres")
    ax.set_ylabel("Frecuencias")
    ax.set_title("Distribución de frecuencias teóricas vs experimentales")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()
    

def getFrequencies(text):
    data = [["Letra","Frecuencia"]]
    frequencies = {}

    for letter in alphabet:
        frequency = text.lower().count(letter) / len(text)
        frequencies[letter] = frequency
        data.append([letter,frequency])

    return frequencies

compareFrequencies(text)