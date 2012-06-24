#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	TeX
%define	pnam	Hyphen
Summary:	TeX::Hyphen Perl module
Summary(cs):	Modul TeX::Hyphen pro Perl
Summary(da):	Perlmodul TeX::Hyphen
Summary(de):	TeX::Hyphen Perl Modul
Summary(es):	M�dulo de Perl TeX::Hyphen
Summary(fr):	Module Perl TeX::Hyphen
Summary(it):	Modulo di Perl TeX::Hyphen
Summary(ja):	TeX::Hyphen Perl �⥸�塼��
Summary(ko):	TeX::Hyphen �� ����
Summary(nb):	Perlmodul TeX::Hyphen
Summary(pl):	Modu� Perla TeX::Hyphen
Summary(pt):	M�dulo de Perl TeX::Hyphen
Summary(pt_BR):	M�dulo Perl TeX::Hyphen
Summary(ru):	������ ��� Perl TeX::Hyphen
Summary(sv):	TeX::Hyphen Perlmodul
Summary(uk):	������ ��� Perl TeX::Hyphen
Summary(zh_CN):	TeX::Hyphen Perl ģ��
Name:		perl-TeX-Hyphen
Version:	0.140
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ee75a22525461e72ceab8e82377d617
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeX::Hyphen - hyphenates words using TeX's patterns.

%description -l pl
Modu� perla TeX::Hyphen - przenosz�cy s�owa przy u�yciu wzorc�w z
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
