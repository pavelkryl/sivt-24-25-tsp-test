from graph import Cesta
from europe import load_europe

evropa = load_europe()
print(evropa)

reseni: list[Cesta] = []

def solve_tsp(graph, dosud_projita_cesta):
    # pokazde kdyz najde platne reseni (ktere projde vsemi mesty prave jednou), prida ho do seznamu 'reseni'
    ...

cesta = Cesta(["Madrid"], 0)
solve_tsp(evropa, cesta)
print(f"hotovo, nasel jsem {len(reseni)} reseni")
