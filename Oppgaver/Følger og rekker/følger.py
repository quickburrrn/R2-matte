from typing import Callable

class SequenceFinder():
    def __init__(self):
        pass

    def finn_eksplisit(tallfølge : list[int]) -> Callable:
        def eksplisitt_formel(n):
            return 2*n+2

        return eksplisitt_formel

    def finn_rekursiv() -> str:
        return "not implemented"

if __name__ == "__main__":
    finder = SequenceFinder

    tallfølge = [10, 8, 6, 4]

    formel : Callable = finder.finn_eksplisit(tallfølge)

    for n in range(1, 5):
        print(formel(n))
