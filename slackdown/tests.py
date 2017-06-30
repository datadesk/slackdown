#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests Slackdown API wrapper.
"""
import unittest
import slackdown


class SlackdownTest(unittest.TestCase):
    def test_render(self):
        txt = slackdown.render('*Bold*')
        self.assertEqual(txt, '<b>Bold</b>')
