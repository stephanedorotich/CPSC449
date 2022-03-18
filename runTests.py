import os
import sys

num_test_cases = 55;
ass = "";

def main():
    # Command line argument validation

    # Check for at least 2 args (program name + assignment code)
    if len(sys.argv) < 2:
        print("Please provide the assignment name (A1, A2, or A3)")
        exit()

    # Validate assignment code
    if sys.argv[1] not in ["A1","A2","A3"]:
        print("Please provide the assignment name (A1, A2, or A3)")
        exit()

    # Ensure output folder exists
    if not (os.path.isdir("./A1/src/outputs")):
        os.mkdir("./A1/src/outputs")

    # Assignment test case number if applicable
    if len(sys.argv) == 3:
        n = int(sys.argv[2])
    else: n = 0

    # Run tests
    if sys.argv[1] == "A1":
        run_A1(n)
    elif sys.argv[1] == "A2":
        run_A2(n)
    elif sys.argv[1] == "A3":
        run_A3(n)


def run_A1(n):
    # Compile
    os.system("javac -d ./ A1/src/Main.java")
    print("Program compiled!")

    if not n == 0:
        os.system(f"java Main tests/test{n}.txt A1/src/outputs/output{n}.txt")
    else:
        for i in range(1, num_test_cases+1):
            os.system(f"java Main tests/test{i}.txt A1/src/outputs/output{i}.txt")

    # Clean
    os.system("rm Main.class | rm InputNode.class")


def run_A2(n):
    # Compile
    os.system("ghc -o main A2/a2.hs")
    print("Program compiled!")

    if not n == 0:
        os.system(f"./main tests/test{n}.txt A1/src/outputs/output{n}.txt")
    else:
        for i in range(1, num_test_cases+1):
            os.system(f"./main tests/test{i}.txt A1/src/outputs/output{i}.txt")

    # Clean
    os.system("rm main A2/a2.hi A2/a2.o")


def run_A3(n):
    if not n == 0:
        os.system(f"swipl A3/a3.pl tests/test{n}.txt A1/src/outputs/output{n}.txt")
    else:
        for i in range(1, num_test_cases+1):
            os.system(f"swipl A3/a3.pl tests/test{i}.txt A1/src/outputs/output{i}.txt")

if __name__=="__main__":
    main()
