cuvinte = "Python este un limbaj de programare foarte popular. Python este folosit pentru dezvoltare web, analiză de date, inteligență artificială și automatizare. Mulți programatori aleg Python deoarece este ușor de învățat și are o comunitate mare."
elemente = []

for cuv in cuvinte.split(" "):
    elemente.append(cuv)

print(elemente)

d = {}

for cuv in elemente:
    d[cuv] = d.get(cuv, 0) + 1

print(d)