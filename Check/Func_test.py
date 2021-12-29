# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:52:23 2021

@author: sodiyqun
"""

import unittest
from Checkfunc import kattasini_top

class kattaTest(unittest.TestCase):
    def test_kattasinitop(self):
        self.assertEqual(kattasini_top(5, 10, 7), 10)
        self.assertEqual(kattasini_top(5, 10, 10), 10)
        self.assertEqual(kattasini_top(10, 10, 10), 10)
        self.assertEqual(kattasini_top(10, 15, 10), 15)
        
unittest.main()