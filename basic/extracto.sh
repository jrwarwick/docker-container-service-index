TGTURL="$1"
curl -L $TGTURL > /tmp/container_response_body.html
if [ $? -ne 0 ] ; then
	echo " <!-- probably not really html serving --> " > /tmp/container_summary.html
else
	/usr/bin/echo -n "<p><img src=\"${TGTURL}/" > /tmp/container_summary.html
	xmllint --html  --xpath '//html/head/link[@rel="icon"]/@href' /tmp/container_response_body.html 2>/dev/null | head -1 | cut -d'"' -f2 | tr -d '\n' >> /tmp/container_summary.html
	/usr/bin/echo -en "\" onerror=\"this.style.display='none';\" />\t" >> /tmp/container_summary.html
	xmllint --html  --xpath '//html/head/title/text()' /tmp/container_response_body.html 2>/dev/null >> /tmp/container_summary.html
	/usr/bin/echo -en "</p>\n<p>" >> /tmp/container_summary.html
	xmllint --html  --xpath '//html/head/meta[@name="description"]/@content' /tmp/container_response_body.html 2>/dev/null | cut -d'"' -f2 >> /tmp/container_summary.html
	/usr/bin/echo -en "</p>\n" >> /tmp/container_summary.html
fi
cat /tmp/container_summary.html
