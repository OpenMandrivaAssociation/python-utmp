Summary:	A python module for working with utmp
Name:		python-utmp
Version:	0.8
Release:	5
Group:		Development/Python
License:	Copyright only
Url:		http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/
Source0:	http://kassiopeia.juls.savba.sk/~garabik/software/%{name}/%{name}_%{version}.tar.gz
%py_requires -d

%description
This package provides 3 python modules to access utmp and wtmp
records.  utmpaccess is lowlevel module wrapping glibc functions,
UTMPCONST provides useful constants, and utmp is module build on top
of utmpaccess module, providing object oriented interface.

%prep
%setup -q

%build
%make -f Makefile.glibc PYTHONVER=%{py_ver} PYTHONDIR='$(DESTDIR)%{py_platsitedir}/'

%install
%makeinstall_std -f Makefile.glibc PYTHONVER=%{py_ver} PYTHONDIR='$(DESTDIR)%{py_platsitedir}/'

%files
%doc README COPYING TODO examples/*
%{py_platsitedir}/*

