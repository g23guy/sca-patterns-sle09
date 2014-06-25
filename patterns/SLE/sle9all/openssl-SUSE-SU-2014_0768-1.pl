#!/usr/bin/perl

# Title:       OpenSSL SA Critical SUSE-SU-2014:0768-1
# Description: solves two vulnerabilities and has one errata
# Modified:    2014 Jun 25
#
##############################################################################
# Copyright (C) 2014 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################
use strict;
use warnings;
use SDP::Core;
use SDP::SUSE;

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

@PATTERN_RESULTS = (
"META_CLASS=Security",
"META_CATEGORY=SLE",
"META_COMPONENT=OpenSSL",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-06/msg00011.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'OpenSSL';
my $MAIN_PACKAGE = 'openssl';
my $SEVERITY = 'Critical';
my $TAG = 'SUSE-SU-2014:0768-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE9GA) >= 0 && SDP::SUSE::compareKernel(SLE10GA) < 0 ) {
	my %HOST_INFO = SDP::SUSE::getHostInfo();
	if ( $HOST_INFO{'architecture'} =~ m/s390/i ) {
		%PACKAGES = (
			'openssl' => '0.9.7d-15.50',
			'openssl-32bit-9-201406060130',
			'openssl-devel' => '0.9.7d-15.50',
			'openssl-devel-32bit-9-201406060130',
			'openssl-doc' => '0.9.7d-15.50',
		);
	} else {
		%PACKAGES = (
			'openssl' => '0.9.7d-15.50',
			'openssl-32bit-9-201406041231',
			'openssl-devel' => '0.9.7d-15.50',
			'openssl-devel-32bit-9-201406041231',
			'openssl-doc' => '0.9.7d-15.50',
		);
	}
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

