.PHONY: all clean include

DIR_SRC := src
DIR_PUB := public

SRC:=$(wildcard src/index.md src/*.md)
#DST:=$(addprefix public/, $(SRC:${DIR_SRC}/%.md=%.html))
DST:=$(patsubst ${DIR_SRC}/%.md,${DIR_PUB}/%.html,${SRC})
CSS:=public/github-markdown.css \
     public/highlight.css \
     public/lazyload.min.js \
     public/jquery-3.0.0.min.js \
     public/jquery.idTabs.min.js \
     public/egg.min.js \
     public/clipboard.min.js \
     public/notes.js \
     public/notes.css \
     public/insight.js \
     public/insight.css \



FROM := markdown+abbreviations+east_asian_line_breaks+emoji
#ifeq (,$(DUMB))
#	FROM := $(FROM)+east_asian_line_breaks+emoji
#endif

all: $(DST) $(CSS)
	#echo $(DST)
clone:
	@echo clone some other repo
	# 注意是 https 的链接，不是 git 的。
	# git clone --depth 1 https://github.com/4ker/LeetCode.git leetcode-maskray
	# git clone --depth 1 https://github.com/4ker/cracking-the-coding-interview.git
	# git clone --depth 1 https://github.com/district10/leetcode.git
serve:
	cd public; python -m SimpleHTTPServer
clean:
	rm -rf public/*
include:
	#make -C include
gh:
	git add -A; git commit -m "`uname`"; git push;

${DIR_PUB}/index.html: ${DIR_SRC}/index.md
	@mkdir -p $(@D)
	(perl meta/cat.pl $< | perl meta/drawer.pl || cat $<) | \
	pandoc \
		-V ISINDEX=true \
		-S -s --ascii --mathjax \
		-f $(FROM) \
		--template meta/note.template \
		-o $@
${DIR_PUB}/%/index.html: ${DIR_SRC}/%/index.md
	@mkdir -p $(@D)
	(perl meta/cat.pl $< | perl meta/drawer.pl || cat $<) | \
	pandoc \
		-V ISINDEX=true \
		-V rootdir=../ \
		-S -s --ascii --mathjax \
		-f $(FROM) \
		--template meta/note.template \
		-o $@
${DIR_PUB}/%.html: ${DIR_SRC}/%.md
	@mkdir -p $(@D)
	(perl meta/cat.pl $< | perl meta/drawer.pl || cat $<) | \
	pandoc \
		-V rootdir=../ \
		-S -s --ascii --mathjax \
		-f $(FROM) \
		--template meta/note.template \
		-o $@

public/%: meta/%
	@mkdir -p $(@D)
	cp $< $@

note: n
n:
	$(EDITOR) -p \
		index.md
m:
	$(EDITOR) Makefile
t:
	$(EDITOR) meta/note.template
j:
	$(EDITOR) meta/notes.js
c:
	$(EDITOR) meta/notes.css
sm: sitemap
sitemap:
	touch public/sitemap.html
	find public/ | \
		sed -e "s/^public/-   </" | \
		sed -e "s/$$/>/" | tee sitemap.md | \
		pandoc --ascii -o public/sitemap.html
	cat sitemap.md
