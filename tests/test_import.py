from types import ModuleType

import cloudcoil.models.fluxcd as fluxcd


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), fluxcd.__dict__.values()))
    assert modules, "No modules found in fluxcd"
