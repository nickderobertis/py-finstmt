from tests.fixtures import *  # noqa: F401, F403

DEVELOPMENT_MODE: bool = False

GENERATED_PATH = os.path.sep.join(["tests", "generated"])

if not os.path.exists(GENERATED_PATH):
    os.makedirs(GENERATED_PATH)
