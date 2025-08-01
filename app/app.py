import os, shutil, json

#directories
source_directory = 'unsorted_directory'
gifs_directory = 'gifs'
images_directory ='images'
videos_directory = 'videos'

log_directory = '/Users/will_tang/Documents/GitHub/file_organizer/logs/log.yaml'

#extention dictionary
extension_dictionary = {images_directory : ['.jpg','.png'], 
                        videos_directory : ['.mp4','.mp4a'],
                        gifs_directory   : ['.gif']
                        }      

log_list = []

#it will not look recursively in directories
#need to fix error handling 


#loop through files in a single directory
for filename in os.listdir(source_directory):
    source_path = os.path.join(source_directory, filename)

    # Check if it's a file (not a subdirectory)
    if os.path.isfile(source_path):
        file_name, file_extension = os.path.splitext(filename)
        for key, items in extension_dictionary.items():
            if file_extension.lower() in items:
                destination_path = os.path.join(key, filename)
                break        
        try:
            shutil.move(source_path, destination_path)
            log_list += [(f"Moved {filename} to {destination_path}")]
            

        except Exception as e:
            log_list += [(f"Error moving {filename}: {e}")]

        destination_path = None #this clears the destination after each loop, previous destinations where incorrectly sorting files
    else:
        log_list += [(f"{filename} is a directory")]

with open(log_directory, "w") as f:
    json.dump(log_list, f, indent=4)