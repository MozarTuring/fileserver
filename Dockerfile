FROM nginx:alpine
RUN apk add --no-cache fcgiwrap spawn-fcgi
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
COPY search.cgi /usr/lib/cgi-bin/search.cgi
COPY start.sh /start.sh
RUN chmod +x /usr/lib/cgi-bin/search.cgi /start.sh
CMD ["/start.sh"]
