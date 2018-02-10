# Kevinsapps.com

Repo for kevinsapps.com, which is a collection of projects I've worked on in the past (or am currently working on).


## Install

When cloning don't forget to add submodules:

```
git submodule update --init --recursive
```

Run server with:

```
docker-compose build
docker-compose up
```


## Services

Current services are:

* [analytics](https://analytics.kevinsapps.com/) - Websocket analytics application with oauth login for Reddit.
* [music](https://music.kevinsapps.com/) - Scrobble recent plays from foobar2000, and save them for analysis later. 
* [vochuts](https://vochuts.kevinsapps.com/) - Really super simple hut booking application prototype for the UBC Outdoor Club (VOC)
* [flask](https://flask.kevinsapps.com/) - Super simple flask echo server.  
* [ghost](https://blog.kevinsapps.com/) - Ghost blog - currently empty, but may move over posts from my [old blog](https://kevinburton.ca/blog/) eventually.
* [nextcloud](http://files.kevinsapps.com/) - Self hosted photos and static files for sharing.

Supporting cast:

* [caddy](https://caddyserver.com/) - Web server.
* [postgres](https://www.postgresql.org/) - Preferred database.
* [redis](https://redis.io/) - Data store for things like Channels and background tasks.

Discontinued services:

* deluge

## Server info

Currently hosted on a VPS with 1GB RAM, and 1 vCPU from a certain provider related to non-analogue maritime infrastructure.   