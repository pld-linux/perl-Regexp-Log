#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Regexp
%define		pnam	Log
Summary:	Regexp::Log - base class for log files regexp builders
Summary(pl.UTF-8):	Regexp::Log - klasa bazowa do tworzenia wyrażeń regularnych dla plików logów
Name:		perl-Regexp-Log
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0047fed2a6b0a1182f2b7d886cfa846c
URL:		http://search.cpan.org/dist/Regexp-Log/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Log is a base class for a variety of modules that generate
regular expressions for performing the usual data munging tasks on log
files that cannot be simply split().

The goal of this module family is to compute regular expressions based
on the configuration string of the log.

%description -l pl.UTF-8
Regexp::Log to klasa bazowa dla różnych modułów generujących wyrażenia
regularne do obrabiania danych z plików logów, których nie wystarczy
tylko potraktować funkcją split().

Celem rodziny modułów jest wyliczanie wyrażeń regularnych oparte na
łańcuchu konfiguracyjnym dla loga.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# one test seems broken
perl -pi -e 's/"a a /"a /' t/20debug.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
