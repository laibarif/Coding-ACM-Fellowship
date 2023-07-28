from os import listdir
from os.path import isfile,join

files_list = [f for f in listdir('C:\Program Files\Python311') if isfile(join('C:\Program Files\Python311',f))] 