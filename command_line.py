# A command line utility in python is usually a programm designd to be executed directly 
# through command line.


import argparse

def main():
    parser=argparse.ArgumentParser(description="calculator")  #argparse.ArgumentParser this is the class inside argparse module

    parser.add_argument("x", type=float, help="first number")
    parser.add_argument("y",type=float,help="second number")
    parser.add_argument("--add",action="store_true",help="add numbers")

    args=parser.parse_args() #here parser is the command line parser --------------- .parse_args() reaads what the user typed in the terminal

    if args.add:
        result=args.x+args.y
        print(f"result is {result}")

if __name__ == "__main__":
    main()