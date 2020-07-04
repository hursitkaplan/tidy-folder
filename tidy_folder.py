import os, shutil
import sys
import datetime

def main():
    # folder names and extensions' name
    files = {"executables" : [".exe"], 
            "torrent files" : [".torrent"], 
            "pdf files" : [".pdf"],
            "zip files" : [".zip"]}

    # Check if arguments is valid
    if len(sys.argv) != 2:
        print("Usage: tidy_folder path")
        sys.exit(1)

    # Get base path from the user via command line
    base_path = sys.argv[1]

    # Path validation
    if not os.path.isdir(base_path):
        print("Invalid path")
        sys.exit(1)

    # change cwd to given path
    os.chdir(os.path.abspath(base_path))

    # Create base folders for extensions
    for folder_name in files.keys():
        # get folder path
        folder_path = os.path.join(base_path, folder_name)

        # If folder does not exist create the folder with given name
        if os.path.isdir(folder_path) == False:
            os.mkdir(folder_path)

    # open history file in append mode to write what is changed
    f = open("history.txt", "a")

    # loop in files in the base folder
    for file_name in os.listdir(base_path):
        # loop in files dict
        for folder_name, extensions in files.items():
            
            # If extension is not correct
            if extension_checker(extensions, file_name) == False: continue
            
            # create source and destination path for file that are gonna be moved
            src_path = os.path.join(base_path, file_name)
            dst_path = os.path.join(base_path, folder_name, file_name)

            # print details in the command line
            print(f"filename: {file_name}")
            print(f"source path: {src_path}")
            print(f"destionation path: {dst_path}")
            print("-"*100)

            # try to move file else print an error message and close the program
            try:
                # move file to folder that it is belongs
                shutil.move(src_path, dst_path)
            except:
                # print error message and close the program
                print(f"File ({file_name}) could not moved!")
                print()
                print("Please check the file before start the program")

                # write the error message into the file
                f.write(f"File ({file_name}) could not moved!\n")
                sys.exit(1)  
            # If program does not give error write details into the file
            else:
                # write details into the file
                f.write(f"filename: {file_name}\n")
                f.write(f"source path: {src_path}\n")
                f.write(f"destionation path: {dst_path}\n")
            
            # print line between details
            f.write("-"*100 + "\n")

    # get the current time
    time = datetime.datetime.now()
    # write time to text file
    f.write(time.strftime("%m/%d/%Y, %H:%M:%S\n"))

    # print * after each use
    f.write("*"*100 + "\n")

    print("Files successfully moved")

    # close the history.txt
    f.close()
    # wait for user to see details
    input()

def extension_checker(extensions, file_name):
    """Check given file names with extensions"""

    for extension in extensions:
        # if extension is not matched pass this loop
        if (file_name.endswith(extension)) == True: 
            return True
        # if extensions not matched with the file's extension
        return False

# stars the program
main()