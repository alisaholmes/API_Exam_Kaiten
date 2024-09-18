from pathlib import Path
import tests
import utils


def path(file_name):
    return str(Path(tests.__file__).parent.parent.joinpath(f'schemas/{file_name}'))


def path_from_project(relative_path: str):
    return (
        Path(utils.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
