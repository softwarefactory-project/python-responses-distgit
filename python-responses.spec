%global pypi_name responses
%global sum Reusable django app for collecting and visualizing network topology

# Python 3 only for Fedora for now.
%if 0%{?fedora} > 12
%global with_python3 1
%endif

# python-setuptools is needed only in EPEL 7. In Fedora is already required by python package
%if 0%{?el7}
%global needs_python_setuptools 1
%endif


Name:           python-%{pypi_name}
Version:        0.5.1
Release:        2%{?dist}
Summary:        %{sum}
License:        ASL 2.0
URL:            https://github.com/getsentry/responses
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel

BuildRequires:  python2-cookies
# python2-six is missing, see https://bugzilla.redhat.com/show_bug.cgi?id=1342037
BuildRequires:  python-six
# python2-requests is missing, https://bugzilla.redhat.com/show_bug.cgi?id=1342056
BuildRequires:  python-requests
%if 0%{?needs_python_setuptools}
BuildRequires:  python-setuptools
%endif
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-cookies
BuildRequires:  python3-requests
BuildRequires:  python3-six
%endif # if with_python3

%description
A utility library for mocking out the requests Python library.

%package -n python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-cookies
Requires:       python-requests
Requires:       python-six

%description -n python2-%{pypi_name}
A utility library for mocking out the requests Python library.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-cookies
Requires:       python3-requests
Requires:       python3-six

%description -n python3-%{pypi_name}
A utility library for mocking out the requests Python library.
%endif # if with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{__python2} setup.py build
%if 0%{?with_python3}
%py3_build
%endif # if with_python3

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%if 0%{?with_python3}
%py3_install
%endif # if with_python3

# upstream developer has not inserted tests in the current pypi release.
# Uncomment in version > 0.5.1
#%check
#%{__python2} setup.py test
#%if 0%{?with_python3}
#%{__python3} setup.py test
#%endif # if with_python3

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%endif # if with_python3

%changelog
* Thu Jun 02 2016 Germano Massullo <germano.massullo@gmail.com> - 0.5.1-2
- Fixed python packages prefix for el <= 7

* Mon Jan 25 2016 Germano Massullo <germano.massullo@gmail.com> - 0.5.1-1
- LICENSE file added in upstream update
- Commented %check section due test file missing in pypi release. See https://github.com/getsentry/responses/issues/98

* Sat Jan 23 2016 Germano Massullo <germano.massullo@gmail.com> - 0.5.0-1
- Package review submission
