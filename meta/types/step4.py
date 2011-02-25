class Animal(object):
    pass


def Grrrr(self):
    return "Grrrr"


a = Animal()

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

cat = Animal()

print cat.roar()
print cat.roar

print "=" * 75


def Purrr(self):
    return "Purrrr"


cat.roar = make_method(Purrr, TemplateAnimal.roar)

print cat.roar()
print cat.roar
print cat.roar.__doc__