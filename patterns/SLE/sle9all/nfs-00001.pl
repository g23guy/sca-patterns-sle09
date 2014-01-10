#!/usr/bin/perl

# Title:       Check for nfs configuration that creates problems copying files > 2GB
# Description: This pattern checks the /etc/fstab to make sure that nfs volume entries have a tcp or nfsvers=3 following them for options.  If one of these options is not present it can cause a problem where file copies of over 2GB will fail.
# Modified:    2013 Jun 27

##############################################################################
#  Copyright (C) 2013,2012 SUSE LLC
##############################################################################
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 2 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

#  Authors/Contributors:
#   Jim Petersen (jpetersen@novell.com)

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
	PROPERTY_NAME_CLASS."=SLE",
	PROPERTY_NAME_CATEGORY."=Filesystem",
	PROPERTY_NAME_COMPONENT."=NFS",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7000362"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub check_nfs_filesize_limit {
SDP::Core::printDebug('>', 'Check for conditions that cause the error ERROR: "File size limit exceeded" while copying a file greater than 2 GB to an NFS share.');
    use constant HEADER_LINES   => 0;
    my $RCODE                    = 0;
    my $FILE_OPEN                = 'fs-diskio.txt';
    my $SECTION1                 = '/bin/mount';
    my $SECTION2                 = '/etc/fstab';
    my @CONTENT                  = ();
    my @LINE_CONTENT             = ();
    my $LINE                     = 0;
    my $FSTAB_RESULT             = 0;
    my $MOUNT_RESULT             = 0;
    my $NFS_EXISTS               = 0;

    if ( SDP::Core::getSection($FILE_OPEN, $SECTION1, \@CONTENT) ) {
        foreach $_ (@CONTENT) {
            next if ( $LINE++ < HEADER_LINES ); # Skip header lines
            next if ( /^\s*$/ );                   # Skip blank lines

            if ( /^.+\s(nfs)\s.*$/ ) {
                $NFS_EXISTS = '1';
            }

            if ( /^.+\s(nfs)\s.*$/ && !/nfsvers\s?=\s?3|tcp/ ) {
                SDP::Core::printDebug("LINE $LINE", $_);
                @LINE_CONTENT = split(/\s+/, $_);
                $MOUNT_RESULT++;
            }
        }
    } else {
       SDP::Core::updateStatus(STATUS_ERROR, "Cannot find \"$SECTION1\" section in $FILE_OPEN");
    }

    @CONTENT = ();
    @LINE_CONTENT = ();
    $LINE = 0;

    if ( SDP::Core::getSection($FILE_OPEN, $SECTION2, \@CONTENT) ) {
        foreach $_ (@CONTENT) {
            next if ( $LINE++ < HEADER_LINES ); # Skip header lines
            next if ( /^\s*$/ );                   # Skip blank lines

            if ( /^.+\s(nfs)\s.*$/ ) {
                $NFS_EXISTS = '1';
            }

            if ( /^.+\s(nfs)\s.*$/ && !/nfsvers\s?=\s?3|tcp/ ) {
                SDP::Core::printDebug("LINE $LINE", $_);
                @LINE_CONTENT = split(/\s+/, $_);
                $FSTAB_RESULT++;
            }
        }
    } else {
       SDP::Core::updateStatus(STATUS_ERROR, "Cannot find \"$SECTION2\" section in $FILE_OPEN");
    }

    $RCODE = $MOUNT_RESULT + $FSTAB_RESULT;

    if ( $NFS_EXISTS ) {
        if ( $MOUNT_RESULT > '0' ) {
          SDP::Core::updateStatus(STATUS_CRITICAL, "The /etc/mount file shows an nfs volume mounted without the tcp or nfsvers options.");
          SDP::Core::printDebug("<", "CHANGING STATUS BECAUSE NFS VOL MOUNTED W/O RIGHT OPTS");
        } elsif ($FSTAB_RESULT > '0') {
          SDP::Core::updateStatus(STATUS_WARNING, "The /etc/fstab file shows an nfs volume configured without the tcp or nfsvers options.");
          SDP::Core::printDebug("<", "CHANGING STATUS BECAUSE NFS VOL CONFIG W/O RIGHT OPTS");
        } else {
          SDP::Core::updateStatus(STATUS_ERROR, "The /etc/mount and /etc/fstab files show that all nfs volumes correctly configured.");
        }
    } else {
        updateStatus(STATUS_ERROR, "No NFS volumes found");
    }

    SDP::Core::printDebug("< Returns: $RCODE", 'check_nfs_filesize_limit');
    return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
    check_nfs_filesize_limit();
SDP::Core::printPatternResults();

exit;


