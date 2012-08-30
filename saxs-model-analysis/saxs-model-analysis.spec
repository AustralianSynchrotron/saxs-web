Summary: SAXS Data Models - Analysis
Name: saxs-model-analysis
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

%description
SAXS Data Models - Analysis

%prep
%setup

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p  %{buildroot}/var/log/saxs/
mkdir -p  %{buildroot}/etc/saxs/
mkdir -p  %{buildroot}/var/lib/saxs/
#chown -R apache.apache %{buildroot}/var/lib/saxs/

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
/var/log/saxs/
/etc/saxs/

%changelog
* Fri Aug 24 2012  Joanna H. Huang <Joanna.HuiTzu.Huang@gmail.com> - 0.0.1-1
- Initial package 

