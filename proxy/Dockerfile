FROM nginx

# Remove default.conf
RUN rm /etc/nginx/conf.d/default.conf

# Copy in custom conf
COPY default.conf etc/nginx/conf.d/

# service nginx configtest
# CMD ["service", "nginx ", "configtest"]

# service nginx restart
# CMD ["service", "nginx", "restart"]

EXPOSE 80