import os
import subprocess
import socket
import re

# first, just get a list of defnitely mapped through ports from docker itself
# then probe them, maybe with nmap?
# then, if html, try some kind of XML parse DOM/walk for interesting details and metadata
# put it all together in some kind of nice fancyindexing. Kind of like Apache fancy indexing idea. But statically generate it.
# finally, throw up a docker image of our own to serve up the fancy index 

# https://xael.org/pages/python-nmap-en.html

stuff = ""

#'docker ps --format "{{.Names}}__{{.Image}}\t{{.Ports}}"'
proc = subprocess.run([ 'docker','ps','--format','"{{.Names}}__{{.Image}}\t{{.Ports}}"'], capture_output=True, text=True)

raw = proc.stdout
print(raw.split("\n"))
for line in raw.split("\n"):
    #print("\n\t"+line)
    tokens = line.split("\t")
    container_name = tokens[0].replace('"',"")
    print(container_name)
    for token in tokens[1:]:
        print("\t\t"+token)
        for item in token.split(","):
            if "0.0.0.0" in item:
                urlish = item.replace("0.0.0.0","http://"+socket.getfqdn())
                urlish = re.sub("->.*/tcp","",urlish)
                try:
                    portpart = urlish.split(":")[2].split("-")[0]
                    port = int(portpart)
                    service = socket.getservbyport(port)
                    print("\t\tservice: "+service)
                    if service == "21":
                        urlish = urlish.replace("http://","ftp://")
                except OSError:
                    # default to http.
                    print("\t\t(service default)")
                print("\t\t"+urlish)
                clickable = '<a href="%s">%s</a>'%(urlish,container_name+" - "+portpart)
                print(clickable)
                stuff += "<li>"+clickable+"</li>"
        
dumplet='''
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/><title>AutoLinks for Docker Containers</title>
    <style>
        body { padding: .5em; font-family: system-ui; background-color:lightgrey;}
        li { padding: .75em; }
    </style>
</head>
<body> <ul> %s </ul> </body>
</html>
'''%stuff

f = open('docker_auto_links.html', 'wt', encoding='utf-8')
f.write(stuff)
f.close()


#docker run -p 80:80 -v $PWD/docker_auto_links.html:/usr/share/caddy/index.html
print("docker run -p 80:80 -v $PWD/docker_auto_links.html:/usr/share/caddy/index.html")
proc = subprocess.run([ 'docker','run','-d','-p','80:80','-v',os.getcwd()+'/docker_auto_links.html:/usr/share/caddy/index.html','caddy' ] , capture_output=True, text=True)
##with open("/tmp/docker_auto_links_output.log", "a") as output:
        ##subprocess.call("docker run -p 80:80 -v $PWD/docker_auto_links.html:/usr/share/caddy/index.html caddy", shell=True, stdout=output, stderr=output)
print (proc.stdout)
print (proc.stderr)
