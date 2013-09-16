%define	modname	Pod-Perldoc
%define modver	3.17

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Tk\\)|perl\\(Tk::Pod\\)'
%else
%define _requires_exceptions perl(Tk)\\|perl(Tk::Pod)
%endif

Summary:	Customized option parser for Pod::Perldoc
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_bindir}/perldoc
%{perl_vendorlib}/*
%{_mandir}/man3/*

