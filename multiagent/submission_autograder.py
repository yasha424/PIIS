#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from codecs import open
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

"""
CS 188 Local Submission Autograder
Written by the CS 188 Staff

==============================================================================
   _____ _              _ 
  / ____| |            | |
 | (___ | |_ ___  _ __ | |
  \___ \| __/ _ \| '_ \| |
  ____) | || (_) | |_) |_|
 |_____/ \__\___/| .__/(_)
                 | |      
                 |_|      

Modifying or tampering with this file is a violation of course policy.
If you're having trouble running the autograder, please contact the staff.
==============================================================================
"""
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))

