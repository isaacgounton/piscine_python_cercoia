#!/usr/bin/env bash

pip --version
pip install -t local_lib --upgrade --force-reinstall --log file.log path.py
# pip install -t local_lib --upgrade --force-reinstall --log file.log git+https://github.com/jaraco/path.git
if [ -d local_lib ] && [ -e 'local_lib/path.py' ]
then
    python my_program.py
fi