import os
from tests.fixtures import *

DEVELOPMENT_MODE: bool = False

GENERATED_PATH = os.path.sep.join(['tests', 'generated'])

if not os.path.exists(GENERATED_PATH):
    os.makedirs(GENERATED_PATH)