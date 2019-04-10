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
import csv
import itertools

if len(sys.argv) == 1:
    print "usage: "+sys.argv[0]+" [input].txt"
    sys.exit()

in_name  = sys.argv[1]
if len(sys.argv) == 2:
    out_name = os.path.splitext(in_name)[0]+'.csv'
else:
    out_name = sys.argv[2]

with open(in_name, 'r') as in_file:
    lines = in_file.read().splitlines()
    stripped = [line.replace("# ","#").split() for line in lines]
    grouped = itertools.izip(*[stripped]*1)
    with open(out_name, 'w') as out_file:
        writer = csv.writer(out_file)
        for group in grouped:
            writer.writerows(group)
