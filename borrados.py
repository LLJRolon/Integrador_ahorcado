def seleccionar_categoria():
    global categoria_selec
    categoria_selec = categori("categorias")
    if categoria_selec:
        palabra_categoria = CATEGORIAS.get(categoria_selec)
    if palabra_categoria:
        palabra_secreta = random.choice(palabra_categoria)
        iniciar_juego(palabra_secreta)
    