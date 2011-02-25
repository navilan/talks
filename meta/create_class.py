class Animal(object):

    def shout(self):
        print "Grrrrrrrr"

a = Animal()
a.shout()

class Cat(Animal):

    def shout(self):
        print "Meow"


c = Cat()
c.shout()


others = dict(dog="bark", owl="hoot")

import sys
import types

mod = sys.modules[__name__]

for animal, sound in others.iteritems():
    def make_class(sound):
        def shout(cls):
            print sound
        capanimal = animal.capitalize()
        t = types.ClassType(capanimal, (Animal,), {})
        setattr(mod, capanimal, t)
        t.shout = types.MethodType(shout, None, t)
    make_class(sound)


for animal in [Animal, Cat, Dog, Owl]:
    a = animal()
    a.shout()
