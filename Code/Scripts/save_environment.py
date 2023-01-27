import os.path
import subprocess

# Own packages
from src.utils import get_root_of_project

def print_messages(message_to_show):
    print(message_to_show)


def save_conda_environment(root_of_project):
    print_messages("Started saving the environment to a YAML file...")
    location_of_file = os.path.join(root_of_project, "environment_file\\env.yaml")
    print(location_of_file)
    subprocess.run(f'conda activate postgrad && conda env export -f { location_of_file } && conda deactivate', shell=False)
    print_messages(f"Environment file saved to location { location_of_file }")


def main():
    save_conda_environment(get_root_of_project())

if __name__ == "__main__":
    main()
    exit(0)