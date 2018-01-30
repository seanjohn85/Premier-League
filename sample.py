#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 17:37:11 2018

@author: johnkenny
"""

import json 

class TestClass:
    #sample varible
    string = "I am a test"

    def testFunc(self, num):
        if num > 10:
            return "greater than 10"
        else:
            return "less than 10"
    
test = TestClass()
test.s = "new Test"
print(test.s)
print(test.testFunc(1))
