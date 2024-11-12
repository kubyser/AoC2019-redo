PART2 = True
modules = []
f = open("resources/day1_input.txt", "r")
lines = f.read().splitlines()
f.close()
for l in lines:
    modules.append(int(l))
sumFuel = 0
while len(modules) > 0:
    mass = modules.pop()
    fuelMass = int(mass/3) - 2
    if fuelMass > 0:
        sumFuel += fuelMass
        if PART2:
            modules.append(fuelMass)

print("Sum of fuel needed: ", sumFuel)
