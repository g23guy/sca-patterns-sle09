# Copyright (C) 2013 SUSE LLC
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild

%define produser sca
%define prodgrp sdp
%define patuser root
%define patgrp root
%define patdir /var/opt/%{produser}/patterns
%define category SLE

Name:         sca-patterns-sle09
Summary:      Supportconfig Analysis Patterns for SLE9
Group:        Documentation/SuSE
Distribution: SUSE Linux Enterprise
Vendor:       SUSE Support
License:      GPLv2
Autoreqprov:  on
Version:      1.2
Release:      1
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch
Requires:     sca-patterns-base
%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of SLES/SLED 9

Authors:
--------
    Jason Record <jrecord@suse.com>

%prep
%setup -q

%build

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle9all
install -m 544 patterns/%{category}/sle9all/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle9all

%files
%defattr(-,%{patuser},%{patgrp})
%dir /var/opt/%{produser}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/sle9all
%attr(555,%{patuser},%{patgrp}) %{patdir}/%{category}/sle9all/*


%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Dec 20 2013 jrecord@suse.com
- separated as individual RPM package
- added
  javaibm-SUSE-SU-2013_1677-1.pl sle9


