populations = [30.55, 2.77, 39.21]

countries = ["afghanistan", "albania", "algeria"]

alb_idx = countries.index("albania")

alb_pop = populations[alb_idx]

population_chart = {
    "afghanistan": 30.55,
    "albania": 2.77,
    "algeria": 39.21
}

population_chart['bosnia'] = 3.28

print(population_chart)

del(population_chart['bosnia'])

print(population_chart)