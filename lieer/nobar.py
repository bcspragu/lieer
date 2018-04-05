#! /usr/bin/env python3
#
# Regular text output drop-in replacement for tqdm

import time
from   math import floor

class tqdm:
  def __init__ (self, leave = True, total = None, desc = '', *args, **kwargs):
    self.desc = desc
    self.args = args
    self.kwargs = kwargs

    if total is not None:
      print (desc, '(%d)' % total, '...', end = '', flush = True)
    else:
      print (desc, '...', end = '', flush = True)
    self.start = time.perf_counter ()
    self.it    = 0

  def update (self, *args):
    self.it += 1

    INTERVAL = 10

    if (self.it % INTERVAL == 0):
      print ('.', end = '', flush = True)

  def set_description (self, *args, **kwargs):
    pass

  def close (self):
    self.end = time.perf_counter ()
    print ('done:', self.it, 'its in', self.pp_duration (self.end - self.start))

  def pp_duration (self, d = None):
    dys = floor (d / (24 * 60 * 60))
    d   = d - (dys * 24 * 60 * 60)

    h = floor (d / (60 * 60))
    d = d - (h * 60 * 60)

    m = floor (d / 60)
    d = d - (m * 60)

    s = d

    o = ''
    above = False
    if dys > 0:
      o = '%dd-' % dys
      above = True

    if above or h > 0:
      o = o + '%02dh:' % h
      above = True

    if above or m > 0:
      o = o + '%02dm:' % m
      above = True

    o = o + '%06.3fs' % s

    return o

