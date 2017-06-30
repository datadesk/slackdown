#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests Slackdown API wrapper.
"""
import unittest
import slackdown


class SlackdownTest(unittest.TestCase):
    def test_bold(self):
        txt = slackdown.render('*bold*')
        self.assertEqual(txt, '<b>bold</b>')

    def test_italics(self):
        txt = slackdown.render('_italics_')
        self.assertEqual(txt, '<i>italics</i>')

    def test_strikethrough(self):
        txt = slackdown.render('~strikethrough~')
        self.assertEqual(txt, '<s>strikethrough</s>')

    def test_line_breaks(self):
        txt = slackdown.render('multiple\ntext\nlines')
        self.assertEqual(txt, 'multiple<br />text<br />lines')

    def test_spaces(self):
        txt = slackdown.render('large     spaces    between     text')
        self.assertEqual(txt, 'large &nbsp &nbsp spaces &nbsp &nbspbetween &nbsp &nbsp text')

    def test_single_line_code(self):
        txt = slackdown.render('`code`')
        self.assertEqual(txt, '<code>code</code>')

    def test_multi_line_code(self):
        txt = slackdown.render('```multiple\nlines of\ncode```')
        self.assertEqual(txt, '<pre>multiple<br />lines of<br />code</pre>')

    def test_bullet_list(self):
        txt = slackdown.render(u'\u2022 item 1\n\u2022 item 2')
        self.assertEqual(txt, '<ul><li>item 1</li><li>item 2</li></ul>')

    def test_hyphen_list(self):
        txt = slackdown.render(u'- item 1\n- item 2')
        self.assertEqual(txt, '<ul><li>item 1</li><li>item 2</li></ul>')

    def test_numbered_list(self):
        txt = slackdown.render(u'1. item 1\n24. item 2')
        self.assertEqual(txt, '<ol><li>item 1</li><li>item 2</li></ol>')

    def test_single_line_blockquote(self):
        txt = slackdown.render('&gt; Someone else said this.')
        self.assertEqual(txt, '<blockquote>Someone else said this.</blockquote>')

    def test_multi_line_blockquote(self):
        txt = slackdown.render('&gt;&gt;&gt; Someone else\nsaid this.')
        self.assertEqual(txt, '<blockquote>Someone else<br />said this.</blockquote>')
