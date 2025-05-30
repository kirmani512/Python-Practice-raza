class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print("sound of animal")

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name, species="dog")
        self.breed=breed

    def make_sound(self):
        print("bark")

d=dog("dog","gemran")
d.make_sound()


c=animal('tommy','german')
c.make_sound()

#implement a cat class by using the animal class. Add some methods specific to that
