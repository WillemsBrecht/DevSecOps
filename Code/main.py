# Own Packages
from src.utils import get_root_of_project
from Code.Helper import checker
from Code.Scripts import save_environment
from Code.Scripts import show_environment_file


def give_options():
    print("Please select an option....")
    print("1. Save environment to YAML-file.")
    print("2. Show existing YAML-file content.")
    print("3. Close application.")
    user_option = input("> ")
    return int(user_option)


def process_user_option():
    user_option = give_options()
    while not checker.check_if_valid(user_option):
        user_option = give_options()

    if user_option == 1:
        save_environment.main()
    elif user_option == 2:
        show_environment_file.main()
    else:
        print("Closing application...")
        exit(0)


def main():
    process_user_option()


if __name__ == "__main__":
    main()
    exit(0)