FROM postgres

ENV PG_HOME=/var/lib/postgresql \
    PG_RUNDIR=/run/postgresql
# VOLUME ["${PG_HOME}", "{$PG_RUNDIR}"]

ADD ./db/dblib /var/lib/postgresql/
ADD ./db/dbrun /run/postgresql/
