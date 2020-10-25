import os
import pathlib
#change the first "\" in the path to a "/" for example C:/bla\blubb

for path in pathlib.Path('C:/Users\manue\Desktop\kekwfolder').iterdir():
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


