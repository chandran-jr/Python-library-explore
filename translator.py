from googletrans import Translator

# taking some text from our website in french language
text = '''Python est un langage de programmation interprété et de haut
            niveau qui a été créé à la fin des années 1980, mais il a été implémenté
            en décembre 1989 par Guido Van Rossum . Le mot Python vient du serpent.
            Selon la récente enquête de StackOverflow , Python a dépassé la popularité de Java'''

# Creating an instance of Translator to use
# Google Translate ajax API
translator = Translator()

# detect- auto detects language of the input text
dt = translator.detect(text)
print(dt)

# translate()-translates the text from source language to destination language
# translate(self, text, dest='en', src='auto', **kwargs)
# if we don't specify the dest(destination language) then
# it translates to english
translated = translator.translate(text)

print(translated.text
