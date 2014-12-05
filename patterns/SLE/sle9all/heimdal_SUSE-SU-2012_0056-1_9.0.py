#!/usr/bin/python
#
# Title:       Important Security Announcement for heimdal SUSE-SU-2012:0056-1
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
META_COMPONENT = "heimdal"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2012-01/msg00039.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'heimdal'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2012:0056-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 9):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		if "s390" in SERVER['Architecture'].lower():
			PACKAGES = {
				'heimdal': '0.6.1rc3-55.29',
				'heimdal-devel': '0.6.1rc3-55.29',
				'heimdal-devel-32bit': '9-201112301034',
				'heimdal-lib': '0.6.1rc3-55.29',
				'heimdal-lib-32bit': '9-201112301034',
				'heimdal-tools': '0.6.1rc3-55.29',
			}
		else:
			PACKAGES = {
				'heimdal': '0.6.1rc3-55.29',
				'heimdal-devel': '0.6.1rc3-55.29',
				'heimdal-devel-32bit': '9-201112301024',
				'heimdal-lib': '0.6.1rc3-55.29',
				'heimdal-lib-32bit': '9-201112301024',
				'heimdal-tools': '0.6.1rc3-55.29',
			}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

