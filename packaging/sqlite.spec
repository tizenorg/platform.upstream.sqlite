Name:       sqlite
Version:    3.8.10.2
Release:    2
License:    PD

Summary:    Embeddable SQL Database Engine
Url:        http://www.sqlite.org/
Group:      System/Database

Source:     %{name}-%{version}.tar.gz

BuildRequires:  pkg-config
BuildRequires:  readline-devel

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Patch1:     sqlite_default_journalmode.patch

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host
SQLite Encryption Extension supported.

%package devel
Summary:    Development tools for the sqlite3 embeddable SQL database engine
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files and development documentation
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .journal_mode

%build

%reconfigure --prefix=%{_prefix} \
	CFLAGS="$RPM_OPT_FLAGS " \
    --disable-dependency-tracking \
	--enable-shared=yes \
	--enable-static=no \
	--enable-threadsafe \
	--enable-icu=no

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}

%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/man

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest sqlite3.manifest
%{_bindir}/sqlite3
%{_libdir}/libsqlite*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libsqlite*.so
%{_libdir}/pkgconfig/sqlite3.pc
