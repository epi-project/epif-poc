FROM nginx

COPY ./default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/nginx/includes
COPY ./proxy.conf /etc/nginx/includes/proxy.conf

COPY ./backend-not-found.html /var/www/html/backend-not-found.html
