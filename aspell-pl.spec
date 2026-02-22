Summary:	Polish dictionary for aspell
Summary(pl.UTF-8):	Polski słownik dla aspella
Name:		aspell-pl
Version:	6.0_20061121
%define	subv	0
Release:	3
Epoch:		1
License:	GPL (unknown)
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/pl/aspell6-pl-%{version}-%{subv}.tar.bz2
# Source0-md5:	3139a69a1bd9ccb1d853d30aa024fc2b
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
Conflicts:	aspell-pl-alt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Polski słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-pl-%{version}-%{subv}

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
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
