import os
import sys

num_test_cases = 30;
ass = "";

def main():
    # Command line argument validation
    if len(sys.argv) != 2:
        print("Please provide the assignment name (A1, A2, or A3)")
        exit()
    if sys.argv[1] not in ["A1","A2","A3"]:
        print("Please provide the assignment name (A1, A2, or A3)")
        exit()

    # Run tests
    if sys.argv[1] == "A1":
        run_A1()
    elif sys.argv[1] == "A2":
        run_A2()
    elif sys.argv[1] == "A3":
        run_A3()


def run_A1():
    # Compile
    os.system("javac -d ./ A1/src/Main.java")
    print("Program compiled!")

    for i in range(1, num_test_cases+1):
        os.system(f"java Main A1/src/tests/test{i}.txt A1/src/outputs/output{i}.txt")

    # Clean
    os.system("rm Main.class | rm InputNode.class")


def run_A2():
    print("hello")


def run_A3():
    print("hello")


if __name__=="__main__":
    main()