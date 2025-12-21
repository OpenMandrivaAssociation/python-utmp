Summary:        A python module for working with utmp
Name:           python-utmp
Version:        0.9
Release:        2
Group:          Development/Python
License:        Copyright only
Url:            https://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/
Source0:        http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/python-utmp_%{version}.orig.tar.gz
BuildRequires:	make
BuildRequires:  python3-devel

%description
This package provides 3 python modules to access utmp and wtmp
records.  utmpaccess is lowlevel module wrapping glibc functions,
UTMPCONST provides useful constants, and utmp is module build on top
of utmpaccess module, providing object oriented interface.

%prep
%autosetup -p1

%build
%make -f Makefile.glibc PYTHONVER=%{py3_ver} PYTHONDIR='$(DESTDIR)%{py3_platsitedir}/'

%install
%makeinstall_std -f Makefile.glibc PYTHONVER=%{py_ver} PYTHONDIR='$(DESTDIR)%{py3_platsitedir}/'

%files
%doc README COPYING TODO examples/*
%{py3_platsitedir}/*
