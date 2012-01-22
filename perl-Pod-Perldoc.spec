%define upstream_name    Pod-Perldoc
%define upstream_version 3.15

%define _requires_exceptions perl(Tk)\\|perl(Tk::Pod)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    Customized option parser for Pod::Perldoc
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Symbol)
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/perldoc
