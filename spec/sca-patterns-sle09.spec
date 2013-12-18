#
# spec file for package scdiag (Version 1.0)
#
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

Name:         sca-patterns-sle09
Summary:      Supportconfig Analysis Patterns for SLE9
Group:        Documentation/SuSE
Distribution: SUSE Linux Enterprise
Vendor:       SUSE Support
License:      GPLv2
Autoreqprov:  on
Version:      1.1
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

%files
%defattr(-,%{patuser},%{patgrp})
%dir /var/opt/%{produser}
%dir %{patdir}
%dir %{patdir}/SLE
%dir %{patdir}/SLE/sle9all
%attr(555,%{patuser},%{patgrp}) %{patdir}/SLE/sle9all/*

%prep
%setup -q

%build
make build

%install
make install

%changelog
* Wed Dec 18 2013 jrecord@suse.com
- separated as individual RPM package
- added
  javaibm-SUSE-SU-2013_1677-1.pl sle9


