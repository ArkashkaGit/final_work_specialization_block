from registry_animal.view.menu import Menu
from registry_animal.model.animal import Animal
from registry_animal.model.registry_animals import Registry_animal
from registry_animal.controller.function_registry_animal import Function_registry_animal


registry_animals = Registry_animal()

dog = Animal("Dog")
dog.add_animal_skill("Bring the ball")
cat = Animal("CAT")
cat.add_animal_skill("Jamp")
cat.add_animal_skill("Murr")

horse = Animal("Horse")
horse.add_animal_skill("To_carry")
horse.add_animal_skill ("Run fast")

registry_animals.add_domestic_animal(cat)
registry_animals.add_domestic_animal(dog)
registry_animals.add_pack_animal(horse)

func_reg_animal = Function_registry_animal(registry_animals)

menu = Menu(func_reg_animal).menu()

