import pytest
from string_utils import StringUtils


# Функция capitilize принимает на вход текст, делает первую букву заглавной и возвращает этот же текст

@pytest.mark.parametrize("input_string, expected_result", [
    ("maria", "Maria"),
    ("алла", "Алла"),
    ("Anton", "Anton"),
    ("生 き が い", "生 き が い"),
    ("    ", "    "),
    ("12345", "12345"),
    ("%%%%%%%%", "%%%%%%%%"),
    ("", "")
    ])
def test_capitilize(input_string, expected_result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == expected_result



# Функция trim принимает на вход текст и удаляет пробелы в начале, если они есть

@pytest.mark.parametrize("input_string, expected_result", [
    (" Moon", "Moon"),
    (" стол", "стол"),
    (" 12345", "12345"),
    (" !!!!!", "!!!!!"),
    ("sun", "sun"),
    ("     ", ""),
    ("", "")
    ])
def test_trim(input_string, expected_result):
    string_utils = StringUtils()
    res = string_utils.trim(input_string)
    assert res == expected_result



# Функция to_list принимает на вход текст с разделителем и возвращает список строк

@pytest.mark.parametrize("input_string, delimiter, expected_result", [
    ("а,Б,в,Г", None, ["а", "Б", "в", "Г"]),
    ("1!2!3", "!", ["1", "2", "3"]),
    ("1:-)2:-)3", ":-)", ["1", "2", "3"]),
    ("1a2a3", "a", ["1", "2", "3"]),
    ("aa,bb,cc", None, ["aa", "bb", "cc"]),
    ("生,き,が,い", None, ["生", "き", "が", "い"]),
    ("", None, []),
    (" , , ", None, [" ", " ", " "]),
    ])
def test_to_list(input_string, delimiter, expected_result):
    string_utils = StringUtils()
    if delimiter is None:
        res = string_utils.to_list(input_string)
    else:
        res = string_utils.to_list(input_string, delimiter)
    assert res == expected_result



# Функция contains возвращает `True`, если строка содержит искомый символ и `False` - если нет

@pytest.mark.parametrize("input_string, symbol, expected_result", [
    ("Moon", "oo", True),
    ("Moon", "m", False),
    ("Круг", "э", False),
    ("12345", "5", True),
    ("%^#@!", "!", True),
    ("生,き,が,い", "生", True),
    ("     ", " ", True),
    ("", "s", False)
    ])
def test_contains(input_string, symbol, expected_result):
    string_utils = StringUtils()
    res = string_utils.contains(input_string, symbol)
    assert res == expected_result



# Функция delete_symbol удаляет все подстроки из переданной строки

@pytest.mark.parametrize("input_string, symbol, expected_result", [
    ("Moon", "oo", "Mn"),
    ("Круг", "э", "Круг"),
    ("10 декабря", " ", "10декабря"),
    ("3555", "5","3"),
    ("%<#@!", "<","%#@!"),
    ("生,き,が,い", "生,", "き,が,い" ),
    ("     ", " ", "" ),
    ("", "", "")
    ])
def test_delete_symbol(input_string, symbol, expected_result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_string, symbol)
    assert res == expected_result



# Функция starts_with возвращает `True`, если строка начинается с заданного символа и `False` - если нет

@pytest.mark.parametrize("input_string, symbol, expected_result", [
    ("Moon", "m", False),
    ("Moon", "Mo", True),
    ("Круг", "э", False),
    ("5432.1", "5", True),
    (" %^#@!", " ", True),
    ("生,き,が,い", "生", True),
    ("     ", " ", True),
    ("", "", True)
    ])
def test_starts_with(input_string, symbol, expected_result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input_string, symbol)
    assert res == expected_result



# Функция ends_with возвращает `True`, если строка заканчивается заданным символом и `False` - если нет

@pytest.mark.parametrize("input_string, symbol, expected_result", [
    ("Moon", "N", False),
    ("Blue Moon", "Moon", True),
    ("Круг", "э", False),
    ("5432.1", ".1", True),
    ("%^#@! ", " ", True),
    ("生,き,が,い", "い", True),
    ("     ", "  ", True),
    ("", "", True)
    ])
def test_ends_with(input_string, symbol, expected_result):
    string_utils = StringUtils()
    res = string_utils.ends_with(input_string, symbol)
    assert res == expected_result



# Функция is_empty возвращает `True`, если строка пустая и `False` - если нет

@pytest.mark.parametrize("input_string, expected_result", [
    ("", True),
    ("     ", True),
    ("Moon", False),
    ("  стол", False),
    ("_____", False),
    ("-----", False),
    ])
def test_is_empty(input_string, expected_result):
    string_utils = StringUtils()
    res = string_utils.is_empty(input_string)
    assert res == expected_result



# Функция list_to_string преобразует список элементов в строку с указанным разделителем

@pytest.mark.parametrize("lst, joiner, expected_result", [
    (["а", "Б", "в", "Г"], None, "а, Б, в, Г"),
    (["Blue", "moon"], " ", "Blue moon"),
    (["1", "2", "3"], "!", "1!2!3"),
    (["1", "2", "3"], ":-)", "1:-)2:-)3"),
    (["1", "2", "3"], "a", "1a2a3"),
    (["aa", "bb", "cc"], None, "aa, bb, cc"),
    (["生", "き", "が", "い"], None, "生, き, が, い"),
    ([" ", " ", " "], None, " ,  ,  "),
    ([], None, ""),
    ])
def test_list_to_string(lst, joiner, expected_result):
    string_utils = StringUtils()
    if joiner is None:
        res = string_utils.list_to_string(lst)
    else:
        res = string_utils.list_to_string(lst, joiner)
    assert res == expected_result
