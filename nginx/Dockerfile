FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf

ADD conf.d/ /etc/nginx/conf.d
ADD proxy_params.conf /etc/nginx