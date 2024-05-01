FROM postgres:latest
RUN mkdir -p /var/lib/postgresql/secure
COPY ./secure/postgres-passwd /var/lib/postgresql/secure
EXPOSE 5432