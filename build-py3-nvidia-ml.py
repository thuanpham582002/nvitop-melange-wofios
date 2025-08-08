#!/bin/bash

# Build nvitop-exporter APK package using melange
# This script builds the nvitop-exporter package for x86_64 architecture

echo "Building py3-nvidia-ml-py APK package..."

# Build py3-nvidia-ml-py APK package using melange
# This script builds the py3-nvidia-ml-py package for x86_64 architecture

echo "Building py3-nvidia-ml-py APK package..."

cd /Users/noroom113/SelfProject/melange_practice
docker run --privileged \
 --rm \
 -v "$PWD":/work \
 -w /work \
 cgr.dev/chainguard/melange \
 build \
 os/py3-nvidia-ml-py.yaml \
 --pipeline-dir os/pipelines \
 -r https://packages.wolfi.dev/os \
 --arch x86_64 \
 --out-dir packages \
 --ignore-signatures