# CopyAllFiles
A simple Python script to copy all files, in all subdirectories of a folder to a single destination directory

Originally created for my father to easily copy all his music files to the root of an SD card that would work with his car radio.

## Instructions
1. Enter the absolute path for the root source directory (where all the subdirectories are located)
2. Enter the absolute path for the destination directory
3. The utility runs!

## Specifics
The utility makes sure that all filenames are unique in the destination directory by dynamically adding (1), (2) etc. to the end of the filename.
For example, if you have 3 `Text.txt` files, the destination will have `Text.txt, Text (1).txt, Text (2).txt` 
