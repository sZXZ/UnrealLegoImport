import argparse
from pathlib import Path


def get_context():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-u', '--unreal')
    return parser.parse_args()


def main(context):
    venv_path = Path(__file__).parent.joinpath('venv')
    ue_path = Path(context.unreal)
    # C:\Program Files\Epic Games\UE_5.1\Engine\Plugins\Experimental\PythonScriptPlugin\Content\Python\remote_execution.py
    with open(venv_path.joinpath('Lib', 'site-packages', 'unreal_remote_execution.pth'), 'w') as f:
        f.write(str(ue_path.joinpath('Engine', 'Plugins', 'Experimental',
                'PythonScriptPlugin', 'Content', 'Python').resolve()))
    # adds root folder
    with open(venv_path.joinpath('Lib', 'site-packages', 'root.pth'), 'w') as f:
        f.write(str(venv_path.parent.resolve()))
    # <ProjectPath>\Intermediate\PythonStub\
    with open(venv_path.joinpath('Lib', 'site-packages', 'unreal_stab.pth'), 'w') as f:
        f.write(str(Path(__file__).parent.parent.parent.joinpath(
            'Intermediate', 'PythonStub').resolve()))


if __name__ == "__main__":
    main(get_context())
