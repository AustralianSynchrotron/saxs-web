Summary: SAXS Deployment Apache
Name: saxs-deployment-apache
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
Requires: httpd
Requires: mod_wsgi
Requires: mod_ssl
Requires: django
Requires: numpy
Requires: python-matplotlib
Requires: libjpeg-devel
Requires(post): expect

%description
SAXS Deployment Apache

%prep
%setup

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mv %{buildroot}/usr/share/saxs/deployment/apache/manage.py %{buildroot}/usr/share/saxs/deployment/apache/manage
sed -i 's/manage.py/manage/' INSTALLED_FILES
chmod +x %{buildroot}/usr/share/saxs/deployment/apache/manage

%post
sed "s/\(DATABASE_PASSWORD: *\)secret/\1$(mkpasswd -s 0 | tr '/' 'x')/" \
	-i %{_sysconfdir}/saxs/saxs-deployment-apache.ini

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Fri Aug 24 2012  Joanna H. Huang <Joanna.HuiTzu.Huang@gmail.com> - 0.0.1-1
- Initial package 

