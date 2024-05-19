#!/usr/bin/python3

import cmd


class CommandShell(cmd.Cmd):
    """Command line interpreter for managing Airbnb objects"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of File command to exit program"""
        return True and '\n'

    def do_quit(self, line):
        """Quit command to exit program"""
        return True and '\n'


if __name__ == '__main__':
    CommandShell().cmdloop()
