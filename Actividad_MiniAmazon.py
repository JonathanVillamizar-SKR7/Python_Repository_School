# Jonathan Villamizar
# DAM 2

# Actividad Mini Amazon (Loops y funciones)


# Datos iniciales proporcionados por la empresa
CATALOGO = {
    "A001": {"nombre": "Teclado Mecánico", "precio": 49.99, "stock": 10, "peso_kg": 0.9},
    "A002": {"nombre": "Ratón Gaming", "precio": 25.50, "stock": 5, "peso_kg": 0.2},
    "A003": {"nombre": "Monitor 24\"", "precio": 149.00, "stock": 3, "peso_kg": 3.5},
    "A004": {"nombre": "Auriculares", "precio": 35.99, "stock": 0, "peso_kg": 0.4},
    "A005": {"nombre": "Webcam HD", "precio": 39.90, "stock": 7, "peso_kg": 0.3},
}

CODIGOS_PROMO = {
    "ENVIOFREE": {"tipo": "envio", "descuento": 1.0}, # 100% descuento en envio
    "DESC10": {"tipo": "total", "descuento": 0.10},   # 10% descuento en total
}

# DEFINICIÓN DE FUNCIONES

def mostrar_catalogo(catalogo):
    # Recorro el diccionario del catalogo para mostrar los productos disponibles
    print("\nCATÁLOGO DE PRODUCTOS")
    for codigo, info in catalogo.items():
        print(f"Cod: {codigo} | {info['nombre']} | Precio: {info['precio']}E | Stock: {info['stock']}")

def validar_codigo_producto(catalogo, codigo):
    # Utilizo un bucle for-else para verificar si el código existe en las claves del catálogo
    for key in catalogo:
        if key == codigo:
            return True
    else:
        # Este else se ejecuta si el bucle termina sin encontrar el producto (sin haber hecho return True)
        print("Error: El código de producto no existe.")
        return False

def agregar_al_carrito(carrito, catalogo, codigo, cantidad):
    # Verifico si hay suficiente stock antes de añadir
    stock_actual = catalogo[codigo]["stock"]
    
    if cantidad > stock_actual:
        print(f"No hay suficiente stock. Solo quedan {stock_actual} unidades.")
        return carrito

    # Si el producto ya está en el carrito, sumo la cantidad, si no, lo creo
    if codigo in carrito:
        carrito[codigo] += cantidad
    else:
        carrito[codigo] = cantidad
    
    print(f"Se han añadido {cantidad} unidades de {catalogo[codigo]['nombre']} al carrito.")
    return carrito

def calcular_totales(carrito, catalogo, iva=0.21):
    # Calculo el subtotal, el peso total para el envío y el total con IVA
    # Uso un valor por defecto para el IVA del 21%
    subtotal = 0
    peso_total = 0
    
    for codigo, cantidad in carrito.items():
        precio_unitario = catalogo[codigo]["precio"]
        peso_unitario = catalogo[codigo]["peso_kg"]
        
        subtotal += precio_unitario * cantidad
        peso_total += peso_unitario * cantidad

    impuestos = subtotal * iva
    total = subtotal + impuestos
    
    # Devuelvo un diccionario con todos los cálculos necesarios
    return {
        "subtotal": subtotal,
        "impuestos": impuestos,
        "total": total,
        "peso_total": peso_total
    }

def calcular_envio(peso_total, zona="PENINSULA"):
    # Calculo el coste de envío basándome en el peso
    coste_base = 5.0
    
    if peso_total <= 1:
        coste = coste_base
    elif peso_total <= 5:
        coste = coste_base + 5.0
    else:
        coste = coste_base + 10.0
        
    return coste

def aplicar_promos(total, envio, *codigos):
    # Uso *args para recibir una cantidad variable de códigos promocionales
    descuento_total = 0
    descuento_envio = 0
    
    print("\nProcesando cupones...")
    
    for codigo in codigos:
        if codigo in CODIGOS_PROMO:
            info_promo = CODIGOS_PROMO[codigo]
            
            if info_promo["tipo"] == "total":
                monto_desc = total * info_promo["descuento"]
                descuento_total += monto_desc
                print(f"Cupón {codigo} aplicado: -{monto_desc:.2f}E")
                
            elif info_promo["tipo"] == "envio":
                monto_desc = envio * info_promo["descuento"]
                descuento_envio += monto_desc
                print(f"Cupón {codigo} aplicado: Descuento en envío")
        else:
            print(f"El cupón {codigo} no es válido.")

    nuevo_total = total - descuento_total
    nuevo_envio = envio - descuento_envio
    
    # Me aseguro de que los precios no sean negativos
    if nuevo_envio < 0: nuevo_envio = 0
    if nuevo_total < 0: nuevo_total = 0
    
    return nuevo_total, nuevo_envio

