%define	pdir	TeX
%define	pnam	Hyphen
%include	/usr/lib/rpm/macros.perl
Summary:	TeX-Hyphen perl module
Summary(pl):	Modu³ perla TeX-Hyphen
Name:		perl-TeX-Hyphen
Version:	0.111
Release:	2

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeX-Hyphen - hyphenates words using TeX's patterns.

%description -l pl
Modu³ perla TeX-Hyphen.

%prep
%setup -q -n TeX-Hyphen-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/TeX/Hyphen.pm
%{_mandir}/man3/*
