%define		pname pycairo
Summary:	Python Cairo bindings
Summary:	Dowi±zania Pythona dla Cairo
Name:		python-%{pname}
Version:	1.2.0
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/releases/%{pname}-%{version}.tar.gz
# Source0-md5:	ab531e02fda56a9d6b2b65153fda65f6
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	libtool
BuildRequires:	python >= 1:2.3
BuildRequires:	python-numpy-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	cairo >= 1.2.0
Requires:	libsvg-cairo >= 0.1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Cairo bindings.

%description -l pl
Dowi±zania Pythona dla Cairo.

%package devel
Summary:	Development files for pycairo
Summary(pl):	Pliki programistyczne pycairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for pycairo.

%description devel -l pl
Pliki programistyczne pycairo.

%package examples
Summary:	Example programs using Python Cairo bindings
Summary(pl):	Przyk³adowe programy w Pythonie u¿ywaj±ce Cairo
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Example programs using Python Cairo bindings.

%description examples -l pl
Przyk³adowe programy w Pythonie u¿ywaj±ce Cairo.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-pygtk
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
