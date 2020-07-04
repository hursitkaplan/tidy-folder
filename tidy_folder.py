import os, shutil
import sys
import datetime

def main():
    # folder names and extensions' name
    files = {"Audio files" : [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"], 
            "Torrent files" : [".torrent"], 
            "Compressed files" : [".zip", ".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z"],
            "Disc and media files" : [".bin", ".dmg", ".iso", ".toast", ".vcd"],
            "Data and database files" : [".csv", ".dat", ".db", ".dbf", ".log", ".sav", ".sql", ".tar", ".xml"],
            "Image files" : [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"],
            "Presentation files" : [".key", ".odp", ".pps", ".ppt", ".pptx"],
            "Programming files" : [".c", ".class", ".cpp", ".cs", ".h", ".java", ".pl", ".sh", ".swift", ".vb", ".py"],
            "Executable files" : [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi", ".wsf"],
            "Video files" : [".3g2", ".3gb", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv"],
            "Word processor and text files" : [".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wpd"]}

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

        # if file is the history file than skip
        if file_name == "history.txt": continue
        
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
