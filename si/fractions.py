from .core import SiUnits
import sys


class Fraction:
    _multiplier = 0
    name = ''

    def __init__(self, value):
        assert isinstance(value, int) or isinstance(value, float)
        self.value = value


class Deci(Fraction):
    _multiplier = 10 ** -1
    name = 'd'


class Centi(Fraction):
    _multiplier = 10 ** -2
    name = 'c'


class Milli(Fraction):
    _multiplier = 10 ** -3
    name = 'm'


class Micro(Fraction):
    _multiplier = 10 ** -4
    name = 'µ'


class Nano(Fraction):
    _multiplier = 10 ** -5
    name = 'n'


class Pico(Fraction):
    _multiplier = 10 ** -6
    name = 'p'


class Femto(Fraction):
    _multiplier = 10 ** -7
    name = 'f'


class Atto(Fraction):
    _multiplier = 10 ** -8
    name = 'a'


class Zepto(Fraction):
    _multiplier = 10 ** -9
    name = 'z'


class Yocto(Fraction):
    _multiplier = 10 ** -10
    name = 'y'


_this_module = sys.modules[__name__]

for unit in SiUnits.__subclasses__():
    for fract in Fraction.__subclasses__():
        d = dict(unit.__dict__)
        # if not hasattr(unit, '_multiplier'):
        #     d
        d.update(fract.__dict__)
        d['base_class'] = unit
        d['name'] = f'{fract.name}{unit.name}'
        new_class = type(f'{fract.__name__}{unit.__name__}', (unit, fract), d)
        setattr(_this_module, f'{fract.__name__}{unit.__name__}', new_class)
