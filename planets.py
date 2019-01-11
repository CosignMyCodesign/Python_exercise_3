planet_list = ["Mercury", "Mars"]

# 1. Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)
# 2. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Uranus", "Neptune"])
print(planet_list)
# 3. Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
print("ordered planets", planet_list)
# 4. Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print("with pluto added:", planet_list)
# 5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets = planet_list[0:4]
print(rocky_planets)
# 6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]
print("with Pluto removed:", planet_list)

# CHALLENGE: Iterating over planets
# 1. Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
just_visiting = [("Voyager", "Mars"), ("Endurance", "Mercury"), ("Extendo", "Neptune")]
# 2. Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
for planet in planet_list:
  for satellite in just_visiting:
    if planet == satellite[1]:
      print(f"{planet} was visited by {satellite[0]}")
