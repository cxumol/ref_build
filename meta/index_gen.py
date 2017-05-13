#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,os.path,sys
import re

SRC_DIR = str(sys.argv[1])
ttl= unicode(sys.argv[2]) or "ref"

def browser(path):    
    ''' get all absolute path of markdown and return a list'''
    if not os.path.isdir(path):   
        print("err! path %s check failed"%path)
        return 

    li=[]
    for fdir, folder, files in os.walk(path):   
        for i in files:  
            dir = os.path.join(fdir, i)    #组成绝对路径文件名
            if os.path.splitext(i)[1] in ('.md','.mdown','.markdn','.markdown'):
                li.append(dir)
    return li
    # 返回所有md文件列表

if __name__ == '__main__':

    md_dirs = browser( SRC_DIR )
    f=open( SRC_DIR+'/index.md' , 'a+' )
    f.write(u"---\ntitle: %s\n---\n\n"%ttl)
    for md_path in md_dirs:
        tt=re.search( "%s.(.*?).md"%SRC_DIR, md_path ).group(1) or ""
        html_path=re.search( "%s.(.*)"%SRC_DIR,os.path.splitext(md_path)[0] ).group(1) + ".html" or ""
        f.write("*   [%s](%s)  \n"%( tt, html_path ))
    f.close()