from world import World
import time


world = World()

print("🌍 OpenSim")
print("A tiny civilization begins...\n")

while True:
    population = world.run_day()

    if population == 0:
        print("\n💀 Civilization has collapsed.")
        break

    if world.day >= 100:
        print("\n🏆 Civilization survived 100 days!")
        break

    time.sleep(0.5)
