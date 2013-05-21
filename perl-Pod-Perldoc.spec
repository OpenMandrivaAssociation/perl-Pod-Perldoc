%define	modname	Pod-Perldoc
%define modver	3.17

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Tk\\)|perl\\(Tk::Pod\\)'
%else
%define _requires_exceptions perl(Tk)\\|perl(Tk::Pod)
%endif

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	2

Summary:	Customized option parser for Pod::Perldoc
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{modname}-%{modver}.tar.gz

BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
_perldoc_ looks up a piece of documentation in .pod format that is embedded
in the perl installation tree or in a perl script, and displays it via
'pod2man | nroff -man | $PAGER'. (In addition, if running under HP-UX, 'col
-x' will be used.) This is primarily used for the documentation for the
perl library modules.

Your system may also have man pages installed for those modules, in which
case you can probably just use the man(1) command.

If you are looking for a table of contents to the Perl library modules
documentation, see the the perltoc manpage page.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/perldoc

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.170.0-1
- cleanups
- new version

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.150.0-5mdv2012.0
+ Revision: 765598
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.150.0-4
+ Revision: 764126
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 3.150.0-3
+ Revision: 657827
- rebuild for updated spec-helper

* Mon Jan 03 2011 Jérôme Quelin <jquelin@mandriva.org> 3.150.0-2mdv2011.0
+ Revision: 628031
- using meta.yml for prereqs

* Mon Dec 07 2009 Jérôme Quelin <jquelin@mandriva.org> 3.150.0-1mdv2011.0
+ Revision: 474332
- import perl-Pod-Perldoc

* Sun Dec 06 2009 cpan2dist 3.15-1mdv
- initial mdv release, generated with cpan2dist
