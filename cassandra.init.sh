#!/bin/bash
#
# /etc/init.d/cassandra
#
# Startup script for Cassandra
#
# chkconfig: 2345 20 80
# description: Starts and stops Cassandra

. /etc/rc.d/init.d/functions

export JAVA_HOME=/usr/lib/jvm/jre
export CASSANDRA_HOME=/opt/cassandra
export CASSANDRA_INCLUDE=/opt/cassandra/bin/cassandra.in.sh
export CASSANDRA_CONF=/opt/cassandra/conf
export CASSANDRA_OWNR=cassandra
log_file=/var/log/cassandra/cassandra.log
pid_file=/var/run/cassandra/cassandra.pid
CASSANDRA_PROG=/opt/cassandra/bin/cassandra


case "$1" in
    start)
        # Cassandra startup
        echo -n "Starting Cassandra: "
        su $CASSANDRA_OWNR -c "$CASSANDRA_PROG -p $pid_file" > $log_file 2>&1
        echo "OK"
        ;;
    stop)
        # Cassandra shutdown
        echo -n "Shutdown Cassandra: "
        su $CASSANDRA_OWNR -c "kill `cat $pid_file`"
        echo "OK"
        ;;
    reload|restart)
        $0 stop
        $0 start
        ;;
    status)
        status -p $pid_file cassandra
        ;;
    *)
        echo "Usage: `basename $0` start|stop|status|restart|reload"
        exit 1
esac

exit 0
