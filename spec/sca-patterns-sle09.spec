# Copyright (C) 2013,2014 SUSE LLC
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild

%define sca_common sca
%define patdirbase /usr/lib/%{sca_common}
%define patdir %{patdirbase}/patterns
%define patuser root
%define patgrp root
%define mode 544
%define category SLE

Name:         sca-patterns-sle09
Summary:      Supportconfig Analysis Patterns for SLE9
URL:          https://bitbucket.org/g23guy/sca-patterns-sle09
Group:        Documentation/SuSE
License:      GPL-2.0
Autoreqprov:  on
Version:      1.3
Release:      2
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
install -m %{mode} patterns/%{category}/sle9all/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle9all

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/sle9all
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle9all/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jan 28 2014 jrecord@suse.com
- includes pertinent patterns from sca-patterns-basic

* Thu Jan 16 2014 jrecord@suse.com
- relocated files according to FHS

* Wed Dec 20 2013 jrecord@suse.com
- separated as individual RPM package
- added
  javaibm-SUSE-SU-2013_1677-1.pl sle9


