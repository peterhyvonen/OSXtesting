import fileinput with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
  for line in file:
    print(line.replace('<root_directory>', '/Users/travis/build/peterhyvonen/OSXtesting'), end='')
