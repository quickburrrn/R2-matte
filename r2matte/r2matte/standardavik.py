from typing import Callable

def mu(tall_liste : list[float]) -> float:
    return sum(tall_liste)/len(tall_liste)

def standardavik(tall_liste: list[float]) -> float:
    my = mu(tall_liste)
    
    sum_med_mu = 0
    for i in tall_liste:
        sum_med_mu += (i-my)**2
    
    return (sum_med_mu/len(tall_liste))**0.5
    

if __name__ == "__main__":
    tallfølge : list[float] = [50, 100, 150]

    print(mu(tallfølge))

    print(standardavik(tallfølge))