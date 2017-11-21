#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Simula Research Laboratory.
# Distributed under the terms of the Modified BSD License.

import os

import pytest


@pytest.fixture()
def needs_altsep():
    if os.sep == os.altsep:
        pytest.skip('test needs alternative path separator')


@pytest.fixture()
def needs_no_altsep():
    if os.sep != os.altsep:
        pytest.skip('test needs alternative path separator')
