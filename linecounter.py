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
import sys
from os import listdir
from os.path import isfile, isdir, join, splitext

VERSION = "1.3.0"
ALL_ARGS = {"linecounter", "linecounter.py", "-f", "-d", "-r", "-v", "-h", "--version", \
        "--help", "--filter", "--noempty"}

def show_usage():
    """ Shows usage of line-counter."""
    print("")
    print("Usage:")
    print("  linecounter -fd [options] path1 [path2 ...] [--filter ext1 [ext2 ...]] ")
    print("")
    print("options:")
    print("  %s\t\t%s" % ("-f", "Run linecounter with file paths"))
    print("  %s\t\t%s" % ("-d", "Run linecounter with directory paths"))
    print("  %s\t\t%s" % ("-r", "Search directories recursively, can be used if '-d' is set"))
    print("  %s\t%s" % ("--filter", "Count lines for files which extension is ext1,ext2\n"
                                    "\t\tcan be used if '-d' is set"))
    print("  %s\t%s" % ("--help", "Show this message"))
    print("  %s\t%s" % ("--version", "Show version info"))
    print("  %s\t%s" % ("--noempty", "Count lines without empty lines"))

def show_usage_error():
    """ Shows short usage error for wrong usages. """
    print("usage: linecounter -fd [-r] path1 [path2 ...] [--filter ext1 [ext2 ...]]")
    print("Try 'linecounter --help' for more information.")
    print("")


def line_count_file(file_path, flags=None):
    """ Counts lines for given file in file_name """
    try:
        count = 0
        with open(file_path) as current_file:
            for line in current_file:
                if line.strip() == "" and flags != None and \
                   "--noempty" in flags:
                    continue
                count += 1

        return count
    except IOError:
        return -1

def line_count_files(file_name_list, flags=None):
    """ Counts lines for given set of files """
    total = 0
    for file_name in file_name_list:
        current = line_count_file(file_name, flags)
        if current >= 0:
            total += current
            print("%6d lines in %s" % (current, file_name))
        else:
            print("error: file not found (" + file_name + ")")
    return total

def line_count_dir(dir_path, flags, filters):
    """ Counts lines for files which are in given directory path and matches
        filter requirements """
    total = 0

    if "--filter" in flags:
        file_list = [join(dir_path, file_p) for file_p in listdir(dir_path)
                     if isfile(join(dir_path, file_p)) and
                     splitext(join(dir_path, file_p))[1] in filters]
    else:
        file_list = [join(dir_path, file_p) for file_p in listdir(dir_path)
                     if isfile(join(dir_path, file_p))] 
                 
    total += line_count_files(file_list, flags)

    if "-r" in flags:
        dir_list = [join(dir_path, directory) for directory in listdir(dir_path)
                    if isdir(join(dir_path, directory))]
        for directory in dir_list:
            total += line_count_dir(directory, flags, filters)

    return total


def main():
    """ Main flow of line-counter """
    if len(sys.argv) == 1:
        show_usage_error()
        return -1

    # Usage check
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        show_usage()
        return 0
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print("linecounter version: " + VERSION)
        return 0

    if len(sys.argv) < 3:
        show_usage_error()
        return -1

    if "-f" in sys.argv and "-d" in sys.argv:
        show_usage_error()
        return -1

    # If everything is ok start counting lines
    output = ""
    total_line = 0

    extensions = []
    if "--filter" in sys.argv:
        extensions = [extension for extension in sys.argv[sys.argv.index("--filter"):]
                      if extension not in ALL_ARGS]

    flags = []
    flags = [flag for flag in sys.argv if flag in ALL_ARGS and
             flag not in flags]

    paths = [path for path in sys.argv if path not in ALL_ARGS and
             path not in extensions]

    if "-f" in flags:
        total_line = line_count_files(paths, flags)
    elif "-d" in flags:
        for directory in paths:
            total_line += line_count_dir(directory, flags, extensions)

    output += "\ntotal lines: " + str(total_line)

    print(output)
    return 0

if __name__ == '__main__':
    main()
