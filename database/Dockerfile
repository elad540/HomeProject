FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD 123
ENV MYSQL_DATABASE database
ENV MYSQL_USER user
ENV MYSQL_PASSWORD password

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
