pines_admin = ["27698", "12345", "99999"]
tipo_cambio_bs = 6.96
inventario = [
    {"titulo": "FIFA 26",        "precio_usd": 60.0, "stock": 10},
    {"titulo": "GTA V",          "precio_usd": 30.0, "stock": 5},
    {"titulo": "Cyberpunk 2077", "precio_usd": 45.0, "stock": 8},
    {"titulo": "Elden Ring",     "precio_usd": 50.0, "stock": 12},
    {"titulo": "Minecraft",      "precio_usd": 20.0, "stock": 15},
]
usuarios_registrados = {"invitado": "55555"}
registro_ventas = []

def mostrar_catalogo():
    print("\n==================================================")
    print("               CATALOGO DE JUEGOS                ")
    print("==================================================")
    for i, juego in enumerate(inventario, 1):
        precio_bs = juego["precio_usd"] * tipo_cambio_bs
        print(f"{i}. {juego['titulo']} | ${juego['precio_usd']:.2f} USD ({precio_bs:.2f} Bs) | Stock: {juego['stock']}")
    print("==================================================")

def restaurar_stock(carrito):
    for item in carrito:
        inventario[item["indice_original"]]["stock"] += item["cantidad"]

def mostrar_registro_ventas():
    print("\n========== REGISTRO DE VENTAS ==========")
    if not registro_ventas:
        print("  No hay ventas registradas aun.")
    else:
        for i, venta in enumerate(registro_ventas, 1):
            print(f"\n  Venta #{i} | Usuario: {venta['usuario']}")
            for item in venta["items"]:
                print(f"    - {item['titulo']} x{item['cantidad']}  ->  ${item['subtotal_usd']:.2f} USD  ({item['subtotal']:.2f} Bs)")
            print(f"    TOTAL PAGADO: {venta['total_bs']:.2f} Bs (${venta['total_usd']:.2f} USD) | Cambio: {venta['cambio_bs']:.2f} Bs")
    print("=========================================")

def despedida():
    print("""
  +-----------------------------------------+
  |                                         |
  |   ██████╗ ██╗   ██╗███████╗             |
  |   ██╔══██╗╚██╗ ██╔╝██╔════╝             |
  |   ██████╔╝ ╚████╔╝ █████╗               |
  |   ██╔══██╗  ╚██╔╝  ██╔══╝               |
  |   ██████╔╝   ██║   ███████╗             |
  |   ╚═════╝    ╚═╝   ╚══════╝             |
  |    Hasta luego   Game Zone              |
  +-----------------------------------------+
    """)

print("""
============
[GAME ZONE]
============
""")

while True:
    r = ""
    while r not in ("admin", "usuario", "salir"):
        r = input("Ingresar como Admin, Usuario o Salir: ").strip().lower()
        if r not in ("admin", "usuario", "salir"):
            print("Error. Escribe Admin, Usuario o Salir.")

    if r == "salir":
        despedida()
        break

    elif r == "admin":
        acceso = False
        while not acceso:
            pin = input("Introduce el pin de seguridad: ").strip()
            if pin in pines_admin:
                print("\n===============================\n[Bienvenido Admin de Game Zone]\n===============================")
                acceso = True
            else:
                print("Pin incorrecto. Intente de nuevo.")

        while True:
            print(f"\n--- PANEL DE ADMINISTRACION | Tasa: {tipo_cambio_bs} Bs/USD ---")
            print("1. Ver catalogo actual")
            print("2. Añadir nuevo juego")
            print("3. Eliminar un juego")
            print("4. Modificar stock de un juego")
            print("5. Actualizar tipo de cambio")
            print("6. Ver registro de ventas")
            print("7. Salir al menu principal")
            opc_admin = input("Seleccione una opcion: ").strip()

            if opc_admin == "1":
                mostrar_catalogo()

            elif opc_admin == "2":
                nuevo_titulo = input("Nombre del videojuego: ").strip()
                if not nuevo_titulo:
                    print("Error: El nombre no puede estar vacio.")
                    continue

                nuevo_titulo = nuevo_titulo.title()

      usuario = input("Ingrese el usuario: ")
while usuario.strip().lower() != "fin":
    usuario = input("Ingrese el usuario: ")

        comentario_invalido = True
while comentario_invalido:
    comentario = input("Ingresa un comentario sobre el producto: ")
    if "malo" in comentario.lower():
        print("Tu comentario no cumple con las normas, intenta de nuevo.")
    else:
        print("Comentario publicado con éxito.")
        comentario_invalido = False
        
        frase = input("Ingresa una frase: ")
if "triste" in frase.lower():
    print(frase.lower().replace("triste", "feliz"))
else:
    print(frase.upper())

