import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description = "Generate strong and random passwords.",
                                    epilog = "I hope you enjoy using my password manager <3")

    parser.add_argument("--generate", "-cr", help = "this command is to create a random password", action = "store_true")
    parser.add_argument("--length", "-len", help = "enter length of password. default is 10", default = 10)
    parser.add_argument("--special_chr", "-sch", help = "choose characters you want use in password. choices are: @,#,$,%,!,&,+",
                        choices = ["@","#","$","%","!","&","+"], nargs='+', default = None)
    parser.add_argument("--strength", "-strn", help = "see your password\'s strength", action = "store_true")
    parser.add_argument("--password", "-pass", help = "enter a password to check it\'s strength")
    parser.add_argument("--describe", "-db", help = "enter description for your password")
    parser.add_argument("--view", "-v", help = "you can see your passwords and descriptions", action = "store_true")
    parser.add_argument("--remove", "-rm", help = "you can remove a password you saved before.(enter number)", type = str)

    return parser.parse_args()