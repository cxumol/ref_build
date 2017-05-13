> this work is mainly based on [district10/notes](https://github.com/district10/notes) 
and the search engine plug-in is transplanted from [zthxxx/hexo-theme-Wikitten](https://github.com/zthxxx/hexo-theme-Wikitten)  
and many thanks to [iHamsterball](https://github.com/iHamsterball)

[demo](http://ref.cxumol.com)

# Deployment instruction

This repository contains only the compiling part of the whole note-taking website system.   
You may also need another repository to store your contents (including some file requested by cloud-based compiling/deployment, maybe)

## Quick start

1. create a new repository on <https://gitlab.com>
2. write your first note as following:  
```markdown
---
title: haha
any: words
---

-   I love [telegram](https://telegram.org) -<
    :   -   contact me `@cxumol`
        -   follow my channel `@cxumolket` or `@cxumeme` or `@cxumolearn`
```
3. copy my [`.gitlab-ci.yml`](https://gitlab.com/cxumol/ref/raw/master/.gitlab-ci.yml) to your repository, and personalize it to your own version.
4. push your git commits to gitlab.com and then all things left are done by gitlab pipelines.

> If you are using the default domain on gitlab.io , please change the value of `ROOT_URL` in `./meta/note.template` to something like `/repo/`

## How it works

### requirement

- pandoc 1.17.1+
- python 2.7+
- perl 5
- git make

### building

`Makefile` is the makefile for building the site on localhost, while `Makefile_ol` is the one for an online version, which uses CDN to boost loading of some static files.

all `.md` notes should be found in `./src/`.   
In my workflow I use `git clone` to download the other git repo folder so that the source notes can be integrated with compiler. 
However it's not the only way for integration.

Assuming all your `.md` notes have already been saved  to `./src/`

- `make all` to compile a website to `./public/`
- `make serve` to serve the note site on localhost
- `make sitemap` may not work currently. 

The steps of generating `index.md` and  `content.json`(search engine index) are not inside `Make file`.   
In order to enable those features, you should run following command before `make all`

- `python meta/index_gen.py "your source folder" "title of home page"`
- `python meta/json_gen.py "your source folder" "your website folder"`

## Deployment

Feel free to compile your content on your own machine or run it anywhere as you like,
but we recommend you using an online service to compile & deploy your note site cloudy.

There must be more than 3 ways for online building. 
for now just 3 of them are introduced there.

1. gitlab.com CI -> gitlab.io  
   an example are presented above (see Quick start)

> (besides USTC) Anyone knows self-hosted gitlab serving Internet user? pls tell me.   
  work flow controlled by `.gitlab-ci.yml`  

2. github -> travis-ci -> gh-pages  

>  NOT recommend. Since the files for web browsing are compiled version and your source files have been version-tracked.
There is no reason to track "b0n0ry" files by git, but at github pages you have to.  
 work flow controlled by `.travis.yml` 

3. github -> netlify

> not tried yet. it would work fine as netlify supports pandoc.(80% confidence)  
  (maybe can) controlled by `Makefile`

## Contributing

- Fork it!
- Create your feature branch: `git checkout -b my-new-feature`
- Commit your changes: `git commit -am 'Add some feature'`
- Push to the branch: `git push origin my-new-feature`
- Submit a pull request

### for contribution, you can

create:  

- [ ] a sample of `.travis.yml` 
- [ ] a sample of `Makefile` for netlify
- [ ] more ways to build online

fix:

- [ ] make `make sitemap` work

or whatever you'd love to contribute!

---
# 部署说明

该 repo 仓库仅为编译部分的程序。  
或许你还需要一个存放 `.md` 原文件的仓库。
(可能包含某些云构建所需的文件)

……
懒得写了，凑合着看英文吧。  
其他内容，比如创造历程和理念，都记载于[构建笔记系统](http://www.kancloud.cn/cxumo/noting)这份文档
