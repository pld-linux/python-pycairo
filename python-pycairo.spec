%define		pname pycairo
Summary:	Python Cairo bindings
Summary:	Dowiązania Pythona dla Cairo
Name:		python-%{pname}
Version:	0.6.0
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{pname}-%{version}.tar.gz
# Source0-md5:	b20c825f0652d6960ab216b0ae1afe91
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	cairo-devel >= 0.6.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	libtool
BuildRequires:	python >= 2.3
BuildRequires:	python-numpy-devel
BuildRequires:	python-pygtk-devel >= 1.99.16
%pyrequires_eq	python-libs
Requires:	cairo >= 0.6.0
Requires:	libsvg-cairo >= 0.1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Cairo bindings.

%description -l pl
Dowiązania Pythona dla Cairo.

%package devel
Summary:        Development files for pycairo
Summary(pl):    Pliki programistyczne pycairo
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for pycairo.

%description -l pl devel
Pliki programistyczne pycairo.

%package examples
Summary:        Example programs using Python Cairo bindings
Summary(pl):    Przykładowe programy w Pythonie używające Cairo
Group:          Libraries/Python
Requires:       %{name} = %{version}-%{release}

%description examples
Example programs using Python Cairo bindings.

%description -l pl examples
Przykładowe programy w Pythonie używające Cairo.

%prep
%setup -q -n %{pname}-%{version}

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

cp -ar examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm $RPM_BUILD_ROOT%{py_sitedir}/cairo/*.{la,py}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS NOTES README
%dir %{py_sitedir}/cairo
%attr(755,root,root) %{py_sitedir}/cairo/*.so
%{py_sitedir}/cairo/*.py[oc]

%files devel
%defattr(644,root,root,755)
%{_includedir}/pycairo
%{_pkgconfigdir}/pycairo.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
