Summary:	A python module for working with utmp
Name:		python-utmp
Version:	0.8
Release:	10
Group:		Development/Python
License:	Copyright only
Url:		http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/
Source0:	http://kassiopeia.juls.savba.sk/~garabik/software/%{name}/%{name}_%{version}.tar.gz

#Only  python2 build .Sflo
BuildRequires:  python2-devel
Requires:  python(abi) = 2.7
Provides:  python2-utmp

%description
This package provides 3 python modules to access utmp and wtmp
records.  utmpaccess is lowlevel module wrapping glibc functions,
UTMPCONST provides useful constants, and utmp is module build on top
of utmpaccess module, providing object oriented interface.

%prep
%setup -q

%build
%make -f Makefile.glibc PYTHONVER=%{py2_ver} PYTHONDIR='$(DESTDIR)%{py2_platsitedir}/'

%install
%makeinstall_std -f Makefile.glibc PYTHONVER=%{py2_ver} PYTHONDIR='$(DESTDIR)%{py2_platsitedir}/'

%files
%doc README COPYING TODO examples/*
%{py2_platsitedir}/*

