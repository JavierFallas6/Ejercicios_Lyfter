class Father:
    def __init__(self, cromosome):
        self.cromosome_father = cromosome

class Mother:
    def __init__(self, cromosome):
        self.cromosome_mother = cromosome

class Kid(Father,Mother):
    def __init__(self,cromosome_father, cromosome_mother):
        Father.__init__(self, cromosome_father)
        Mother.__init__(self, cromosome_mother)

    def gender(self):
        if self.cromosome_father == "X" and self.cromosome_mother == "X":
            print("It is a Girl")
        else:
            print("It is a Boy")

cromosome_from_Mother = "X" ##Mom always provide only a X cromosome
cormosome_from_Father = input("Cromosome from Father X o Y select one: ")
new_born = Kid(cormosome_from_Father, cromosome_from_Mother)
new_born.gender()    