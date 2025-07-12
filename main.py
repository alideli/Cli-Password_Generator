from cli import get_arguments
from func import pass_generator

def main():
    args = get_arguments()
    pass_generator(args)

if(__name__ == "__main__"):
    main()