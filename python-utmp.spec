Summary: A python module for working with utmp
Name: python-utmp
Version: 0.8
Release: 3
URL: http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/
Source0: http://kassiopeia.juls.savba.sk/~garabik/software/%{name}/%{name}_%{version}.tar.gz
License: Copyright only
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
%make -f Makefile.glibc PYTHONVER=%{py_ver} PYTHONDIR='$(DESTDIR)%{py_platsitedir}/'

%install
%makeinstall_std -f Makefile.glibc PYTHONVER=%{py_ver} PYTHONDIR='$(DESTDIR)%{py_platsitedir}/'


%files
%doc README COPYING TODO examples/*
%{py_platsitedir}/*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8-2mdv2011.0
+ Revision: 668049
- mass rebuild

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 0.8-1mdv2011.0
+ Revision: 484983
- Update to new version 0.8
- Use Fedora license tag, package COPYING file because it's non-standard

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 0.7-9mdv2009.1
+ Revision: 319834
- rebuild for new python

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7-8mdv2009.0
+ Revision: 225164
- rebuild
- fix spacing at top of description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.7-7mdv2008.1
+ Revision: 126245
- kill re-definition of %%buildroot on Pixel's request


* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.7-7mdv2007.0
+ Revision: 96565
- Rebuild against new python

  + Michael Scherer <misc@mandriva.org>
    - Import python-utmp

* Fri May 05 2006 Stefan van der Eijk <stefan@eijk.nu> 0.7-6mdk
- rebuild for sparc

* Tue Jun 14 2005 Frederic Lepied <flepied@mandriva.com> 0.7-5mdk
- fix requires

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.7-4mdk
- Rebuild for new python

