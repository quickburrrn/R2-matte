from typing import Callable
from r2matte import mu

def finn_eksplisit(tallfølge : list[int]) -> Callable:
    """
    Finner eksplisit, gjør sitte beste å skille på linær, polynom og eksponensiel. Klarer ikke å finne sin, logistisk, tan osv

    Args:
        tallfølge (list[int]): Tallfølgen som du skal ha formelen til

    Returns:
        Callable: eksplisitt formel
    """

    # avragey
    # avragex
    
    # nedre = 0
    # for i in tallfølge:
    #     nedre += i-

    def eksplisitt_formel(n):
        return (tallfølge[1]-tallfølge[0])*n+tallfølge[0]-(tallfølge[1]-tallfølge[0])

    return eksplisitt_formel

def finn_rekursiv() -> str:
    return "not implemented"

if __name__ == "__main__":
    tallfølge = [10, 8, 6, 4]