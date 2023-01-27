import yaml
import pprint
import os.path

# Own packages
from src.utils import get_root_of_project


def load_and_show_yaml_file(root_of_project):
    # Generates Error
    content = yaml.load(open(os.path.join(root_of_project, "environment_file\env.yaml")))
    # Is safe to use
    #content = yaml.safe_load(open(os.path.join(root_of_project, "environment_file\env.yaml")))
    pprint.pprint(content)


def main():
    load_and_show_yaml_file(get_root_of_project())


if __name__ == "__main__":
    main()
    exit(0)