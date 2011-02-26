import functools
import types
import sys

module = sys.modules[__name__]

def make_method(wrapped, template, cls=object, instance=None):

    @functools.wraps(template)
    def wrapper(self):
        return wrapped(self)

    return types.MethodType(wrapper, instance, cls)

class AnimalType(type):
    """
    The Animal type.
    """

    def roar(self):
        """
        Animals make this sound when
        they are disturbed or angry.
        """
        return "RRRRRRRRawr"

    def __call__(mcs, *args, **kwargs):
        factory_params = [kwargs[a] for a in ['name', 'sound'] if a in kwargs]
        if factory_params:
            cls = getattr(module, 'Animal')
            (name, sound) = tuple(factory_params)
            animal_name = name.capitalize()
            if not hasattr(module, animal_name):
                def shout(self):
                    return sound
                attrs = {}
                attrs['roar'] = make_method(shout, AnimalType.roar)
                t = types.ClassType(animal_name, (cls,), attrs)
                setattr(module, animal_name, t)
            return getattr(module, animal_name)()
        return super(AnimalType, mcs).__call__(*args, **kwargs)


class Animal(object):

    __metaclass__ = AnimalType

animal_data = dict(dog="bark", owl="hoot")

animals = [Animal(name=name, sound=sound) for name, sound in animal_data.iteritems()]

assert Dog
assert Owl

for animal in animals:
    print animal.roar()
    print animal.roar
    print animal.roar.__doc__
    print "*" * 75

