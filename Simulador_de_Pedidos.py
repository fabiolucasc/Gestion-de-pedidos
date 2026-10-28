from sys import exit

PORTES = 7.50
MINIMO_GRATIS = 150.00

cliente = {
190: "Policia",
191: "Bombeiro",
192: "Samu"   
}

print("Gestión de pedidos")
print("Menú:")
print("""1 - Registrar pedido
2 - Consultar pedido creado
3 - Cancelar pedido""")

proceso = int(input("Seleccionar: "))

if proceso == 1:
    fecha = input("Fecha de la solicitud: ")
    usuario = int(input("Usuario: "))

    if usuario != 6865:
        print("¡Usuario no autorizado!")
        exit()

    print("¡Bienvenido, Fabio! Puede continuar con el pedido.")
    print("")

    codigo = int(input("Código del cliente: "))
    if codigo in cliente:
        print("Cliente:", cliente[codigo])
    material = input("Material solicitado: ")
    valor = float(input("Valor del material: "))

    if valor < MINIMO_GRATIS:
        print("Aplicar portes.")
        gastos = input("No se ha alcanzado el valor mínimo. Se cobrarán portes en su envío. ¿Desea continuar? (si/no): ").lower()
        if gastos in ("si", "s"):
            precio_final = valor + PORTES
            print(f"Valor final del pedido: {precio_final:.2f}€")
            print("¡Pedido registrado con éxito!")
        else:
            print("Pedido cancelado.")
    else:
        print("Envío gratuito")
        print(f"Valor final del pedido: {valor:.2f}€")
        print("¡Pedido registrado con éxito!")

elif proceso in (2, 3):
    print("Todavía en desarrollo... :)")
else:
    print("Opción no válida.")