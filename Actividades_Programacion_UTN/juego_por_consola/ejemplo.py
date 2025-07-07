def pu(txt:str, booleano:bool)->str:
    if txt == "aja":
        booleano = False
        txt = "quseyyop"
    return txt

dic = {"nolose":True}

hola = pu("aja",dic["nolose"])

print(hola, dic["nolose"])