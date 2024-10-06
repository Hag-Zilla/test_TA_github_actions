import pytest

def test_calc_addition():
    """
    Teste l'addition de deux nombres.

    Assure que l'addition de 2 et 4 donne bien 6.

    Exemple :
        >>> test_calc_addition()
    """
    output = 2 + 4
    assert output == 6

def test_calc_substraction():
    """
    Teste la soustraction de deux nombres.

    Assure que la soustraction de 4 à 2 donne bien -2.

    Exemple :
        >>> test_calc_substraction()
    """
    output = 2 - 4
    assert output == -2

def test_calc_multiply():
    """
    Teste la multiplication de deux nombres.

    Assure que la multiplication de 2 par 4 donne bien 8.

    Exemple :
        >>> test_calc_multiply()
    """
    output = 2 * 4
    assert output == 8

def test_coucou():
    """
    Teste le retour de la chaîne de caractères 'hello'.

    Assure que la fonction retourne bien la chaîne 'hello'.

    Exemple :
        >>> test_coucou()
    """
    output = 'hello'
    assert output == 'hello'
