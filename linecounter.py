"""
 Copyright 2015 Muhammet Halit Karakis

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. 
"""

""" Basically counts lines in files. It is developed for developers,
    who want to count lines of their codes. It can be used for another
    purposes also.

    Author: m.halit karakis
    Created: 15-07-2015 """
import sys
from os import listdir
from os.path import isfile, isdir, join, splitext

def show_usage():
    """ Shows usage of line-counter."""
    print("")
    print("Usage:")
    print("  line-counter -fd [-r] path1 [path2 ...] [--filter ext1 [ext2 ...]] ")
    print("")
    print("options:")
    print("  %s\t\t%s" % ("-f", "Run line-counter with file paths"))
    print("  %s\t\t%s" % ("-d", "Run line-counter with directory paths"))
    print("  %s\t\t%s" % ("-r", "Search directories recursively, can be used if '-d' is set"))
    print("  %s\t%s" % ("--filter", "Count lines for files which extension is ext1,ext2\n"
                                    "\t\tcan be used if '-d' is set"))
    print("  %s\t%s" % ("--help", "Show this message"))


def line_count_file(file_path):
    """ Counts lines for given file in file_name """
    try:
        count = 0
        with open(file_path) as current_file:
            for line in current_file:
                count += 1

        return count
    except IOError:
        return -1

def line_count_files(file_name_list):
    """ Counts lines for given set of files """
    total = 0
    for file_name in file_name_list:
        current = line_count_file(file_name)
        if current >= 0:
            total += current
            print("%6d---in--->%s" % (current, file_name))
        else:
            print("error: file not found (" + file_name + ")")
    return total

def line_count_dir(dir_path, flags, filters):
    """ Counts lines for files which are in given directory path and matches
        filter requirements """
    total = 0
    file_list = [join(dir_path, file) for file in listdir(dir_path)
                 if isfile(join(dir_path, file)) and
                 splitext(join(dir_path, file))[1] in filters]

    total += line_count_files(file_list)

    if flags.count("-r") > 0:
        dir_list = [join(dir_path, directory) for directory in listdir(dir_path)
                    if isdir(join(dir_path, directory))]
        for directory in dir_list:
            total += line_count_dir(directory, flags, filters)

    return total


def main():
    """ Main flow of line-counter """
    if sys.argv[1] == "--help":
        show_usage()
        return -1

    output = ""
    total_line = 0

    if len(sys.argv) < 3:
        show_usage()
        return -1

    if sys.argv.count("-f") >= 1 and sys.argv.count("-d") >= 1:
        show_usage()
        return -1

    if sys.argv.count("-f") == 1 and sys.argv.index("-f") == 1:
        total_line = line_count_files(sys.argv[2:])
    elif sys.argv.count("-d") == 1 and sys.argv.index("-d") == 1:
        flags = []
        if sys.argv[2] == "-r":
            flags.append("-r")

        filters = []
        if sys.argv.count("--filter") > 0:
            filters = sys.argv[sys.argv.index("--filter")+1::]

        start_index = 2 + len(flags)
        end_index = len(sys.argv) - len(filters) - 1

        for directory in sys.argv[start_index:end_index]:
            total_line = line_count_dir(directory, flags, filters)

    output += "\ntotal lines: " + str(total_line)

    print(output)
    exit(total_line)

if __name__ == '__main__':
    main()
