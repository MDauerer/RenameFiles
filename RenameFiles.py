import pathlib
#change the first "\" in the path to a "/" for example C:/bla\blubb

def rename_files(pathname='C:/Users\manue\Desktop\kekwfolder'):
    for path in pathlib.Path(pathname).iterdir():
        if path.is_file():
            contains_digit = False        # only rename the file, if the timestamp is still in the filename, to avoid duplicate namechanges by accident
            old_name = path.stem

            for character in old_name:
                if character.isdigit():
                    contains_digit = True
            
            if contains_digit:
                old_extension = path.suffix
                directory = path.parent
                new_name =  old_name[6:] + old_extension
                path.rename(pathlib.Path(directory, new_name))
        
        if path.is_dir():
            rename_files(path)

if __name__ == "__main__":
    rename_files()
