from sys import argv
from bsc import Bsc
from cli import Cli

def main():
    bsc = Bsc()
    cli = Cli(bsc)

    if(len(argv))<2:
        cli.start()

    if(len(argv))>2:
        cli.err("Too many arguments")
        exit()
    
    else:
        try:
            f = open(argv[1], "r")
            content = f.read()
            f.close()
        except:
            cli.err(f"Can't open file: {argv[1]}")
            exit()

        out = bsc.run(content)
        if out == True:
            cli.err("Parser error")

if __name__ == "__main__":
    main()