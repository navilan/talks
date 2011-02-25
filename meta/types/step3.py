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

class TemplateAnimal(object):
    def roar(self):
        """
        Animals make this sound when
        they are disturbed or angry.
        """
        return "RRRRRRRRawr"


import functools

def make_method(wrapped, template):

    @functools.wraps(template)
    def wrapper(self):
        return wrapped(self)

    return wrapper

Animal.roar = make_method(Grrrr, TemplateAnimal.roar)

print a.roar()
print a.roar
print a.roar.__doc__
