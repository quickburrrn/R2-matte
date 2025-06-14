from typing import Callable

def finn_eksplisit(tallfølge : list[int]) -> Callable:
    # Kanskje 
    # | n_1=a*1+b
    # || n_2=a*2+b
    # løser det
    
    n_1 = tallfølge[0]
    n_2 = tallfølge[1]

    def eksplisitt_formel(n):
        return 2*n+2

    return eksplisitt_formel

def finn_rekursiv() -> str:
    return "not implemented"

if __name__ == "__main__":
    tallfølge = [10, 8, 6, 4]

    formel : Callable = finn_eksplisit(tallfølge)

    for n in range(1, 5):
        print(formel(n))
