Summary:	Polish dictionary for aspell
Summary(pl):	Polski s³ownik dla aspella
Name:		aspell-pl
Version:	0.51
%define	subv	0
Release:	1
Epoch:		1
License:	GPL (unknown)
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/pl/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	5435be1c9c39326a02e2798d8b4d257b
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
Obsoletes:	aspell-pl-alt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish dictionary (i.e. word list) for aspell.

%description -l pl
Polski s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*
