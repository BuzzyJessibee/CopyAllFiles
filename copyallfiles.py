import os
import shutil

'''
Makes sure that paths are unique. If a path isn't unique,
the function edits the resulting filename to add (1), (2), etc.
'''
def make_paths_unique(destination, file):

   # Split the original file name (ex. Test.txt) to two variables (Test, txt)
   filename, extension = file.rsplit('.', 1)

   # What the destination dir would be without changes
   path = os.path.join(destination, file)

   # File counter for (1), (2), etc
   counter = 1

   while os.path.exists(path):
      new_filename = filename + " (" + str(counter) + ")" + "." + extension
      # Full path for the destination folder, including the new (1), (2), etc
      path = os.path.join(destination, new_filename) 
      counter += 1
   
   # We don't need the full filepath since we already have that,
   # So we only need the new filename (Test1 (1).txt). We use a
   # dummy variable _ to basically throw the other away.
   _, fixed_file = os.path.split(path)
   return fixed_file

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print("Welcome to the copy files utility!")
starting_dir = input("Please enter the complete, absolute SOURCE directory path starting with the drive letter (Windows) or / (Linux/Mac), without using quotes: ")
print(f'You entered: {starting_dir}')
destination_dir = input("Please enter the complete, absolute DESTINATION directory path starting with the drive letter (Windows) or / (Linux/Mac): ")
print(f'You entered: {destination_dir}')

print()

# Probably a better way to do this more gracefully but ehh
print("Testing Paths...")
assert os.path.exists(starting_dir), "I could not find the folder at, "+str(starting_dir)
assert os.path.exists(destination_dir), "I could not find the folder at, "+str(destination_dir)

print()

print("Path checks passed, starting copy process...")

# For every file in the starting_dir, including sub-directories.
for root, dirs, files in os.walk(starting_dir):
   for file in files:

      # Path of the source file to copy
      src_path = os.path.join(root, file)

      # Filename with (1), (2), etc if needed, otherwise the same
      fixed_file = make_paths_unique(destination_dir, file)

      # Full destination path with the fixed file name for copy2()
      dest_path = os.path.join(destination_dir, fixed_file)

      print(f'Copying {src_path}')
      shutil.copy2(src_path, dest_path)

print()

print("All files have been copied and utility will now end. Thanks!")