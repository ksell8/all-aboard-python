"""
Pruebas para la función sort_dicts_by_key.
"""
import pytest

from code_to_test import sort_dicts_by_key, OrdenarError, ValorError, TipoError


class TestSortDictsByKey:

    @pytest.mark.unit
    @pytest.mark.happy_path
    def test_sort_by_numeric_key(self):
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35}
        ]
        result = sort_dicts_by_key(data, "age")
        assert result[0]["age"] == 25
        assert result[1]["age"] == 30
        assert result[2]["age"] == 35

    @pytest.mark.unit
    @pytest.mark.happy_path
    def test_sort_by_string_key(self):
        data = [
            {"name": "Charlie", "score": 100},
            {"name": "Alice", "score": 95},
            {"name": "Bob", "score": 90}
        ]
        result = sort_dicts_by_key(data, "name")
        assert result[0]["name"] == "Alice"
        assert result[1]["name"] == "Bob"
        assert result[2]["name"] == "Charlie"

    @pytest.mark.unit
    @pytest.mark.happy_path
    def test_sort_reverse_order(self):
        data = [
            {"product": "A", "price": 10},
            {"product": "B", "price": 30},
            {"product": "C", "price": 20}
        ]
        result = sort_dicts_by_key(data, "price", reverse=True)
        assert result[0]["price"] == 30
        assert result[1]["price"] == 20
        assert result[2]["price"] == 10

    @pytest.mark.unit
    @pytest.mark.exception
    def test_missing_key_raises_error(self):
        """Prueba que una clave que no se existe en un diccionario echa OrdenarError."""
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob"},
            {"name": "Charlie", "age": 35}
        ]
        with pytest.raises(OrdenarError):
            sort_dicts_by_key(data, "age")

    @pytest.mark.unit
    @pytest.mark.exception
    def test_unsortable_values_raises_error(self):
        """Prueba que tipos incompatibles echa OrdenarError."""
        data = [
            {"id": 1, "value": 10},
            {"id": 2, "value": "string"},
            {"id": 3, "value": 30}
        ]
        with pytest.raises(OrdenarError):
            sort_dicts_by_key(data, "value")

    @pytest.mark.unit
    @pytest.mark.exception
    def test_empty_list_raises_error(self):
        """Prueba que una lista vacia echa ValorError."""
        with pytest.raises(ValorError):
            sort_dicts_by_key([], "key")

    @pytest.mark.unit
    @pytest.mark.exception
    def test_non_list_input_raises_error(self):
        """Prueba que si la entrada no es una lista, echa TipoError."""
        with pytest.raises(TipoError):
            sort_dicts_by_key({"not": "a list"}, "key")

    @pytest.mark.unit
    @pytest.mark.exception
    def test_non_dict_items_raise_error(self):
        """Prueba que una lista con no-diccionarios echa ValorError."""
        data = [
            {"name": "Alice"},
            "not a dict",
            {"name": "Charlie"}
        ]
        with pytest.raises(ValorError):
            sort_dicts_by_key(data, "name")

    @pytest.mark.unit
    @pytest.mark.exception
    def test_none_values(self):
        """Prueba que None echa OrdenarError."""
        data = [
            {"id": 1, "value": 10},
            {"id": 2, "value": None},
            {"id": 3, "value": 30}
        ]
        with pytest.raises(OrdenarError):
            sort_dicts_by_key(data, "value")

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_mixed_numeric_types(self):
        """Prueba que una lista con tipos diferentes que pueden comparar es ordenado."""
        data = [
            {"id": 1, "score": 10.5},
            {"id": 2, "score": 5},
            {"id": 3, "score": 20}
        ]
        result = sort_dicts_by_key(data, "score")
        assert result[0]["score"] == 5
        assert result[1]["score"] == 10.5
        assert result[2]["score"] == 20

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_single_item_list(self):
        data = [{"name": "Alice", "age": 30}]
        result = sort_dicts_by_key(data, "age")
        assert len(result) == 1
        assert result[0]["age"] == 30

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_original_list_unchanged(self):
        """Prueba que la lista original no cambia."""
        data = [
            {"name": "Charlie", "age": 35},
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]
        original_first = data[0]["name"]
        result = sort_dicts_by_key(data, "age")

        # La lista original es la misma
        assert data[0]["name"] == original_first
        # La salida es ordenado
        assert result[0]["name"] == "Bob"
