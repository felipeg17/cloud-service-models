FROM nginx:1.27

COPY default.conf /etc/nginx/conf.d/default.conf
COPY demo.html /usr/share/nginx/html/index.html

EXPOSE 8080
