#!/bin/sh

RPMDIR=`mktemp -d /tmp/rpmbuild.XXXXXXXX`
mkdir -p "$RPMDIR/BUILD"   \
         "$RPMDIR/RPMS"    \
         "$RPMDIR/SRPMS"   \
         "$RPMDIR/SOURCES" \
         "$RPMDIR/SPECS"

cp source/* "$RPMDIR/SOURCES"
cp capture-replay-db.spec "$RPMDIR/SPECS"

rpmbuild "$RPMDIR/SPECS/capture-replay-db.spec"       \
           --define "_topdir $RPMDIR"                 \
           --define "tgzroot apache-cassandra-0.6.1"  \
           --buildroot "$RPMDIR/BUILDROOT"            \
           --clean -ba

cp $RPMDIR/RPMS/x86_64/*.rpm .
rm -rf "$RPMDIR"
