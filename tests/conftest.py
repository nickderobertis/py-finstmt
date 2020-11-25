import os
from pathlib import Path

from tests.fixtures import *

DEVELOPMENT_MODE: bool = False

GENERATED_PATH = os.path.sep.join(['tests', 'generated'])
EXPECT_DATA_PATH = Path(__file__).parent / 'expectdata'
EXPECT_CONFIG_PATH = EXPECT_DATA_PATH / 'config'
EXPECT_STATEMENTS_PATH = EXPECT_DATA_PATH / 'statements'

if not os.path.exists(GENERATED_PATH):
    os.makedirs(GENERATED_PATH)