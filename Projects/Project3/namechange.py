import os

path = 'C:\Test'
for filename in os.listdir(path):
        os.rename(os.path.join(path,filename),os.path.join(path, filename.replace(' ',"_")))