contrasena = input("Ingresa una contraseña: ")
insegura = True

while insegura:
    if contrasena.strip() == "12345":
        contrasena = input("Contraseña insegura, ingresa otra: ")
    else:
        insegura = False

print("Acceso concedido")

  titulos_existentes = [j["titulo"].lower() for j in inventario]
                if nuevo_titulo.lower() in titulos_existentes:
                    print(f"Error: '{nuevo_titulo}' ya existe en el catalogo.")
                    continue

                nuevo_precio = float(input("Precio en USD: "))
                nuevo_stock  = int(input("Stock inicial: "))
                if nuevo_precio <= 0 or nuevo_stock < 0:
                    print("Error: valores deben ser positivos.")
                else:
                    inventario.append({"titulo": nuevo_titulo, "precio_usd": nuevo_precio, "stock": nuevo_stock})
                    print(f"'{nuevo_titulo}' añadido.")

            elif opc_admin == "3":
                mostrar_catalogo()
                indice = int(input("Numero del juego a eliminar: ")) - 1
                if 0 <= indice < len(inventario):
                    eliminado = inventario.pop(indice)
                    print(f"'{eliminado['titulo']}' eliminado.")
                else:
                    print("Numero no valido.")

            elif opc_admin == "4":
                mostrar_catalogo()
                indice = int(input("Numero del juego para modificar stock: ")) - 1
                if 0 <= indice < len(inventario):
                    nuevo_stock = int(input(f"Nuevo stock para '{inventario[indice]['titulo']}': "))
                    if nuevo_stock < 0:
                        print("Error.")
                    else:
                        inventario[indice]["stock"] = nuevo_stock
                        print("Stock actualizado.")
                else:
                    print("Numero no valido.")

            elif opc_admin == "5":
                nueva_tasa = float(input("Nueva tasa en Bs: "))
                if nueva_tasa <= 0:
                    print("Error: la tasa debe ser mayor a 0.")
                else:
                    tipo_cambio_bs = nueva_tasa
                    print(f"Tasa actualizada a {tipo_cambio_bs}.")

            elif opc_admin == "6":
                mostrar_registro_ventas()

            elif opc_admin == "7":
                print("Cerrando sesion de administrador")
                break
            else:
                print("Opcion no valida.")

    elif r == "usuario":
        usuario_actual = None
        print("\n--- ACCESO DE USUARIOS ---")
        print("1. Iniciar Sesion o como Invitado(User:invitado ; Contraseña:55555)")
        print("2. Registrar nuevo usuario")
        opc_usuario = input("Seleccione una opcion: ").strip()

        if opc_usuario == "2":
            print("\n--- REGISTRO ---")
            while True:
                nuevo_usuario = input("Nombre de usuario: ").strip()
                if nuevo_usuario == "":
                    print("El nombre no puede estar vacio.")
                elif nuevo_usuario in usuarios_registrados:
                    print("Ese usuario ya existe. Elige otro.")
                else:
                    break
            while True:
                nueva_contrasena = input("Contrasena (min. 4 caracteres): ").strip()
                if len(nueva_contrasena) < 4:
                    print("La contrasena debe tener al menos 4 caracteres.")
                else:
                    confirmar = input("Confirma la contrasena: ").strip()
                    if confirmar != nueva_contrasena:
                        print("Las contrasenas no coinciden.")
                    else:
                        break
            usuarios_registrados[nuevo_usuario] = nueva_contrasena
            print(f"\nRegistro exitoso! Ahora inicia sesion.")

        print("\n--- INICIO DE SESION ---")
        intentos = 3
        while intentos > 0:
            nombre = input("Usuario: ").strip()
            clave  = input("Contrasena: ").strip()
            if nombre in usuarios_registrados and usuarios_registrados[nombre] == clave:
                usuario_actual = nombre
                print(f"\nSesion iniciada correctamente")
                break
            else:
                intentos -= 1
                print(f"Datos incorrectos. Intentos restantes: {intentos}")

        if usuario_actual is None:
            print("Demasiados intentos fallidos. Volviendo al inicio.")
            continue

        print(f"\n=================================\n[Bienvenido, {usuario_actual}!]\n=================================")
        carrito = []
        total_a_pagar_bs = 0.0

        while True:
            mostrar_catalogo()
            seleccion = int(input("\nIntroduce el numero del juego (o 0 para salir): ")) - 1
            if seleccion == -1:
                break

            if 0 <= seleccion < len(inventario):
                juego_elegido = inventario[seleccion]
                if juego_elegido["stock"] > 0:
                    cantidad = int(input(f"Cuantas copias? (Stock: {juego_elegido['stock']}): "))
                    if 0 < cantidad <= juego_elegido["stock"]:
                        subtotal     = juego_elegido["precio_usd"] * tipo_cambio_bs * cantidad
                        subtotal_usd = juego_elegido["precio_usd"] * cantidad
                        en_carrito = next((item for item in carrito if item["indice_original"] == seleccion), None)
                        if en_carrito:
                            en_carrito["cantidad"]     += cantidad
                            en_carrito["subtotal"]     += subtotal
                            en_carrito["subtotal_usd"] += subtotal_usd
                        else:
                            carrito.append({
                                "titulo":          juego_elegido["titulo"],
                                "cantidad":        cantidad,
                                "subtotal":        subtotal,
                                "subtotal_usd":    subtotal_usd,
                                "indice_original": seleccion,
                            })
                        total_a_pagar_bs       += subtotal
                        total_a_pagar_usd       = sum(item["subtotal_usd"] for item in carrito)
                        juego_elegido["stock"] -= cantidad
                        print(f"\nAñadido! Total acumulado: ${total_a_pagar_usd:.2f} USD  ({total_a_pagar_bs:.2f} Bs).")

                        if input("Seguir comprando? (Si/No): ").strip().lower() != "si":
                            break
                    else:
                        print("Stock insuficiente o cantidad invalida.")
                else:
                    print("Juego agotado.")
            else:
                print("Numero de juego no valido.")

        if carrito:
            total_usd = sum(item["subtotal_usd"] for item in carrito)
            print("\n========== RESUMEN DE COMPRA ==========")
            for item in carrito:
                print(f"  {item['titulo']} x{item['cantidad']}  ->  ${item['subtotal_usd']:.2f} USD  ({item['subtotal']:.2f} Bs)")
            print(f"  TOTAL: ${total_usd:.2f} USD  ({total_a_pagar_bs:.2f} Bs)")
            print("========================================")

            moneda = ""
            while moneda not in ("bs", "usd"):
                moneda = input("Pagar en (Bs/USD): ").strip().lower()
                if moneda not in ("bs", "usd"):
                    print("Escribe Bs o USD.")

            pago_str = input(f"Ingresa el monto en {'Bs' if moneda == 'bs' else 'USD'} (o escribe cancelar): ").strip().lower()
            if pago_str == "cancelar":
                restaurar_stock(carrito)
                print("Compra cancelada. Stock restaurado.")
            else:
                pago_ingresado = float(pago_str)
                pago_en_bs = pago_ingresado if moneda == "bs" else pago_ingresado * tipo_cambio_bs

                if pago_en_bs >= total_a_pagar_bs:
                    cambio_bs  = pago_en_bs - total_a_pagar_bs
                    cambio_usd = cambio_bs / tipo_cambio_bs
                    print("\n========== RESUMEN DE PAGO ==========")
                    for item in carrito:
                        print(f"  {item['titulo']} x{item['cantidad']}  ->  ${item['subtotal_usd']:.2f} USD  ({item['subtotal']:.2f} Bs)")
                    print(f"  TOTAL:          ${total_usd:.2f} USD  ({total_a_pagar_bs:.2f} Bs)")
                    if moneda == "bs":
                        print(f"  MONTO PAGADO:   {pago_ingresado:.2f} Bs")
                        print(f"  CAMBIO:         {cambio_bs:.2f} Bs  (${cambio_usd:.2f} USD)")
                    else:
                        print(f"  MONTO PAGADO:   ${pago_ingresado:.2f} USD  ({pago_en_bs:.2f} Bs)")
                        print(f"  CAMBIO:         ${cambio_usd:.2f} USD  ({cambio_bs:.2f} Bs)")
                    print("=======================================")

                    registro_ventas.append({
                        "usuario":   usuario_actual,
                        "items":     carrito,
                        "total_bs":  total_a_pagar_bs,
                        "total_usd": total_usd,
                        "cambio_bs": cambio_bs,
                    })

                    print("""
  +-----------------------------------------+
  |                                         |
  |   ██████╗ ██╗   ██╗███████╗             |
  |   ██╔══██╗╚██╗ ██╔╝██╔════╝             |
  |   ██████╔╝ ╚████╔╝ █████╗               |
  |   ██╔══██╗  ╚██╔╝  ██╔══╝               |
  |   ██████╔╝   ██║   ███████╗             |
  |   ╚═════╝    ╚═╝   ╚══════╝             |
  | Compra exitosa Disfruta tu juego        |
  | Vuelve pronto a Game Zone               |
  +-----------------------------------------+
                    """)
                else:
                    restaurar_stock(carrito)
                    print("Saldo insuficiente. Compra cancelada y stock restaurado.")
        else:
            print("\nGracias por visitarnos.")
