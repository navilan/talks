class Animal(object):
    pass

def Grrrr(self):
    return "Grrrr"


a = Animal()

Animal.roar = Grrrr
print a.roar() # Grrrrr
print a.roar
# <bound method Animal.Grrrr of <__main__.Animal object at 0x100460690>>

print "=" * 75

def make_method(method, name, cls):
    def method_(self):
        return method(self)
    method_.__name__ = name
    return method_

Animal.roar = make_method(Grrrr, "roar", Animal)

print a.roar()
print a.roar
