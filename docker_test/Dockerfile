FROM postgres:latest
RUN mkdir -p /var/lib/postgresql/secure
RUN pwd
COPY ./docker_test/secure/postgres-passwd /var/lib/postgresql/secure
EXPOSE 5432