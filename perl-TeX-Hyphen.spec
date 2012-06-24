%include	/usr/lib/rpm/macros.perl
%define	pdir	TeX
%define	pnam	Hyphen
Summary:	TeX::Hyphen perl module
Summary(pl):	Modu� perla TeX::Hyphen
Name:		perl-TeX-Hyphen
Version:	0.121
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeX::Hyphen - hyphenates words using TeX's patterns.

%description -l pl
Modu� perla TeX::Hyphen - przenosz�cy s�owa przy u�yciu wzorc�w z
TeX-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/TeX/Hyphen.pm
%{perl_sitelib}/TeX/Hyphen
%{_mandir}/man3/*
