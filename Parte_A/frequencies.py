import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

print("-"*40)
print("ANÁLISIS DE FRECUENCIAS")
print("-"*40)

alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Frecuencias teóricas en español
theorical = {
    'a': 0.11525,
    'b': 0.02215,
    'c': 0.04019,
    'd': 0.05010,
    'e': 0.12181,
    'f': 0.00692,
    'g': 0.01768,
    'h': 0.00703,
    'i': 0.06247,
    'j': 0.00493,
    'k': 0.00011,
    'l': 0.04967,
    'm': 0.03157,
    'n': 0.06712,
    'ñ': 0.00311,
    'o': 0.08683,
    'p': 0.02510,
    'q': 0.00877,
    'r': 0.06871,
    's': 0.07977,
    't': 0.04632,
    'u': 0.02927,
    'v': 0.01138,
    'w': 0.00017,
    'x': 0.00215,
    'y': 0.01008,
    'z': 0.00467,
    'á': 0.00502,
    'é': 0.00433,
    'í': 0.00725,
    'ó': 0.00827,
    'ú': 0.00168,
    'ü': 0.00012
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

if __name__ == "__main__":
    compareFrequencies(text)