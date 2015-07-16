# linecounter

linecounter is a tool written in python, you can count how many lines you have in your files. This tool may be useful for developers who want to count how many lines of code they have in their projects. Because of linecounter isn't restricted for just code files it can be used in many areas which needs line counting. 

## Features
- Line counting for given file/files
- Line counting for list of files in given directory
- Line counting for list of files in given directory recursively
- Line counting for list of files in given directory with filtering file extensions

## Installation
You can install from pip by running

```
$ pip install linecounter
```

or you can download from github and run

```
$ python setup.py install
```
## Usage
```
Usage: linecounter -fd [-r] path1 [path2 ...] [--filter ext1 [ext2 ...]]

options:
    -f         Run line-counter with file paths
    -d         Run line-counter with directory paths
    -r         Search directories recursively, can be used if '-d' is set
    --filter   Count lines for files which extension is ext1, ext2 ...,
               can be used if '-d' is set
    --help     Show this message
    --version  Show version info
```
