%define		pname pycairo
Summary:	Python Cairo bindings
Summary:	Dowi±zania Pythona dla Cairo
Name:		python-%{pname}
Version:	0.4.0
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{pname}-%{version}.tar.gz
# Source0-md5:	5e8d7fa07b1f367b47f366811bbe4ac9
Patch0:		%{name}-ac.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	cairo-devel >= 0.4.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libsvg-cairo-devel >= 0.1.5
BuildRequires:	libtool
BuildRequires:	python >= 2.2
BuildRequires:	python-numpy-devel
BuildRequires:	python-pygtk-devel >= 1.99.16
%pyrequires_eq	python-libs
Requires:	cairo >= 0.4.0
Requires:	libsvg-cairo >= 0.1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Cairo bindings.

%description -l pl
Dowi±zania Pythona dla Cairo.

%package examples
Summary:        Example programs using Python Cairo bindings
Summary(pl):    Przyk³adowe programy w Pythonie u¿ywaj±ce Cairo
Group:          Libraries/Python
Requires:       %{name} = %{version}-%{release}

%description examples
Example programs using Python Cairo bindings.

%description -l pl examples
Przyk³adowe programy w Pythonie u¿ywaj±ce Cairo.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

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

mv $RPM_BUILD_ROOT%{py_sitescriptdir}/cairo/* $RPM_BUILD_ROOT%{py_sitedir}/cairo
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

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
