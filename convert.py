import json

data = json.loads(open("./diamond_hoe.json", "r").read())

write_file = open("./diamond_hoe.txt", "w")

for override in data["overrides"]:
    try:
        damage = override["predicate"]["damage"]
    except KeyError:
        damage = 0
    damage *= 1562
    damage = round(damage)
    model = override["model"]
    x = model.replace("custom/vehicles/", "")
    xs = x.replace("_", " ")
    write_file.write(f"Damage: {damage}, Naam: {xs}\n")

write_file.close()