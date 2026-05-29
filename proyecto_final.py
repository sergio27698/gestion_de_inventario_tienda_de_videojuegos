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
def despedida():
    print("""
  +------------------------------------------+
  |                                          |
  |   ██████╗ ██╗   ██╗███████╗             |
  |   ██╔══██╗╚██╗ ██╔╝██╔════╝             |
  |   ██████╔╝ ╚████╔╝ █████╗               |
  |   ██╔══██╗  ╚██╔╝  ██╔══╝               |
  |   ██████╔╝   ██║   ███████╗             |

| ╚═════╝    ╚═╝   ╚══════╝ |
| :--- |
| Hasta luego!  [ Game Zone ] |

  +------------------------------------------+
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
            print("6. Salir al menu principal")
            opc_admin = input("Seleccione una opcion: ").strip()
            
            if opc_admin == "1":
                mostrar_catalogo()
                
            elif opc_admin == "2":
                nuevo_titulo = input("Nombre del videojuego: ").strip()
                if not nuevo_titulo:
                    print("Error: El nombre no puede estar vacio.")
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
                        print("Error: el stock no puede ser negativo.")
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
                print("Cerrando sesion de administrador...")
                break
            else:
                print("Opcion no valida.")
                
    elif r == "usuario":
        usuario_actual = None
        print("\n--- ACCESO DE USUARIOS ---")
        print("1. Iniciar Sesion")
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
                print(f"\nSesion iniciada correctamente!")
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
                        subtotal = juego_elegido["precio_usd"] * tipo_cambio_bs * cantidad
                        en_carrito = next((item for item in carrito if item["indice_original"] == seleccion), None)
                        if en_carrito:
                            en_carrito["cantidad"] += cantidad
                            en_carrito["subtotal"] += subtotal
                        else:
                            carrito.append({
                                "titulo":          juego_elegido["titulo"],
                                "cantidad":        cantidad,
                                "subtotal":        subtotal,
                                "indice_original": seleccion,
                            })
                        total_a_pagar_bs       += subtotal
                        juego_elegido["stock"] -= cantidad
                        print(f"\nAñadido! Total acumulado: {total_a_pagar_bs:.2f} Bs.")
                        
                        if input("Seguir comprando? (s/n): ").strip().lower() != "s":
                            break
                    else:
                        print("Stock insuficiente o cantidad invalida.")
                else:
                    print("Juego agotado.")
            else:
                print("Numero de juego no valido.")
                
        if carrito:
            print("\n========== RESUMEN DE COMPRA ==========")
            for item in carrito:
                print(f"  {item['titulo']} x{item['cantidad']}  ->  {item['subtotal']:.2f} Bs")
            print(f"  TOTAL: {total_a_pagar_bs:.2f} Bs")
            print("========================================")
            
            pago_str = input("Ingresa el monto a pagar en Bs (o escribe cancelar): ").strip().lower()
            if pago_str == "cancelar":
                restaurar_stock(carrito)
                print("Compra cancelada. Stock restaurado.")
            else:
                pago = float(pago_str)
                if pago >= total_a_pagar_bs:
                    print(f"\n  Cambio: {pago - total_a_pagar_bs:.2f} Bs.")
                    print("""
  +-----------------------------------------+
  |                                         |
  |   ██████╗ ██╗   ██╗███████╗             |
  |   ██╔══██╗╚██╗ ██╔╝██╔════╝             |
  |   ██████╔╝ ╚████╔╝ █████╗               |
  |   ██╔══██╗  ╚██╔╝  ██╔══╝               |
  |   ██████╔╝   ██║   ███████╗             |
  |   ╚═════╝    ╚═╝   ╚══════╝             |
  | Compra exitosa! Disfruta tu juego!      |
  | Vuelve pronto a Game Zone               |
  +-----------------------------------------+
                    """)
                else:
                    restaurar_stock(carrito)
                    print("Fondos insuficientes. Compra cancelada y stock restaurado.")
        else:
            print("\nGracias por visitarnos.")
