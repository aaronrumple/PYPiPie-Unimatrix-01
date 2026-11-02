# -*- coding: utf-8 -*-
# Unimatrix 01 - runs enabled mappings (sync trigger).
# Must stay silent: any problem is written to %APPDATA%\pyRevit\Unimatrix01\push.log
from pypipie.hookrunner import run_hook

run_hook("sync")
