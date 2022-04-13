import os
os.getcwd()      # Return the current working directory
'C:\\Python310'
os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell
0

import os
dir(os)
#output:
<returns a list of all module functions>
help(os)
#output:
<returns an extensive manual page created from the module's docstrings>

import shutil
shutil.copyfile('data.db', 'archive.db')
#output:
'archive.db'
shutil.move('/build/executables', 'installdir')
#output:
'installdir'

