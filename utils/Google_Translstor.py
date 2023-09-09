from deep_translator import GoogleTranslator


def translater(word: str, first_l: str, second_l: str):
    txt = GoogleTranslator(source=first_l, target=second_l).translate(word)
    return txt
