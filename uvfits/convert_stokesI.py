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

import ehtim as eh

doy = {'3597':'095','3598':'096','3600':'100','3601':'101'}

path0='../sr1/postproc-hops-'

for band in ['hi','lo']:
    for expt in ['3597','3598','3600','3601']:
        pathf=path0+band+'/3.+netcal/'+expt+'/hops_'+expt+'_M87+netcal.uvfits'

        f0stokes = eh.obsdata.load_uvfits(pathf,polrep='stokes')
        for col in ['qvis','uvis','vvis','qsigma','usigma']:
            #remove non-Stokes I components but keep Stokes V errors for consistent
            #treatment of errors magnitude with Stokes / pseudo Stokes data present
            f0stokes.data[col] *= 0 # this operation is nan-preserving

        # remove record of single polarization pseudo-I construction (remove nan)
        f0stokes.data['vvis'] = 0. * f0stokes.data['vis']
        f0stokes.data['vsigma'] = 1. * f0stokes.data['sigma']

        outname='SR1_M87_2017_'+doy[expt]+'_'+band+'_hops_netcal_StokesI.uvfits'
        f0stokes.save_uvfits(outname)
