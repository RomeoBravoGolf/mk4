from textblob import TextBlob
from googletrans import Translator

translator = Translator()

x = input('ingrese frase: ')

xx = translator.translate(x, dest='en')

testo = TextBlob(xx.text)

#polaridad: -1 malo +1 bueno
#subjetividad: 0 subj 1 obj
print(testo)
print("polaridad: -1 malo +1 bueno, subjetividad: 0 subj 1 obj")
print(testo.sentiment)
