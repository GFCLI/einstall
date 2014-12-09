from py_compile import compile
import os

def main(args):
    pkname = args
    if raw_input("You are about to install " + pkname + " which originates from an unverified repository.  Are you sure you want to continue? (yN)"):
        os.system("git clone https://github.com/" + pkname + ".git")
        os.system("copy " + pkname + "/" + pkname + ".py " + pkname + ".py")
        compile(pkname + ".py")
        os.system("DEL " + pkname + ".py;rd /s /q " + pkname)
