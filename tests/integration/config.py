from pathlib import Path

EXPECT_DATA_PATH = Path(__file__).parent / "expectdata"
EXPECT_CONFIG_PATH = EXPECT_DATA_PATH / "config"
EXPECT_STATEMENTS_PATH = EXPECT_DATA_PATH / "statements"
DEVELOPMENT_MODE: bool = False
