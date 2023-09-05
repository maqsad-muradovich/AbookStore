from deep_translator import GoogleTranslator



def translater(word,first_l,secnd_l):
    txt = GoogleTranslator(source=first_l, target=secnd_l).translate(word)
    return txt