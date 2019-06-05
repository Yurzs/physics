import inspect


class Converter:
    def __init__(self, unit):
        self._unit = unit

    def to(self, base):
        assert inspect.isclass(base), f'{base} is not a class'

        def error_text_fn(x, y):
            return f'Cannot convert {x.__class__.__name__} to {y.__name__ if inspect.isclass(y) else y.__class__.__name__}'

        if hasattr(base, 'base_class') and hasattr(self._unit, 'base_class'):
            assert base.base_class == self._unit.base_class, error_text_fn(self._unit, base)
            return base(self._unit._multiplier / base._multiplier * self._unit.value)
        assert issubclass(self._unit.__class__, base) and issubclass(base, self._unit.__class__), error_text_fn(
            self._unit, base)
        return base(self._unit._multiplier / base._multiplier * self._unit.value)
