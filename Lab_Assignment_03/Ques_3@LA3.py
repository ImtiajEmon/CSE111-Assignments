class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True

#=====================================================================

president1 = Wadiya()
print("Part 1:")
print("Name of President:", president1.name)
print("Designation:", president1.designation)
print("Number of wife:", president1.num_of_wife)
print("Is he/she a dictator:", president1.dictator)

president1.name = 'Donald Trump'
president1.designation = 'President'
president1.num_of_wife = 1
president1.dictator = False

print("Part 2:")
print("Name of President:", president1.name)
print("Designation:", president1.designation)
print("Number of wife:", president1.num_of_wife)
print("Is he/she a dictator:", president1.dictator)
