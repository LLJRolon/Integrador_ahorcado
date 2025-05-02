import tkinter
from PIL import Image, ImageTk

ventana = tkinter.Tk()
ventana.title("Juego del ahorcado")
ventana.geometry("1280x650")

imagen_fondo = Image.open("algo_asi.png")  # Asegurate de que esté en la misma carpeta
imagen_fondo = imagen_fondo.resize((1280, 650))  # Ajustar tamaño a la ventana
fondo = ImageTk.PhotoImage(imagen_fondo)

label_fondo = tkinter.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

#label_texto = tkinter.Label(ventana, text="Juego del Ahorcado", font=("Arial", 20), bg= "white")
#label_texto.place(x=600, y=20)

etiqueta = tkinter.Label(ventana, text = "Bienvenido al juego del ahorcado", font=("Arial", 20), bg= "white")
etiqueta.place(x = 400, y = 20)

boton_iniciar = tkinter.Button(ventana, text = "Iniciar juego")
boton_iniciar.place(x = 450, y = 200)

#letra_elegida = tkinter.Entry(ventana, font = "Helvetica 20")    input con la letra
#letra_elegida.grid(row=3, column= 2)



ventana.mainloop()
