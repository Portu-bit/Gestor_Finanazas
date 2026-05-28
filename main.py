#crear un menu en la terminal donde el ususario pueda elegir entre agregar un ingreso, agregar un gasto, ver el balance o exportar las transacciones a un archivo csv
def mostrar_menu():
    print("1. Agregar ingreso")
    print("2. Agregar gasto")
    print("3. Ver balance")
    print("4. Ver Historial de transacciones")
    print("5. Exportar transacciones a CSV")
    print("6. Salir")

def main():
    from finanzas.src.database import crear_tabla_transacciones
    from finanzas.src.transacciones import GestorFinanzas
    from finanzas.src.reportes import exportar_csv
    crear_tabla_transacciones()
    gestor = GestorFinanzas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            monto = float(input("Ingrese el monto del ingreso: "))
            descripcion = input("Ingrese la descripción del ingreso: ")
            try:
                gestor.agregar_ingreso(monto, descripcion)
                print("Ingreso agregado exitosamente.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif opcion == '2':
            monto = float(input("Ingrese el monto del gasto: "))
            descripcion = input("Ingrese la descripción del gasto: ")
            try:
                gestor.agregar_gasto(monto, descripcion)
                print("Gasto agregado exitosamente.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif opcion == '3':
            balance = gestor.obtener_balance()
            print(f"Balance actual: {balance:.2f}")
        
        elif opcion == '4':
            transacciones = gestor.obtener_transacciones()
            for transaccion in transacciones:
                print(f"ID: {transaccion[0]}, Fecha: {transaccion[1]}, Tipo: {transaccion[2]}, Monto: {transaccion[3]:.2f}, Descripción: {transaccion[4]}")
        elif opcion == '5':
            nombre_archivo = input("Ingrese el nombre del archivo CSV (ejemplo: transacciones.csv): ")
            exportar_csv(nombre_archivo)
            print(f"Transacciones exportadas a {nombre_archivo} exitosamente.")
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")


if __name__ == "__main__":
    main()