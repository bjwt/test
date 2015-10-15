#!/usr/bin/bash

ebook-convert $1 $2 --authors 'Wu Tao' --cover nce4.jpg --share-not-sync --title "New Concept English" --mobi-toc-at-start --level1-toc '//h:h1' --level2-toc '//h:h2'
