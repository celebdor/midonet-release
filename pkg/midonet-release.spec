Name:           midonet-release
Version:        2015.01
Release:        1
Summary:        Repositories for MidoNet networking
Group:          System Environment/Base
License:        ASL 2.0

# This is a EPEL maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
URL:            http://repo.midonet.org/yum
Source0:        http://repo.midonet.org/RPM-GPG-KEY-midokura
Source1:        datastax.repo
Source2:        midonet-misc.repo
Source3:        midonet-openstack-integration.repo
Source4:        midonet.repo
# MidoNet default preset policy
Source5:        80-midonet.preset

BuildArch:     noarch
Requires:      epel-release >= 7
Requires:      redhat-release >= 7

%description
This package contains the Midonet repository and repositories for its
dependencies, the MidoNet GPG key as well as presets for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

# Placing the GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-midokura

# Placing the various repo files
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 -D %{SOURCE5} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/80-midonet.preset

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*
%{_prefix}/lib/systemd/system-preset/80-midonet.preset

%changelog
* Mon Feb 9 2015 Antoni Segura Puimedon <toni@midokura.com> - 2015.01-1
- initial MidoNet release build.

