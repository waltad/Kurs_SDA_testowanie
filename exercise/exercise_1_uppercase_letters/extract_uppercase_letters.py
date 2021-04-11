"""
EXTRACT UPPERCASE LETTERS

Twoim zadaniem jest stworzenie funkcji zwracającej string zawierający wszystkie duże litery z podanego stringa.
String przyjmowany jest jako parametr 'sentence'. W pliku test_extract_uppercase_letters.py napisz testy tej funkcji.

Wskazówki:
*   Zalecam użycie pętli 'for' aby sprawdzić każdy ze znaków.
*   Do sprawdzenia czy dana litera jest wielką można użyć metody 'isupper()', która zwaraca True gdy litera jest wielka
    oraz False w przeciwnym wypadku. Np. <literka>.isupper().

"""


def extract_uppercase_letters(sentence):
    uppercase_letters = ""

    for letter in sentence:
        if letter.isupper():
            uppercase_letters += letter

    return uppercase_letters

if __name__ == '__main__':
    sentence = "TgAfdgDgh EvxUdzSZ"
    b = extract_uppercase_letters(sentence)
    print(b)
