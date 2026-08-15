"""
Calculador de Gastos Personales (Expense Tracker)
Proyecto educativo para el uso de funciones lambda, filter() y sum().
"""

def add_expense(expenses: list, amount: float, category: str) -> list:
    """Agrega un nuevo gasto a la lista de gastos en formato de diccionario."""
    expenses.append({"amount": amount, "category": category})
    return expenses

def print_expenses(expenses: list) -> None:
    """Recorre y muestra en consola el listado completo de gastos."""
    if not expenses:
        print("No hay gastos registrados.")
        return
    
    print("\n--- Historial de Gastos ---")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Monto: ${expense['amount']:.2f} | Categoría: {expense['category']}")
    print("-" * 27)

def total_expenses(expenses: list) -> float:
    """Suma todos los montos registrados utilizando sum() y una expresión lambda."""
    return sum(map(lambda expense: expense["amount"], expenses))

def filter_expenses_by_category(expenses: list, category: str) -> list:
    """Retorna una nueva lista con los gastos que coincidan con la categoría,
    empleando filter() y una expresión lambda.
    """
    return list(filter(lambda expense: expense["category"].lower() == category.lower(), expenses))

def main():
    """Menú de consola interactivo para el gestor de gastos."""
    expenses = []

    while True:
        print("\n=== CALCULADOR DE GASTOS PERSONALES ===")
        print("1. Agregar gasto")
        print("2. Ver todos los gastos")
        print("3. Calcular gasto total")
        print("4. Filtrar gastos por categoría")
        print("5. Salir")

        option = input("Selecciona una opción (1-5): ").strip()

        if option == "1":
            try:
                amount = float(input("Ingresa el monto del gasto: "))
                if amount < 0:
                    print("El monto no puede ser negativo.")
                    continue
                category = input("Ingresa la categoría (ej. Comida, Transporte): ").strip()
                add_expense(expenses, amount, category)
                print("¡Gasto agregado con éxito!")
            except ValueError:
                print("Por favor, ingresa un valor numérico válido para el monto.")

        elif option == "2":
            print_expenses(expenses)

        elif option == "3":
            total = total_expenses(expenses)
            print(f"\nEl gasto total acumulado es: ${total:.2f}")

        elif option == "4":
            category = input("Ingresa la categoría a filtrar: ").strip()
            filtered = filter_expenses_by_category(expenses, category)
            if filtered:
                print_expenses(filtered)
            else:
                print(f"No se encontraron gastos en la categoría '{category}'.")

        elif option == "5":
            print("¡Gracias por usar el Calculador de Gastos Personales. Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona un número entre 1 y 5.")

if __name__ == "__main__":
    main()