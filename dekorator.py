#Ez a program bekér két számot. Meghív egy dekorátor függvényt, amely megnézi a két számot

def divide_dec(func):
    def ellenoriz(value1,value2):
        if value2 ==0:
            return "Nullaval nem lehet osztani"
        else:
            return func(value1,value2)
    return ellenoriz



@divide_dec
def divide(value1,value2):
    return value1/value2


value1 = int(input("Ird be az elso szamot: "))
value2 = int(input("Ird be a masodik szamot: "))
print(divide(value1,value2))
