from __future__ import print_function
from __future__ import absolute_import

###############################################################################
#   volumina: volume slicing and editing library
#
#       Copyright (C) 2011-2014, the ilastik developers
#                                <team@ilastik.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the Lesser GNU General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# See the files LICENSE.lgpl2 and LICENSE.lgpl3 for full text of the
# GNU Lesser General Public License version 2.1 and 3 respectively.
# This information is also available on the ilastik web site at:
# 		   http://ilastik.org/license/
###############################################################################
import sys
import threading
import logging
import weakref
from functools import partial, wraps
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from volumina.pixelpipeline.asyncabcs import RequestABC, SourceABC, IndeterminateRequestError
import volumina
from volumina.slicingtools import is_pure_slicing, slicing2shape, is_bounded, make_bounded, index2slice, sl
from volumina.config import CONFIG
import numpy as np
from future.utils import raise_with_traceback

from .array import ArraySource, ArraySinkSource, RelabelingArraySource
from .constant import ConstantSource
from .minmax import MinMaxSource
from .halo import HaloAdjustedDataSource

try:
    from .lazyflow import LazyflowSource, LazyflowSinkSource
except ImportError:
    pass
