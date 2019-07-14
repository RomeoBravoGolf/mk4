n = int(input('cantidad de fotos a ingresar'))


file = open("file.txt", "w+")

for i in range(n):
	nombre = input("ingresar nombres")
	text = """ 
{} = face_recognition.load_image_file("{}.jpg")
{}_encoding = face_recognition.face_encodings({})[0] 
""".format(nombre, nombre, nombre, nombre)
	file.write(text)

file.close()