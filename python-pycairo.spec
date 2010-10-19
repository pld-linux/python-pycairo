Summary:	Python Cairo bindings
Summary(pl.UTF-8):	Dowiązania Pythona dla Cairo
Name:		python-pycairo
Version:	1.8.10
Release:	3
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/releases/py2cairo-%{version}.tar.gz
# Source0-md5:	87421a6a70304120555ba7ba238f3dc3
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.6
BuildRequires:	cairo-devel >= 1.8.10
BuildRequires:	libtool >= 2:1.4
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel
# for tests only
#BuildRequires:	python-numpy
# not release yet
#BuildRequires:	python-xpyb >= 1.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	cairo >= 1.8.10
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
Requires:	cairo-devel >= 1.8.10

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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm $RPM_BUILD_ROOT%{py_sitedir}/cairo/*.{la,py}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%dir %{py_sitedir}/cairo
%attr(755,root,root) %{py_sitedir}/cairo/_cairo.so
%{py_sitedir}/cairo/__init__.py[co]

%files devel
%defattr(644,root,root,755)
%{_includedir}/pycairo
%{_pkgconfigdir}/pycairo.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
