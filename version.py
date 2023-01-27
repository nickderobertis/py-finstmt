from pathlib import Path

pyproject_toml_path = Path(__file__).parent / "pyproject.toml"


def get_version() -> str:
    if not pyproject_toml_path.exists():
        return "0.0.1"
    with open(pyproject_toml_path) as f:
        for line in f:
            if line.startswith("version"):
                return line.split("=")[1].strip().replace('"', "")
    raise ValueError("could not find version in pyproject.toml")


if __name__ == "__main__":
    print(get_version())
