import fileinput 
Path2File = '/Users/travis/build/peterhyvonen/OSXtesting/connector-plugin-sdk/tests/datasets/TestV1/postgres/'
Path2Config = '/Applications/Tableau Desktop 2019.2.app/Contents/MacOS/tabquerytool'
FileNames = ['load_batters.sql', 'load_calcs.sql', 'load_staples.sql']
ConfigFile = 'config/tdvt/tdvt_override.ini'
for FileName in FileNames:
  FileName = Path2File+FileName
  with open(FileName) as f:
    newText=f.read().replace('<root_directory>', '/Users/travis/build/peterhyvonen/OSXtesting')
  with open(FileName, "w") as f:
    f.write(newText)
with open(ConfigFile) as f:
  newText=f.read().replace('', Path2Config)
with open(ConfigFile, "w") as f:
  f.write(newText)
