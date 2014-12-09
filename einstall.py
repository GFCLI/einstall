from py_compile import compile
import os

def main(args):
    args = args.split("#/")
    pkname = args[0]
    os.system("git clone https://github.com/" + pkname + ".git")
    os.system("copy " + pkname + "/" + pkname + ".py " + pkname + ".py")
    compile(pkname + ".py")
    os.system("DEL " + pkname + ".py;DEL " + pkname)
