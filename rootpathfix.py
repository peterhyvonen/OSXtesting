import fileinput 
Path2File = '/Users/travis/build/peterhyvonen/OSXtesting/connector-plugin-sdk/tests/datasets/TestV1/postgres/'
FileNames = ['load_batters.sql', 'load_calcs.sql', 'load_staples.sql']
foreach FileName in FileNames:
  FileName = Path2File+FileName
  with open(FileName) as f:
    newText=f.read().replace('<root_directory>', '/Users/travis/build/peterhyvonen/OSXtesting')
  with open(FileName, "w") as f:
    f.write(newText)
