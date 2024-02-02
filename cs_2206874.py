def modify_file(file_path):

    #Open sfs.py for reading
    with open(file_path, 'r') as file:
        lines = file.readlines()


    #Open sfs.py for writing
    with open(file_path, 'w') as file:
        #Write lines 1-51 to the new file as per the assignment brief
        for i in range(51):
            file.write(lines[i])

        #Insert this at line 52
        modified_line_52 = lines[51].rstrip('\n') + '; print("Virus")\n'
        file.write(modified_line_52)

        #Write the rest of the file from line 53
        for line in lines[52:]:
            file.write(line)


#Check to see if it works on the sfs.py file
#Run sfs.py afterwards from command line to see if the new line has been inserted correctly

modify_file('sfs.py')