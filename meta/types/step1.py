class Animal(object):
    pass

def Grrrr(self):
    return "Grrrrr"


a = Animal()

assert not hasattr(a, "Grrrr")
assert not hasattr(a, "roar")

#setattr(Animal, "roar", Grrrr)
Animal.roar = Grrrr

assert not hasattr(a, "Grrrr")
assert hasattr(a, "roar")

print a.roar() # Grrrrr

print "=" * 75

cat = Animal()
print cat.roar() # Grrrrr