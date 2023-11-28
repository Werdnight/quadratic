from treatment_input import *
from pytest import *
import time
import random
import tqdm


def main(str_input: str):
    d = Input(str_input)
    return d.pattern_interpret()
