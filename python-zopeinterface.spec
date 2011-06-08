%define module zopeinterface
Name:           python-%{module}
Version:        3.6.1
Release:        %mkrel 1
Url:            http://pypi.python.org/pypi/zope.interface
Summary:        Interfaces for Python
License:        ZPL 2.1
Group:          Development/Python
Source:         zope.interface-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel

%description
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package provides an implementation of object interfaces for Python.
Interfaces are a mechanism for labeling objects as conforming to a given
API or contract. So, this package can be considered as implementation of
the Design By Contract methodology support in Python.


%prep
%setup -n zope.interface-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYRIGHT.txt CHANGES.txt LICENSE.txt README.txt
%{python_sitearch}/*


