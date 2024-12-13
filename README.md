# docker-container-service-index
Quick and dirty clickable index of services offered by way of docker, served up in a docker container, naturally.

The idea is that you bring down this little package and launch.sh it, and it will interrogate/scan the host, parse results, generate a handy little clickable (but static) index and then fire up a simple caddy docker image to serve up this simple index file. Ideally, let this image be the one to serve on port 80, and then you can just navigate to the docker host in a browser for nice, clickable menu of running (and published) containers. Thus, you can stop trying to remember which services are on which port, and you also don't have to run docker ps everytime you want to know.

Of course, if you have a conventional local/non-containerized httpd already running you could just modify the script to deliver the generated index into the webroot of that instead of one more container. It just seemed funny and clever to index docker via docker.
