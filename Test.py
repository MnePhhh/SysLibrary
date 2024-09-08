import sys

def command_output(index, result):
    f = open(sys.argv[index], 'w')
    f.write(result)

def main():

    try:
        if str.isdigit(sys.argv[1]) and str.isdigit(sys.argv[2]):
            result_sum = int(sys.argv[2]) + int(sys.argv[1])
        else:
            sys.stderr.write("Error: passed arguments must be numbers!")
            sys.exit(1)
            
    except IndexError:
        sys.stderr.write("Error: Two numbers must be passed!")
        sys.exit(1)
    
    if "--output" in sys.argv:
        index_output = sys.argv.index("--output") + 1

        try:
            if sys.argv[index_output] and ".txt" in sys.argv[index_output]:
                command_output(index_output, str(result_sum))
                sys.exit(0)
            
            sys.stderr.write("Error: file name must end with '.txt'")
            sys.exit(1)

        except IndexError:
             sys.stderr.write("Error: You must specify a file for output.")
             sys.exit(1)

    sys.stderr.write(str(result_sum))

if __name__ == "__main__":
    main()