import pytest

from calculadora import calcular, main


@pytest.mark.parametrize(
    "numero1, numero2, opcion, esperado",
    [
        (10, 5, "1", 30),
        (-3, 2, "1", -1),
        (10, 5, "2", 5),
        (3, 8, "2", -5),
        (4, 3, "3", 12),
        (5, 0, "3", 0),
        (10, 2, "4", 5),
        (5, 2, "4", 2.5),
        (0.1, 0.2, "1", 0.3),
    ],
)
def test_operaciones(numero1, numero2, opcion, esperado):

    assert calcular(numero1, numero2, opcion) == pytest.approx(esperado)


def test_division_entre_cero():

    with pytest.raises(ZeroDivisionError):
        calcular(10, 0, "4")


def test_opcion_no_valida():

    with pytest.raises(ValueError):
        calcular(10, 5, "9")


def test_menu_suma_y_salida(monkeypatch, capsys):

    respuestas = iter(["1", "10", "5", "5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(respuestas)
    )

    main()

    salida = capsys.readouterr().out

    assert "Resultado: 15.0" in salida

    assert "Gracias por usar la calculadora." in salida