from typing import Callable
from r2matte.følger import finn_eksplisit

def finn_neste_tall(endring: Callable):
    liste = []
    for n in range(1, 21):
        liste.append(endring(n))
    print(liste)
    print()

def a():
    print("oppgave a \nplusser med 4 for hver gang")
    
    def endring(n):
        return (4*n+1)
    
    finn_neste_tall(endring)

def b():
    print("oppgave b \nsubtraherer med 2 for hver gang")

    def endring(n):
        return (-2*n+12)
    
    finn_neste_tall(endring)

def c():
    print("oppgave c")

def d():
    print("oppgave d")

def e():
    print("oppgave e")

def f():
    print("oppgave f")

a()
b()
c()
d()
e()
f()


