#!/usr/bin/env python3
# Author ID: sparaskevilo

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    return read_data


def read_file_list(file_name):
    string_data = read_file_string(file_name)# Use read_file_string to get string data so we can use split command
    strip_data = string_data.split('\n') #split to remove newline from string
    line_data = list(strip_data) # return its entire contents as a list of lines without new-line characters
    line_data.remove("") #Remove empty space list item
    return line_data

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends string_of_lines to the end of the file
    f = open(file_name, 'a')
    string_file = f.write(string_of_lines)
    f.close()
    return string_file

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(str(line) + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    line_data = read_file_list(file_name_read) #Get list of lines from read_file_list function
    f = open(file_name_write, "w")
    i = 0 #Use index number as counter
    for line in line_data: #Iterate through each line/list item
        i = i+1 #Adjust i to keep track of line numbers
        f.write(str(i) + ":" + str(line) + "\n") #Convert i and list items to string so they can be concatenated and written as string
    f.close
        
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))