import os
import shutil

tabs_dict = {'2D materials':['Intro','Basics','Data analysis', 'Data visualization'],
             'Python':['Intro','Basics','Data analysis', 'Data visualization','os'],
            'English' : ['Basics', 'Vocab 1', 'Vocab2'],
            'Charac' : ['AFM','STM','XPS'],
             'Others' : ['Health','Economy','Politics','Social','Life style'],
              'Inspiration' : ['Scientist','Artist','Sports players','Politicians-leaders','Quotes'] }

keys_list = list(tabs_dict.keys())

if os.path.isdir("tab_created") : shutil. rmtree('tab_created')  # rv dir and its contents
os.mkdir('tab_created')  # make dir

parent_dir = "tab_created"

for i in range (len(keys_list)):
    path = os.path.join(parent_dir, keys_list[i])
    os.mkdir(path)

head_temp = """<!DOCTYPE html><html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>logo</title>
	<!-- link to icon page -->
	<link rel="icon" type="image/ico" sizes="100x26" href="../../resources/images/logo.ico">
	<!-- link to cloud stylesheet -->
	<link rel="styleseeht" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" />
	<!-- link to local stylesheet -->
	<link rel="stylesheet" type="text/css" href="../../css/style.css">
</head>

<body><div class="menu-bar"><a ref="#" class="logo">Aymen Mahmoudi</a><ul><li class="active"><a href="..\index.html">Home</a></li>
"""

head_temp_index = """<!DOCTYPE html><html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Home</title>
	<!-- link to icon page -->
	<link rel="icon" type="image/ico" sizes="100x26" href="../resources/images/logo.ico">
	<!-- link to cloud stylesheet -->
	<link rel="styleseeht" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" />
	<!-- link to local stylesheet -->
	<link rel="stylesheet" type="text/css" href="../css/style.css">
</head>

<body><div class="menu-bar"><a ref="#" class="logo">Aymen Mahmoudi</a><ul><li class="active"><a href="index.html">Home</a></li>"""


body_temp_sum =""
body_temp_sum_index=""
for i in range (len(keys_list)):
    list_of_subtabs1=list_of_subtabs2=body_temp1=body_temp2 = ""
    for k in range (len(tabs_dict[keys_list[i]])):
        list_of_subtabs1 +=  f'<li><a href="..\{keys_list[i]}\{tabs_dict[keys_list[i]][k]}.html">{tabs_dict[keys_list[i]][k]}</a></li>'
        list_of_subtabs2 +=  f'<li><a href="{keys_list[i]}\{tabs_dict[keys_list[i]][k]}.html">{tabs_dict[keys_list[i]][k]}</a></li>'
        #print(list_of_subtabs)
    body_temp1 = f'<li><a href="#">{keys_list[i]}</a><div class="sub-menu"><ul>{list_of_subtabs1}</ul></div></li>'
    body_temp2 = f'<li><a href="#">{keys_list[i]}</a><div class="sub-menu"><ul>{list_of_subtabs2}</ul></div></li>'
    body_temp_sum+=body_temp1
    body_temp_sum_index+=body_temp2



for i in range (len(keys_list)):   
    for k in range (len(tabs_dict[keys_list[i]])):
        path_creation = 'tab_created'+'\\'+keys_list[i]+'\\'+tabs_dict[keys_list[i]][k]+'.html'
        path_reading = 'tab_content'+'\\'+keys_list[i]+'\\'+tabs_dict[keys_list[i]][k]+'.html'
        #print(list_of_subtabs)
        with open(path_reading,'r') as file:
                content = file.read()   
        with open(path_creation,'w') as file:
            file.write(head_temp + body_temp_sum+"</ul></div>"+content+'</body></html>')

index_content = 'eLLLMMM'
with open('tab_created\index.html','w') as file:
            file.write(head_temp_index + body_temp_sum_index+"</ul></div>"+index_content+'</body></html>')

            



  

