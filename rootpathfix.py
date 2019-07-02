import fileinput 
FileName = 'load_batters.sql'
with open(FileName) as f:
  newText=f.read().replace('<root_directory>', '/Users/travis/build/peterhyvonen/OSXtesting')
with open(FileName, "w") as f:
  f.write(newText)
