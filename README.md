# docker-container-service-index
Quick and dirty clickable index of currently active services offered by way of local docker, served up in a docker container, naturally.

The idea is that you bring down this little package and launch.sh it, and it will interrogate/scan the host, parse results, generate a handy little clickable (but static) index and then fire up a simple caddy docker image to serve up this simple index file. Ideally, let this image be the one to serve on port 80, and then you can just navigate to the docker host in a browser for nice, clickable menu of running (and published) containers. Thus, you can stop trying to remember which services are on which port, and you also don't have to run docker ps everytime you want to know.

Of course, if you have a conventional local/non-containerized httpd already running you could just modify the script to deliver the generated index into the webroot of that instead of one more container. It just seemed funny and clever to index docker via docker.

# Appendix

also throw in a bonus cheat sheet for the cli.



TODO: first get all unique docker compose project labels via:
docker ps --format "table {{.Label \"com.docker.compose.project\"}}" | sort -u
then, iterate through them, and for each, filter docker output so we can have docker containers grouped by compose pproject, if any.


TODO: some kind of lightweight scrape of the top page returned IFF it is clearly http/html and has language indicating it is a nav page, and has hyperlinks from there. E.g., mopidy has the iris client linked on index.html

TODO: maybe have a volume mount and then periodically re-run (on the host, maybe cron) the port scan thing, but then diff it from previous and those that _were_ active but no longer are are moved down and greyed out, but not deleted, and new ones added on, without restarting the container.
