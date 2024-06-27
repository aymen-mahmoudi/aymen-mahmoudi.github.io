tabs = dict{'Python':['Intro','Basics','Data analysis', 'Data visualization'],
            'English' : ['Basics', 'Vocab 1', 'Vocab2'],
             'Charac' : ['AFM','STM','XPS'] }




# tabs_cluster = 

    '<li><a href="#">2D materials</a>'+'\n'+'<div class="sub-menu">
          <ul>
            <li><a href="tabs/Charac/AFM.html">Description</a></li>
            <li><a href="tabs/Charac/AFM.html">Optical Characterization</a></li>
            <li><a href="tabs/Charac/SEM.html">Physical Characterization</a></li>
            <li><a href="#">X-ray methods</a></li>
          </ul>
        </div>
      </li>

part1 = '<li><a href="#">'+key1+'</a>'+'\n'+'<div class="sub-menu">
part2=''
for i in dickey1:
    part2=part2+'<li><a href="tabs/'+keyi+/valueij+'.html'>+'value1'+'</a></li>'




# To open a file via python we can use with open.

lines = []

with open('index.html','r') as file_r:
    lines = file_r.readlines()
    #content = file_r.read()



start_index = lines.index('<!-- START -->\n')
end_index = lines.index('<!-- END -->\n') + 1

print(lines.index('<!-- START -->\n'))
print(lines.index('<!-- END -->\n'))

'''
k = []
for i in lines:
    j = i.lstrip()
    k.append(j)
print(k[4])

print(k.index('<title>Drop Down Menu Design</title>\n'))

'''


with open('index1.html','w') as file_w:
    for n, line in enumerate(lines):
        if n not in range(start_index,end_index):
            file_w.write(line)








   



