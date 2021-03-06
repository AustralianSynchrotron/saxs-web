Summary: SAXS Application - Data Analysis
Name: saxs-app-analysis
Version: 0.0.1
Release: 1%{?dist}
Source0: %{name}-%{version}.tar.gz
License: Apache license v2.0
Group: Web Application
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
Vendor: Joanna H. Huang <Joanna.HuiTzu.Huang@gmail.com>
Url: https://github.com/AustralianSynchrotron
Requires: saxs-library-js
Requires: saxs-model-analysis
Requires: numpy
Requires: python-matplotlib
Requires: libjpeg-devel

%description
SAXS Application - Data Analysis

%prep
%setup

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Fri Aug 24 2012  Joanna H. Huang <Joanna.HuiTzu.Huang@gmail.com> - 0.0.1-1
- Initial package 

