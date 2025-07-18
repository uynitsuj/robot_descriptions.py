#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Inria

"""Booster T1 description."""

from os import getenv as _getenv
from os import path as _path

from ._cache import clone_to_cache as _clone_to_cache

REPOSITORY_PATH: str = _clone_to_cache(
    "booster_gym",
    commit=_getenv("ROBOT_DESCRIPTION_COMMIT", None),
)

PACKAGE_PATH: str = _path.join(REPOSITORY_PATH, "resources", "T1")

URDF_PATH: str = _path.join(PACKAGE_PATH, "T1_serial.urdf")
