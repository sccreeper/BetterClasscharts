#!/bin/bash

echo -------------------
echo Pulling licenses...
echo -------------------

python3 pull_licenses.py

echo -------------------
echo Building APK and deploying...
echo -------------------

buildozer android debug deploy run

echo -------------------
echo Finished
echo -------------------
