# ------------------------------------------------------------------------------
# Macro definition
# ------------------------------------------------------------------------------

%define instdir %{buildroot}
%define makedir .

# ------------------------------------------------------------------------------
# Introduction section
# ------------------------------------------------------------------------------

Summary: Capture/Replay Database (Cassandra)
Name: capture-replay-db
Version: 0.6.1
Release: 1
Group: Applications/Databases
Requires: jre >= 1.6.0
Vendor: Collaborative Software Initiative
License: Apache License, Version 2.0
Source: apache-cassandra-%{version}-bin.tar.gz
%description
This is nothing more than a repackaging of the Apache Cassandra database server
pre-configured to work with the CSI Capture/Replay facility

# ------------------------------------------------------------------------------
# Prep section (prepare source for build/packaging)
# ------------------------------------------------------------------------------

%prep
%setup -n %{tgzroot}


# ------------------------------------------------------------------------------
# Build section
# ------------------------------------------------------------------------------

%build
mkdir -p %{instdir}/opt/cassandra


# ------------------------------------------------------------------------------
# Install section
# ------------------------------------------------------------------------------

%install
cp -R %{makedir}/* %{instdir}/opt/cassandra


# ------------------------------------------------------------------------------
# Clean section
# ------------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT


# ------------------------------------------------------------------------------
# Files section
# ------------------------------------------------------------------------------

%files
/opt/cassandra/bin
/opt/cassandra/lib
%doc /opt/cassandra/*.txt
%doc /opt/cassandra/javadoc
%config /opt/cassandra/conf
%config /opt/cassandra/scripts
%config /opt/cassandra/interface


# ------------------------------------------------------------------------------
# Post-install script
# ------------------------------------------------------------------------------

%post
useradd -r cassandra
mkdir -p /var/log/cassandra /var/run/cassandra /var/lib/cassandra
chown cassandra:cassandra /var/log/cassandra /var/run/cassandra /var/lib/cassandra
cp /opt/cassandra/scripts/cassandra /etc/init.d/
chmod 755 /etc/init.d/cassandra
chkconfig --add cassandra
service cassandra start


# ------------------------------------------------------------------------------
# Pre-uninstall script
# ------------------------------------------------------------------------------

%preun
service cassandra stop
chkconfig --del cassandra
rm -rf /etc/init.d/cassandra /var/run/cassandra
userdel cassandra
rm -rf /opt/cassandra