# FUNCIÓN PRINCIPAL

def main():
    carrito = {}
    historial_pedidos = [] # Aquí guardaré los pedidos confirmados o cancelados
    continuar = True

    print("Bienvenido al sistema de gestión de pedidos Mini Amazon")

    # Bucle principal del menú
    while continuar:
        print("\nMENÚ PRINCIPAL")
        print("1. Ver catálogo")
        print("2. Añadir producto al carrito")
        print("3. Quitar producto del carrito")
        print("4. Ver carrito")
        print("5. Confirmar pedido")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_catalogo(CATALOGO)

        elif opcion == "2":
            codigo = input("Introduce el código del producto (ej. A001): ").upper()
            
            # Uso continue si la validación falla para volver al inicio del while
            if not validar_codigo_producto(CATALOGO, codigo):
                continue
                
            try:
                cantidad = int(input("Introduce la cantidad: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                    continue
            except ValueError:
                print("Error: Debes introducir un número entero.")
                continue

            agregar_al_carrito(carrito, CATALOGO, codigo, cantidad)

        elif opcion == "3":
            # Opción para quitar elementos del carrito
            codigo = input("Código a eliminar: ").upper()
            if codigo in carrito:
                del carrito[codigo]
                print("Producto eliminado del carrito.")
            else:
                print("Ese producto no está en tu carrito.")

        elif opcion == "4":
            print("\n--- CONTENIDO DEL CARRITO ---")
            if not carrito:
                print("El carrito está vacío.")
            else:
                for cod, cant in carrito.items():
                    nombre = CATALOGO[cod]['nombre']
                    print(f"- {nombre}: {cant} unidades")

        elif opcion == "5":
            if not carrito:
                print("No puedes confirmar un pedido vacío.")
                continue

            # Cálculos iniciales
            datos_totales = calcular_totales(carrito, CATALOGO)
            coste_envio = calcular_envio(datos_totales["peso_total"])
            
            total_pagar = datos_totales["total"]
            
            print(f"\nSubtotal (con IVA): {total_pagar:.2f}E")
            print(f"Gastos de envío estimados: {coste_envio:.2f}E")
            
            # Preguntar por promociones
            tiene_promo = input("¿Tienes códigos promocionales? (s/n): ").lower()
            if tiene_promo == "s":
                entrada_codigos = input("Introduce los códigos separados por espacio: ").upper()
                lista_codigos = entrada_codigos.split()
                # Llamo a la función con *args desmpaquetando la lista
                total_pagar, coste_envio = aplicar_promos(datos_totales["total"], coste_envio, *lista_codigos)
            
            total_final = total_pagar + coste_envio
            
            print(f"\nRESUMEN FINAL")
            print(f"Total a pagar: {total_final:.2f}E")
            
            confirmar = input("¿Confirmar pedido? (s/n): ").lower()
            
            if confirmar == "s":
                # Proceso de confirmación: Restar stock
                for cod, cant in carrito.items():
                    CATALOGO[cod]["stock"] -= cant
                
                # Guardo en historial
                historial_pedidos.append({"estado": "CONFIRMADO", "total": total_final, "productos": carrito.copy()})
                print("¡Pedido confirmado exitosamente!")
                carrito.clear() # Vacío el carrito para la próxima compra
            else:
                historial_pedidos.append({"estado": "CANCELADO", "total": total_final})
                print("Pedido cancelado.")

        elif opcion == "0":
            continuar = False # Cambio la bandera para salir del bucle while
            
        else:
            print("Opción no reconocida, por favor intenta de nuevo.")
            
    else:
        # Bloque while-else: Se ejecuta cuando el while termina normalmente (cuando continuar es False)
        # Aquí genero el informe final solicitado
        print("\nINFORME DE CIERRE DE SESIÓN")
        
        # Uso for-else para verificar si hubo ventas
        ventas_confirmadas = 0
        for pedido in historial_pedidos:
            print(f"Pedido: {pedido['estado']} | Importe: {pedido.get('total', 0):.2f}E")
            if pedido['estado'] == "CONFIRMADO":
                ventas_confirmadas += 1
        else:
            # Este bloque del for se ejecuta al terminar de recorrer la lista
            if ventas_confirmadas == 0:
                print("Nota: No se han registrado ventas confirmadas en esta sesión.")
            else:
                print(f"Total de ventas confirmadas: {ventas_confirmadas}")

    print("Gracias por usar el sistema Mini Amazon. ¡Hasta pronto!")

# Punto de entrada del script
if __name__ == "__main__":
    main()