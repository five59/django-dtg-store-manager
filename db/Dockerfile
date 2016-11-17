FROM postgres

ENV PG_HOME=/var/lib/postgresql \
    PG_RUNDIR=/run/postgresql

VOLUME ["{$PG_HOME}", "{$PG_RUNDIR}", ]

ADD ./dblib "{$PG_HOME}"
ADD ./dbrun "{$PG_RUNDIR}"
