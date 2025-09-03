# definerer t(n)
t = lambda n: 1/2 * n * (n+1)

# altid et heltall
def T(n) -> int:
    s = []
    for i in range(n+1):
        s.append(t(i))
    return sum(s)

# printer summen fra 1 til 10
for n in range(1, 11):
    print(f"T({n}) : {T(n)}")