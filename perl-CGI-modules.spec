%include	/usr/lib/rpm/macros.perl
Summary:	CGI-modules perl module
Summary(pl):	Modu³ perla CGI-modules
Name:		perl-CGI-modules
Version:	2.76
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-modules-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-libwww
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-modules is a set of modules for use in writing CGI scripts.

%description -l pl
CGI-modules jest zestawem modu³ów do wykorzystania przy pisaniu
skryptów CGI.

%prep
%setup -q -n CGI-modules-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man3/CGI::Carp.3pm

gzip -9nf README doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*
%{perl_sitelib}/CGI/*.pm
%{perl_sitelib}/CGI/test.pl
%{_mandir}/man3/*
