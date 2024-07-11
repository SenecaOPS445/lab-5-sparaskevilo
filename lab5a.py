#!/usr/bin/env python3
# Author ID: sparaskevilo

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open('data.txt', 'r')
    read_data = f.read()
    f.close()
    return read_data


def read_file_list(file_name):
    string_data = read_file_string(file_name)# Use read_file_string to get string data so we can use split command
    strip_data = string_data.split('\n') #split to remove newline from string
    line_data = list(strip_data) # return its entire contents as a list of lines without new-line characters
    line_data.remove("") #Remove empty space list item 
    return line_data

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))