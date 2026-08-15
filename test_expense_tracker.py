import pytest
from expense_tracker import (
    add_expense,
    total_expenses,
    filter_expenses_by_category,
)

def test_add_expense():
    """Valida que add_expense agregue correctamente un diccionario a la lista."""
    expenses = []
    add_expense(expenses, 50.0, "Comida")
    
    assert len(expenses) == 1
    assert expenses[0] == {"amount": 50.0, "category": "Comida"}

def test_total_expenses_empty():
    """Valida que total_expenses retorne 0.0 cuando la lista está vacía."""
    expenses = []
    assert total_expenses(expenses) == 0.0

@pytest.mark.parametrize(
    "expenses_list, expected_total",
    [
        ([{"amount": 10.0, "category": "Comida"}], 10.0),
        ([{"amount": 15.5, "category": "Transporte"}, {"amount": 20.0, "category": "Ocio"}], 35.5),
        ([{"amount": 100.0, "category": "Servicios"}, {"amount": 50.0, "category": "Comida"}, {"amount": 25.25, "category": "Otros"}], 175.25),
    ]
)
def test_total_expenses_parametrize(expenses_list, expected_total):
    """Evalúa el cálculo del monto total con diferentes conjuntos de datos usando @pytest.mark.parametrize."""
    assert total_expenses(expenses_list) == expected_total

def test_filter_expenses_by_category():
    """Confirma que filter_expenses_by_category retorne solo los diccionarios de la categoría consultada."""
    expenses = [
        {"amount": 15.0, "category": "Comida"},
        {"amount": 30.0, "category": "Transporte"},
        {"amount": 10.0, "category": "Comida"}
    ]
    
    filtered = filter_expenses_by_category(expenses, "Comida")
    
    assert len(filtered) == 2
    assert all(expense["category"] == "Comida" for expense in filtered)

def test_filter_expenses_non_existent_category():
    """Evalúa el comportamiento al filtrar por una categoría que no existe (debe devolver una lista vacía)."""
    expenses = [
        {"amount": 15.0, "category": "Comida"},
        {"amount": 30.0, "category": "Transporte"}
    ]
    
    filtered = filter_expenses_by_category(expenses, "Entretenimiento")
    
    assert filtered == []
    assert isinstance(filtered, list)