# Created by halit karakis on 15/07/2015

import sys

# shows usage of line counter program
def show_usage():
    print("line counter v.0.0.1")

# counts line for given file
def line_count_file(file_name):
    count = 0
    with open(file_name) as code_file:
        for line in code_file:
            count += 1

    return count

# main flow of program
def main():
    output = ""
    total_line = 0

    if len(sys.argv) < 3:
        show_usage()
        exit(-1)

    if sys.argv.count("-f") >= 1 and sys.argv.count("-d") >= 1:
        show_usage()
        exit(-1)

    if sys.argv.count("-f") == 1 and sys.argv.index("-f") == 1:
        total_line = 0
        for i in range(2, len(sys.argv)):
            current_line = line_count_file(sys.argv[i])

            if current_line >= 0:
                output += str(current_line) + "\t in \t" + sys.argv[i] +"\n"
                total_line += current_line
            else:
                output += "err: file not found (" + sys.argv[i] + ")\n"
    elif sys.argv.count("-d") == 1 and sys.argv.index("-d") == 1:
        total_line = 2;

    output += "\ntotal lines: " + str(total_line)

    print(output)
    exit(total_line)
    
if __name__ == '__main__':
    main()
