%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	modules
Summary:	A set of modules for use in writing CGI scripts
Summary(pl):	Zestaw modu��w do wykorzystania przy pisaniu skrypt�w CGI
Name:		perl-CGI-modules
Version:	2.76
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
Requires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of modules for use in writing CGI scripts.

%description -l pl
Ten pakiet zawiera zestaw modu��w do wykorzystania przy pisaniu skrypt�w
CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man3/CGI::Carp.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/CGI/*.pm
%{perl_sitelib}/CGI/test.pl
%{_mandir}/man3/*
