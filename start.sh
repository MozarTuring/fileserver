#!/bin/sh
spawn-fcgi -s /var/run/fcgiwrap.sock -U nginx -G nginx -- /usr/bin/fcgiwrap
nginx -g 'daemon off;'
