from typing import Callable

def finn_eksplisit(tallfølge : list[int]) -> Callable:
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
