#!/usr/bin/env python3
# Author ID: asmodi2

def read_file_string(file_name):
    f = open(file_name, 'r')
    file_contents = f.read()
    f.close()
    return file_contents

def read_file_list(file_name):
    f = open(file_name, 'r')
    lines = f.read().splitlines()
    f.close()
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
