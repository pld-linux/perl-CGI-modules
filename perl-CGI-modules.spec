%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	CGI-modules perl module
Summary(pl):	Modu³ perla CGI-modules
Name:		perl-CGI-modules
Version:	2.76
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-modules-%{version}.tar.gz
Patch:		perl-CGI-modules-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-libwww
BuildRoot:	/tmp/%{name}-%{version}-root

%description
CGI-modules is a set of modules for use in writing CGI scripts.

%description -l pl
CGI-modules jest zestawem modu³ów do wykorzystania przy pisaniu skryptów CGI.

%prep
%setup -q -n CGI-modules-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz doc/*

%{perl_sitelib}/CGI/*.pm
%{perl_sitelib}/CGI/test.pl
%{perl_sitearch}/auto/CGI/.packlist

%{_mandir}/man3/*
