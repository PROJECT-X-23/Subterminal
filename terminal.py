import os
import random
import sys
import cmd


############################
# Terminal creation
############################
class Terminal(cmd.Cmd):
        intro = "Welcome to the terminal. Type help or ? to list commands.\n"
        prompt = "(terminal) "
        file = None
        def default(self, line):
              print("Invalid command. Type help or ? to list commands.")
              return True
        def do_echo(self, arg):
              'Echo the input argument'
              print(arg)
              return True
        def do_exit(dself, arg):
              'exit terminal'
              return True
        def do_clear(self, arg):
              "clearing ..."
              return True
        def do_cd(self, arg):
              # do cd please
            if arg == "..":
                    os.chdir("..")
                    print(os.getcwd())
            elif arg == "/":
                    os.chdir("/")
                    print(os.getcwd())
            elif arg == "2317":
                  print("modalità sviluppatore attivata")
            else:
                  print("uknow unexpected action")
                  return True
        
        


def create_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;32;40m" + "Terminal" + "\033[]")
    print("\033[1;32;40m" + "------------------------" + "\033")
    print("terminale attivo scrivere righe di codice")
if __name__ == '__main__':
      create_terminal().cmdloop()