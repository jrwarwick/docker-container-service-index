#!/usr/bin/sh

docker stop docker-server-portsmania
docker rm docker-server-portsmania
#HOST Net inspection needs to happen above the docker container context. Too much security isolation once in docker context.
#so, this python script does the inspection, parsing, and generates a static index file  and then kicks off simple docker container to serve it up.
python3 ./basic/docker_ports_autolist.py

cp /etc/motd ./banner.txt
#TODO: if banner.txt is -z ero bytes big, auto dig up something cool and fun.
#
#actually, probably, TODO: split the docker_ports_autolist.py up a little. It should generate the index, but maybe the docker invocation to serve it should be here instead of embedded in the script. Either that, or this here launch.sh should just be discarded.

#This next section is purely supplementary, not really necessary. Or working at this point.
#docker build -t portsmania .
#docker run -it portsmania
#docker run --name portsmania-discovery -d portsmania

