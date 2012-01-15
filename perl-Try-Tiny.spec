#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Try
%define	pnam	Tiny
Summary:	Try::Tiny - minimal try/catch with proper localization of $@
Summary(pl.UTF-8):	Try::Tiny - minimaly try/catch z odpowiednią lokalizacją $@
Name:		perl-Try-Tiny
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DO/DOY/Try-Tiny-%{version}.tar.gz
# Source0-md5:	4d2c8ff385ac3513edf4c042dd0eacbe
URL:		http://search.cpan.org/dist/Try-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides bare bones try/catch statements that are designed
to minimize common mistakes with eval blocks, and NOTHING else.

This is unlike TryCatch which provides a nice syntax and avoids adding
another call stack layer, and supports calling return from the try
block to return from the parent subroutine. These extra features come
at a cost of a few dependencies, namely Devel::Declare and
Scope::Upper which are occasionally problematic, and the additional
catch filtering uses Moose type constraints which may not be desirable
either.

The main focus of this module is to provide simple and reliable error
handling for those having a hard time installing TryCatch, but who
still want to write correct eval blocks without 5 lines of boilerplate
each time.

%description -l pl.UTF-8
Ten moduł udostępnia proste instrukcje try/catch zaprojektowane w
celu ograniczenia popularnych błędów w blokach eval - i NIC więcej,
w przeciwieństwie do TryCatch, który udostępnia ładną składnię oraz
zapobiega dodawaniu kolejnej warstwy stosu wywołań i obsługuje powrót
z bloku try do procedury wywołującej. Te dodatkowe możliwości są
okupione kilkoma zależnościami (Devel::Declare i Scope::Upper), które
bywają problematyczne, a dodatkowe filtrowanie catch wykorzystuje
ograniczenia typu Moose, które mogą być niepożądane.

Głównym celem tego modułu jest udostępnienie prostej i wiarygodnej
obsługi błędów dla zmęczonych instalowaniem TryCatch, ale nadal
chcących pisać proste bloki eval bez każdorazowych 5 nadmiarowych
linii.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Try
%{perl_vendorlib}/Try/Tiny.pm
%{_mandir}/man3/Try::Tiny.3pm*
