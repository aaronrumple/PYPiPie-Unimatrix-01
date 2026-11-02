# -*- coding: utf-8 -*-
# Unimatrix 01 - runs enabled mappings (save trigger).
# Must stay silent: any problem is written to %APPDATA%\pyRevit\Unimatrix01\push.log
from pypipie.hookrunner import run_hook

run_hook("save")
