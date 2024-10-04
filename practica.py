# **15. Soy profesora y me encanta inspirar y enseñar a la gente. (I am a teacher and I love to inspire and teach people). ¿Cuántas palabras únicas se han utilizado en la oración?. Utilice los métodos de división (split()) y conjunto (set()) para obtener las palabras únicas.**

# Frase Inicial
frase = "I am a teacher and I love to inspire and teach people"
print("Frase original: ", frase)

# División de frase en palabras
frase_dividida = frase.split()
print("Palabras divididas: ", frase_dividida)

# Creación de conjunto de palabras únicas
set_de_frase = set(frase_dividida)
print("Palabras únicas: ", set_de_frase)

# Conteo de palabras únicas
cantidad_unicas = len(set_de_frase)
print(cantidad_unicas)
