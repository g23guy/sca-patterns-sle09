#!/usr/bin/python
#
# Title:       Critical Security Announcement for Samba SUSE-SU-2012:0338-1
# Description: Security fixes for SUSE Linux Enterprise 9 SP0
# Source:      Security Announcement Parser v1.1.7
# Modified:    2014 Dec 05
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

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "Samba"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2012-03/msg00009.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Samba'
MAIN = ''
SEVERITY = 'Critical'
TAG = 'SUSE-SU-2012:0338-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 9):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		if "s390" in SERVER['Architecture'].lower():
			PACKAGES = {
				'libsmbclient': '3.0.26a-0.21',
				'libsmbclient-32bit': '9-201202240207',
				'libsmbclient-devel': '3.0.26a-0.21',
				'samba': '3.0.26a-0.21',
				'samba-32bit': '9-201202240207',
				'samba-client': '3.0.26a-0.21',
				'samba-client-32bit': '9-201202240207',
				'samba-doc': '3.0.26a-0.21',
				'samba-pdb': '3.0.26a-0.21',
				'samba-python': '3.0.26a-0.21',
				'samba-vscan': '0.3.6b-0.49',
				'samba-winbind': '3.0.26a-0.21',
				'samba-winbind-32bit': '9-201202240207',
			}
		else:
			PACKAGES = {
				'libsmbclient': '3.0.26a-0.21',
				'libsmbclient-32bit': '9-201202240204',
				'libsmbclient-devel': '3.0.26a-0.21',
				'samba': '3.0.26a-0.21',
				'samba-32bit': '9-201202240204',
				'samba-client': '3.0.26a-0.21',
				'samba-client-32bit': '9-201202240204',
				'samba-doc': '3.0.26a-0.21',
				'samba-pdb': '3.0.26a-0.21',
				'samba-python': '3.0.26a-0.21',
				'samba-vscan': '0.3.6b-0.49',
				'samba-winbind': '3.0.26a-0.21',
				'samba-winbind-32bit': '9-201202240204',
			}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

