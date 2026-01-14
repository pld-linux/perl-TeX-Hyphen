#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	TeX
%define		pnam	Hyphen
Summary:	TeX::Hyphen Perl module
Summary(cs.UTF-8):	Modul TeX::Hyphen pro Perl
Summary(da.UTF-8):	Perlmodul TeX::Hyphen
Summary(de.UTF-8):	TeX::Hyphen Perl Modul
Summary(es.UTF-8):	Módulo de Perl TeX::Hyphen
Summary(fr.UTF-8):	Module Perl TeX::Hyphen
Summary(it.UTF-8):	Modulo di Perl TeX::Hyphen
Summary(ja.UTF-8):	TeX::Hyphen Perl モジュール
Summary(ko.UTF-8):	TeX::Hyphen 펄 모줄
Summary(nb.UTF-8):	Perlmodul TeX::Hyphen
Summary(pl.UTF-8):	Moduł Perla TeX::Hyphen
Summary(pt.UTF-8):	Módulo de Perl TeX::Hyphen
Summary(pt_BR.UTF-8):	Módulo Perl TeX::Hyphen
Summary(ru.UTF-8):	Модуль для Perl TeX::Hyphen
Summary(sv.UTF-8):	TeX::Hyphen Perlmodul
Summary(uk.UTF-8):	Модуль для Perl TeX::Hyphen
Summary(zh_CN.UTF-8):	TeX::Hyphen Perl 模块
Name:		perl-TeX-Hyphen
Version:	0.140
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ee75a22525461e72ceab8e82377d617
URL:		http://search.cpan.org/dist/TeX-Hyphen/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeX::Hyphen - hyphenates words using TeX's patterns.

%description -l pl.UTF-8
Moduł perla TeX::Hyphen - przenoszący słowa przy użyciu wzorców z
TeXa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorlib}/TeX/Hyphen.pm
%{perl_vendorlib}/TeX/Hyphen
%{_mandir}/man3/*
