#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define		module	pycairo
Summary:	Python 2 Cairo bindings
Summary(pl.UTF-8):	Dowiązania Pythona 2 dla Cairo
Name:		python-%{module}
Version:	1.16.3
Release:	5
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries/Python
Source0:	https://github.com/pygobject/pycairo/releases/download/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	d2a115037ccd128219f43d5ed3df7926
Patch0:		python3.8.patch
URL:		http://cairographics.org/
BuildRequires:	cairo-devel >= 1.13.1
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-devel >= 1:2.7
# python2 only for now
BuildRequires:	python-xpyb-devel >= 1.3
%if %{with tests}
BuildRequires:	python-hypothesis
BuildRequires:	python-numpy
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-devel >= 1:3.3
%if %{with tests}
BuildRequires:	python3-hypothesis
BuildRequires:	python3-numpy
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-Sphinx
BuildRequires:	python-sphinx_rtd_theme
%endif
Requires:	python-libs >= 1:2.7
Requires:	cairo >= 1.13.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 Cairo bindings.

%description -l pl.UTF-8
Dowiązania Pythona 2 dla Cairo.

%package devel
Summary:	Development files for Python 2 pycairo
Summary(pl.UTF-8):	Pliki programistyczne pycairo dla Pythona 2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.13.1
Requires:	python-devel >= 1:2.7

%description devel
Development files for Python 2 pycairo.

%description devel -l pl.UTF-8
Pliki programistyczne pycairo dla Pythona 2.

%package -n python3-%{module}
Summary:	Python 3 Cairo bindings
Summary(pl.UTF-8):	Dowiązania Pythona 3 dla Cairo
Group:		Libraries/Python
Requires:	cairo >= 1.13.1
Requires:	python3-libs >= 1:3.3

%description -n python3-%{module}
Python 3 Cairo bindings.

%description -n python3-%{module} -l pl.UTF-8
Dowiązania Pythona 3 dla Cairo.

%package -n python3-%{module}-devel
Summary:	Development files for Python 3 pycairo
Summary(pl.UTF-8):	Pliki programistyczne pycairo dla Pythona 3
Group:		Development/Libraries
Requires:	cairo-devel >= 1.13.1
Requires:	python3-%{module} = %{version}-%{release}
Requires:	python3-devel >= 1:3.3

%description -n python3-%{module}-devel
Development files for Python 3 pycairo.

%description -n python3-%{module}-devel -l pl.UTF-8
Pliki programistyczne pycairo dla Pythona 3.

%package apidocs
Summary:	API documentation for Python Cairo bindings
Summary(pl.UTF-8):	Dokumentacja API dla wiązań Pythona do Cairo
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python Cairo bindings.

%description apidocs -l pl.UTF-8
Dokumentacja API dla wiązań Pythona do Cairo.

%package examples
Summary:	Example programs using Python Cairo bindings
Summary(pl.UTF-8):	Przykładowe programy w Pythonie używające Cairo
Group:		Libraries/Python
Obsoletes:	python3-pycairo-devel
BuildArch:	noarch

%description examples
Example programs using Python Cairo bindings.

%description examples -l pl.UTF-8
Przykładowe programy w Pythonie używające Cairo.

%prep
%setup -q -n pycairo-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test} \
	--enable-xpyb
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C docs
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.rst
%dir %{py_sitedir}/cairo
%attr(755,root,root) %{py_sitedir}/cairo/_cairo.so
%{py_sitedir}/cairo/__init__.py[co]
%{py_sitedir}/cairo/__init__.pyi
%{py_sitedir}/cairo/include
%{py_sitedir}/pycairo-%{version}-py*.egg-info

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/pycairo.h
%{_pkgconfigdir}/pycairo.pc
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc COPYING NEWS README.rst
%dir %{py3_sitedir}/cairo
%attr(755,root,root) %{py3_sitedir}/cairo/_cairo.cpython-*.so
%{py3_sitedir}/cairo/__init__.py
%{py3_sitedir}/cairo/__init__.pyi
%{py3_sitedir}/cairo/__pycache__
%{py3_sitedir}/cairo/include
%{py3_sitedir}/pycairo-%{version}-py*.egg-info

%files -n python3-%{module}-devel
%defattr(644,root,root,755)
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/py3cairo.h
%{_pkgconfigdir}/py3cairo.pc
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/{_images,_static,reference,*.html,*.js}
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
