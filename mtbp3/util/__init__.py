from .lsr import *
from .cdt import *
from .cdtg import *

import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data(path):
    return os.path.join(_ROOT, '../data', path)
