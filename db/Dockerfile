FROM postgres

ENV PG_HOME=/var/lib/postgresql \
    PG_RUNDIR=/run/postgresql

ADD ./dblib "{$PG_HOME}"
ADD ./dbrun "{$PG_RUNDIR}"
