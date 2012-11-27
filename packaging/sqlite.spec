Name:           sqlite3
Version:        3.7.14
Release:        0
License:        SUSE-Public-Domain
%define tarversion 3071400
Summary:        Embeddable SQL Database Engine
Url:            http://www.sqlite.org/
Group:          Productivity/Databases/Servers
Source0:        sqlite-autoconf-%tarversion.tar.gz
Source1:        baselibs.conf
#
BuildRequires:  pkg-config
BuildRequires:  readline-devel
Requires:       libsqlite3 = %{version}
Provides:       sqlite = %{version}
Obsoletes:      sqlite < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is a server and the SQLite library reads and writes
directly to and from the database files on disk.

SQLite can be used via the sqlite command line tool or via any
application that supports the Qt database plug-ins.

%package -n libsqlite3
Summary:        Shared libraries for the Embeddable SQL Database Engine
Group:          Development/Libraries/C and C++

%description -n libsqlite3
This package contains the shared libraries for the Embeddable SQL
Database Engine.

SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is a server and the SQLite library reads and writes
directly to and from the database files on disk.

SQLite can be used via the sqlite command line tool or via any
application that supports the Qt database plug-ins.

%package devel
Summary:        Embeddable SQL Database Engine
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libsqlite3 = %{version}
Provides:       sqlite-devel = %{version}
Obsoletes:      sqlite-devel < %{version}

%description devel
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server; SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

SQLite can be used via the sqlite command-line tool or via any
application which supports the Qt database plug-ins.

%prep
%setup -q -n sqlite-autoconf-%tarversion

%build
export CFLAGS="-DSQLITE_ENABLE_COLUMN_METADATA -DSQLITE_ENABLE_FTS4"
%configure --disable-static
make

%install
%make_install

%post -n libsqlite3 -p /sbin/ldconfig

%postun -n libsqlite3 -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/bin/sqlite3
%doc %{_mandir}/man1/*

%files -n libsqlite3
%defattr(-,root,root)
%{_libdir}/libsqlite*.so.*

%files devel
%defattr(-,root,root)
/usr/include/*.h
%{_libdir}/libsqlite*.so
%{_libdir}/pkgconfig/sqlite3.pc

