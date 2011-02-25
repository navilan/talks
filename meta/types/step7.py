class Animal(object):
    pass


def Grrrr(self):
    return "Grrrr"

class TemplateAnimal(object):
    def roar(self):
        """
        Animals make this sound when
        they are disturbed or angry.
        """
        return "RRRRRRRRawr"


import functools
import types

def make_method(wrapped, template, cls=Animal, instance=None):

    @functools.wraps(template)
    def wrapper(self):
        return wrapped(self)

    return types.MethodType(wrapper, instance, cls)

Animal.roar = make_method(Grrrr, TemplateAnimal.roar)

import sys

mod = sys.modules[__name__]

def make_animal(name, sound):
    animal_name = name.capitalize()
    t = types.ClassType(animal_name, (Animal,), {})
    setattr(mod, animal_name, t)
    def shout(cls):
        return sound
    t.roar = make_method(shout, TemplateAnimal.roar)
    return t

animals = dict(dog="bark", owl="hoot")

for animal_name, sound in animals.iteritems():
    make_animal(animal_name, sound)

assert Dog
assert Owl

for animal in [Dog, Owl]:
    a = animal()
    print a.roar()
    print a.roar
    print a.roar.__doc__
    print "*" * 75

