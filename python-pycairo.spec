%define		module	pycairo
Summary:	Python Cairo bindings
Summary(pl.UTF-8):	Dowiązania Pythona dla Cairo
Name:		python-%{module}
Version:	1.16.3
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	https://github.com/pygobject/pycairo/releases/download/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	d2a115037ccd128219f43d5ed3df7926
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.6
BuildRequires:	cairo-devel >= 1.13.1
BuildRequires:	libtool >= 2:1.4
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel
# for tests only
#BuildRequires:	python-numpy
BuildRequires:	python-xpyb-devel >= 1.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	cairo >= 1.13.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Cairo bindings.

%description -l pl.UTF-8
Dowiązania Pythona dla Cairo.

%package devel
Summary:	Development files for pycairo
Summary(pl.UTF-8):	Pliki programistyczne pycairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.13.1

%description devel
Development files for pycairo.

%description devel -l pl.UTF-8
Pliki programistyczne pycairo.

%package examples
Summary:	Example programs using Python Cairo bindings
Summary(pl.UTF-8):	Przykładowe programy w Pythonie używające Cairo
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Example programs using Python Cairo bindings.

%description examples -l pl.UTF-8
Przykładowe programy w Pythonie używające Cairo.

%prep
%setup -q -n pycairo-%{version}

%ifarch x32
%{__sed} -i -e 's/lib64/libx32/g' setup.py
%endif

%build
%py_build --enable-xpyb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%py_install

cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/cairo/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.rst
%dir %{py_sitedir}/cairo
%attr(755,root,root) %{py_sitedir}/cairo/_cairo.so
%{py_sitedir}/cairo/__init__.py[coi]
%{py_sitedir}/cairo/include
%{py_sitedir}/pycairo-*-py2.7.egg-info

%files devel
%defattr(644,root,root,755)
%{_includedir}/pycairo
%{_pkgconfigdir}/pycairo.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
