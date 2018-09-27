#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:11:57 2018

@author: ryan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:52:09 2018

@author: ryan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===========================================
# hardware.py
#
# Getting hardware information in PyQuil.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-24-18
# ===========================================

from pyquil.quil import Program
import pyquil.gates as gates
from pyquil import api

devices = api.get_devices(as_dict=True)
acorn = devices['19Q-Acorn']

