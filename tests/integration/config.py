import os
from pathlib import Path

EXPECT_DATA_PATH = Path(__file__).parent / "expectdata"
EXPECT_CONFIG_PATH = EXPECT_DATA_PATH / "config"
EXPECT_STATEMENTS_PATH = EXPECT_DATA_PATH / "statements"
GENERATE_TEST_DATA: bool = os.getenv("FINSTMT_GENERATE_TEST_DATA", False)
