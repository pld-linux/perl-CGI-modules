%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	modules
Summary:	A set of modules for use in writing CGI scripts
Summary(pl.UTF-8):	Zestaw modułów do wykorzystania przy pisaniu skryptów CGI
Name:		perl-CGI-modules
Version:	2.76
Release:	13
# same as perl (Artistic for Carp.pm)
License:	GPL v1+ (except Carp.pm) or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	be3a6dff87ae14bbf54b60005ceb5bb3
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of modules for use in writing CGI scripts.

%description -l pl.UTF-8
Ten pakiet zawiera zestaw modułów do wykorzystania przy pisaniu skryptów
CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
mv CGI/test.pl test.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man3/CGI::Carp.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/CGI/[!C]*.pm
%{_mandir}/man3/*
