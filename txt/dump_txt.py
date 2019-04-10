#!/usr/bin/env python2
#
# Copyright (C) 2019 The Event Horizon Telescope Collaboration
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import os
import ehtim as eh
import numpy as np

if len(sys.argv) == 1:
    print "usage: "+sys.argv[0]+" [input].uvfits"
    sys.exit()

in_name = sys.argv[1]
if len(sys.argv) == 2:
    out_name = os.path.splitext(in_name)[0]+'.txt'
else:
    out_name = sys.argv[2]

def save_obs_txt_stokesI(obs, fname):
    """Save the observation data in a text file. """
    outdata = obs.unpack(['time_utc', 't1', 't2', 'u', 'v', 'amp', 'phase', 'sigma'])
    head = (
        "SRC:"+obs.source+" DATE(MJD):"+str(obs.mjd)+" FREQ:"+str(round(obs.rf/1.e9,4))+"GHz\n" +
        "time(UTC)      T1     T2   U(lambda)        V(lambda)         " +
        "Iamp(Jy)    Iphase(d)   " +
        "Isigma(Jy)"
    )

    fmts = ("%011.8f  %6s %6s  %16.4f  %16.4f  %10.8f  %10.4f  %10.8f")
    np.savetxt(fname, outdata, header=head, fmt=fmts)

obs = eh.obsdata.load_uvfits(in_name, polrep='stokes')
save_obs_txt_stokesI(obs, out_name)
