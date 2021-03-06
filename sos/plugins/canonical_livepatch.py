# Copyright (c) 2016 Bryan Quigley <bryan.quigley@canonical.com>

# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.plugins import Plugin, UbuntuPlugin


class CanonicaLivepatch(Plugin, UbuntuPlugin):
    """Canonical Livepatch Service
    """

    plugin_name = 'canonical_livepatch'
    profiles = ('system', 'kernel')
    commands = ('canonical-livepatch',)

    def setup(self):
        self.add_cmd_output([
            "systemctl status snap.canonical-livepatch.canonical-livepatchd",
            "canonical-livepatch status --verbose",
            "canonical-livepatch --version"
        ])

# vim: set et ts=4 sw=4 :
