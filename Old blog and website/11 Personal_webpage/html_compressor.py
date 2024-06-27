# After editing the files in the dev folder, use this scripts to generate a compressed copy in the public folder.and
# It allows also to copy the css and resources folders
# This script will erase the whole content of the public folder before copying

import htmlmin

path_reading = ["dev\index.html","dev\events.html"]
path_writing = ["public\index.html","public\events.html"]

def html_compress(path_reading,path_writing):
    with open(path_reading,'r') as file:
        content = file.read()  
    #print(content)
    content = htmlmin.minify(content, remove_empty_space=True, remove_comments=True)

    with open(path_writing,'w') as file:
        file.write(content)
        
for i in range(len (path_reading)):
    html_compress(path_reading[i],path_writing[i])

print('DONE.....')