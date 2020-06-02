#!/usr/bin/env python

# Copyright (c) 2013 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Verifies that ARC objc settings are handled correctly.
"""

import TestGyp

import sys

if sys.platform == 'darwin':
  # set |match| to ignore build stderr output.
  test = TestGyp.TestGyp(formats=['ninja', 'make', 'xcode'],
                         match = lambda a, b: True)

  CHDIR = 'objc-arc'
  test.run_gyp('test.gyp', chdir=CHDIR)

  test.build('test.gyp', 'arc_enabled', chdir=CHDIR)
  test.build('test.gyp', 'weak_enabled', chdir=CHDIR)
  test.build('test.gyp', 'arc_disabled', chdir=CHDIR)

  test.pass_test()
