#!/usr/bin/bash

#sed -f tohtml.sed nce.txt > nce.html 
# get nce.html
sed -f <(cat << EOF
1i <h1> NCE4 </h1>
s///
s/\(^4.*\)/<h2> \1 <\/h2>/
s/^$/<br \/>\n<br \/>/
/^<h2>/,/^<br/{/^<h2>/b;d}
EOF
) nce.txt > nce.html
echo "Output nce.html ..... Done!"

# mark some words
pattern=""
while read word
do
	new="s/ \($word\)/ <b>\1<\/b>/;"		
    pattern=$pattern$new
done < word.txt
sed -i "$pattern" nce.html
echo "Adjust nce.html ..... Done!"

# get mobi file from html file
ebook-convert nce.html nce.mobi --authors 'Wu Tao' --cover nce4.jpg --share-not-sync --title "New Concept Englist" --mobi-toc-at-start --level1-toc '//h:h1' --level2-toc '//h:h2' > /dev/null
echo "Output nce.mobi ..... Done!"
