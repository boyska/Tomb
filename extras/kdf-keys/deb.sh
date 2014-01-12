#!/usr/bin/env bash

cd $(dirname $0)
CPPFLAGS=$(dpkg-buildflags --get CPPFLAGS)
CFLAGS=$(dpkg-buildflags --get CFLAGS)
CXXFLAGS=$(dpkg-buildflags --get CXXFLAGS)
LDFLAGS=$(dpkg-buildflags --get LDFLAGS)
export CPPFLAGS
export CFLAGS
export CXXFLAGS
export LDFLAGS
export PREFIX=/usr
make all
checkinstall -y --install=no --nodoc \
	--pkgname=tomb-kdf \
	--pkgversion=1.4 \
	--maintainer=boyska \
	--requires=libgcrypt11,libc6

