## Basic File Organizer 1.0

This application reads all the files within a directory, creates new directories based on those exetensions, then moves the files.

Example, if the file is an `image.png`, it will create a `/png` directory and move the file.

## app vs app_V2

app.py moves files to specified directories and ignore files that do not have an extension in the extension dictionary.

app_v2.py creates directories based on the extension and then moves the files to the specific directories.

## Future features
These udpates have been made for V2
- [x] better error handling/log keeping - try/except blocks aren't printing to the log
- [ ] move files in sub-directories recursively - need to figure out how to do this with the DRY principle.
- [x] create directories based on the extensions. You would only provide a source directory to search and the application would make directories based on the extensions.
