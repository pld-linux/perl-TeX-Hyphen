%include	/usr/lib/rpm/macros.perl
Summary:	TeX-Hyphen perl module
Summary(pl):	Modu³ perla TeX-Hyphen
Name:		perl-TeX-Hyphen
Version:	0.101
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/TeX/TeX-Hyphen-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeX-Hyphen - hyphenates words using TeX's patterns.

%description -l pl
Modu³ perla TeX-Hyphen.

%prep
%setup -q -n TeX-Hyphen-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/TeX/Hyphen
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz

%{perl_sitelib}/TeX/Hyphen.pm
%{perl_sitearch}/auto/TeX/Hyphen

%{_mandir}/man3/*
