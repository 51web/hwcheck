Name: hwcheck
Version: 0.1
Release: 1%{?dist}
Summary: Scirpts for hardware info check and monitor

Group: Applications/System
License: Apache
URL: http://git.51web.net/os/hwcheck
Source0: hwcheck-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: python
Requires: srvadmin-omacore, srvadmin-omcommon, srvadmin-storage-cli, smbios-utils-bin, lm_sensors, dmidecode

%description
Provides scripts for server hardware infomation gathering and monitoring,just
support DELL server now.


%prep
%setup -q


%build
rm -f *.swp
rm -f *.pyc


%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -pm 755 hwcheck %{buildroot}%{_bindir}/hwcheck
install -pm 755 hwinfo %{buildroot}%{_bindir}/hwinfo


%post
if /usr/sbin/dmidecode | grep -iq 'kvm'; then
    /opt/dell/srvadmin/sbin/srvadmin-services.sh disable >/dev/null
else
    /opt/dell/srvadmin/sbin/srvadmin-services.sh enable >/dev/null
    /opt/dell/srvadmin/sbin/srvadmin-services.sh restart >/dev/null
    echo yes|/usr/sbin/sensors-detect >/dev/null
fi


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/hwcheck
%{_bindir}/hwinfo

%changelog
* Fri Jun 19 2015 Gaoyongwei <gaoyongwei@51web.com> - 0.1-1
- First release
