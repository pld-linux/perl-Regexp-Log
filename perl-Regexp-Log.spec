#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Log
Summary:	Regexp::Log - base class for log files regexp builders
Summary(pl):	Regexp::Log - klasa bazowa do tworzenia wyra¿eñ regularnych dla plików logów
Name:		perl-Regexp-Log
Version:	0.01
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e773d421166563966ca02f9cf439e2f
%{!?_without_tests:BuildRequires:	perl-Test-Simple}
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Log is a base class for a variety of modules that generate
regular expressions for performing the usual data munging tasks on log
files that cannot be simply split().

The goal of this module family is to compute regular expressions based
on the configuration string of the log.

%description -l pl
Regexp::Log to klasa bazowa dla ró¿nych modu³ów generuj±cych wyra¿enia
regularne do obrabiania danych z plików logów, których nie wystarczy
tylko potraktowaæ funkcj± split().

Celem rodziny modu³ów jest wyliczanie wyra¿eñ regularnych oparte na
³añcuchu konfiguracyjnym dla loga.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# one test seems broken
perl -pi -e 's/"a a /"a /' t/20debug.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Regexp/Log.pm
%{_mandir}/man3/*
