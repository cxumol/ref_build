#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,os.path
import sys
import re,json

# root_path = "../public/"
root_path=str(sys.argv[2])
src_path=str(sys.argv[1])

print(src_path,root_path)

def browser(path):   
    ''' get all absolute path of markdown and return a list'''
    if not os.path.isdir(path):   #判断path是否为路径
        print("err! path %s check failed"%path)
        return 

    li=[]
    for fdir, folder, files in os.walk(path):   
    #绝对路径，文件夹名，文件名
        for i in files:  
            dir = os.path.join(fdir, i)    #组成绝对路径文件名
            if os.path.splitext(i)[1] in ('.md','.mdown','.markdn','.markdown'):
                li.append(dir)
    return li
    # 返回所有md文件列表


if __name__ == '__main__':

    md_dir=browser(src_path)
    # print md_dir #debug

    container={"posts":[],"pages":[]}
    for md_path in md_dir:
        md_f=open(md_path,"r")
        md_content=md_f.read()
        try:
            title=re.search("title: (.*)", md_content).group(1) or ""
        except:
            print "path :"+md_path
            title="(untitled)"
        try:
            txt_f=os.popen('pandoc -f markdown+abbreviations+east_asian_line_breaks+emoji -t plain --wrap=none %s'%md_path)
            text=txt_f.read().replace('\n-   \n','').replace('    ','').replace('\n\n','\n').replace('-<','').replace('+<','')
            txt_f.close()
        except:
            print "path :"+md_path
            print md_content
            text = md_content  or ""

        html_path=re.search( "%s.(.*)"%src_path,os.path.splitext(md_path)[0] ).group(1) + ".html" or ""

        container["posts"].append({"title":title,"path":html_path,"text":text})

    if not os.path.isdir(root_path): os.system('mkdir '+' "%s" '%root_path)
    json_f=open(root_path+'/content.json','w')
    # print json_f.name #debug
    json.dump(container,json_f,ensure_ascii=False)
    json_f.close()