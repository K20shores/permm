__all__ = ['Mechanism', 'Species', 'Reaction', 'atoms', 'mechanism_dict']

from .core.Species import Species
from .core.Reaction import Reaction
from .core.Mechanism import Mechanism
from .mechanisms import mechanism_dict, atoms
from . import mechanisms
from . import getmech
# The interactive shell and GUI depend on optional toolkits (readline, tkinter,
# wxPython) that need not be present for headless/analysis use, so import them
# lazily and don't let a missing toolkit break ``import permm``.
try:
    from . import Shell
except Exception:  # pragma: no cover - optional dependency
    Shell = None
try:
    from . import GUI
except Exception:  # pragma: no cover - optional dependency
    GUI = None
from .getmech import get_pure_mech, get_prepared_mech
get_mech = get_pure_mech

if __name__ == '__main__':
    from permm.main import parse_and_run
    parse_and_run()