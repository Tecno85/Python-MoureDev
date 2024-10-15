# Solución 1:
sentence = ("No puedes terminar una oración con porque porque porque porque es una conjunción")
antes, separador, despues = sentence.partition("porque porque porque porque")
print(antes.strip() + " " + despues.strip())
# imprime: No puedes terminar una oración con es una conjunción

# Solución 2:
sentence = ("No puedes terminar una oración con porque porque porque porque es una conjunción")
new_sentence = sentence.replace("porque porque porque porque","").replace("  ", " ")
print(new_sentence.strip())
# imprime: No puedes terminar una oración con es una conjunción