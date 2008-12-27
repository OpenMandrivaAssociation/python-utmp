Summary: A python module for working with utmp
Name: python-utmp
Version: 0.7
Release: %mkrel 9
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
%py_requires -d

%description
This package provides 3 python modules to access utmp and wtmp
records.  utmpaccess is lowlevel module wrapping glibc functions,
UTMPCONST provides useful constants, and utmp is module build on top
of utmpaccess module, providing object oriented interface.

%prep
%setup -q

%build
%make -f Makefile.glibc PYTHONVER=%pyver PYTHONDIR='$(DESTDIR)%py_platsitedir/'

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -f Makefile.glibc PYTHONVER=%pyver PYTHONDIR='$(DESTDIR)%py_platsitedir/'


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO examples/*
%py_platsitedir/*


