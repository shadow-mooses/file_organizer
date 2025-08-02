import os, shutil, json

#local directories
log_directory = 'logs/log'
unsorted_directory = 'unsorted_directory' #location of files to be sorted
extension_directory = 'ext_directory/' #target location for new directories and sorted files should the files

#variables
extension_dictionary = {}
log_list = []


#step 1 - loop through all files and create a dictionary of extensions
for filename in os.listdir(unsorted_directory):
    source_path = os.path.join(unsorted_directory, filename)

    # Check if it's a file (not a subdirectory)
    if os.path.isfile(source_path):
        file_name, file_extension = os.path.splitext(filename)
        ext_folder_name = file_extension.replace('.','')
        extension_dictionary[ext_folder_name] = file_extension
    else:
        continue

#step 2 - make directories for all the extension types - try block isn't printing to the log
for key in extension_dictionary.keys():
    try:
        os.mkdir(extension_directory + key)
        log_list += [(f'Created Directory {extension_dictionary + key}')]
    except FileExistsError:
        print((f'Directory {extension_directory + key} already exists'))
        log_list += [(f'Directory {extension_directory + key} already exists')]
    except FileNotFoundError:
        print(f'{extension_directory} does not exist')
        log_list += [(f'{extension_directory} does not exist')]

#step 3 - move the files to the correct directory
for filename in os.listdir(unsorted_directory):
    source_path = os.path.join(unsorted_directory, filename)

    # Check if it's a file (not a subdirectory)
    if os.path.isfile(source_path):
        file_name, file_extension = os.path.splitext(filename)
        try:
            destination_path = extension_directory + file_extension.replace('.','')
            shutil.move(source_path, destination_path)
            log_list += [(f"Moved {filename} to {destination_path}")]

        except Exception as e:
            log_list += [(f"Error moving {filename}: {e}")]

        destination_path = None #this clears the destination after each loop, previous destinations where incorrectly sorting files
    else:
        log_list += [(f"{filename} is a directory")]

#dump json log
with open(log_directory, "w") as f:
    json.dump(log_list, f, indent=4)

