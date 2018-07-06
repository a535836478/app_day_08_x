#!/usr/bin/env python      # -*- coding: utf-8 -*-
import pytest
import allure

class Test_001:

    @allure.step(title='测试步骤001')
    def test_001_1(self):

        assert 0

    @allure.step(title='测试步骤002')
    def test_001_2(self):
        assert 1