#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostForeachConan(base.BoostBaseConan):
    name = "boost_foreach"
    url = "https://github.com/bincrafters/conan-boost_foreach"
    lib_short_names = ["foreach"]
    header_only_libs = ["foreach"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_iterator",
        "boost_mpl",
        "boost_range",
        "boost_type_traits"
    ]
