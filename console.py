#!/usr/bin/python3

"""
Program to for the console
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
        Main command
    """
    prompt = "(hbnb) "


    def do_nothing(self, arg):
        """ Empty work """
        pass 

    def emptyline(self):
        """ Emplty line """
        pass 

    def do_quit(self, arg):
        """ Quit the program """
        return True


    def do_EOF(self, arg):
        """ End of File """
        print("")
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
