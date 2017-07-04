#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests Slackdown API wrapper.
"""
import unittest
import slackdown


class SlackdownTest(unittest.TestCase):
    def test_bold(self):
        txt = slackdown.render('Some *bold* text.')
        self.assertEqual(txt, '<p>Some <b>bold</b> text.</p>')

    def test_italics(self):
        txt = slackdown.render('Some _italics_ text.')
        self.assertEqual(txt, '<p>Some <i>italics</i> text.</p>')

    def test_strikethrough(self):
        txt = slackdown.render('Some ~strikethrough~ text.')
        self.assertEqual(txt, '<p>Some <s>strikethrough</s> text.</p>')

    def test_line_breaks(self):
        txt = slackdown.render('multiple\n\ntext\nlines')
        self.assertEqual(txt, '<p>multiple</p><p></p><p>text</p><p>lines</p>')

    def test_spaces(self):
        txt = slackdown.render('large     spaces    between     text')
        self.assertEqual(txt, '<p>large &nbsp &nbsp spaces &nbsp &nbspbetween &nbsp &nbsp text</p>')

    def test_single_line_code(self):
        txt = slackdown.render('Some `*code*` text.')
        self.assertEqual(txt, '<p>Some <code>*code*</code> text.</p>')

    def test_multi_line_code(self):
        txt = slackdown.render('```multiple\n*lines* of\ncode```')
        self.assertEqual(txt, '<pre>multiple<br />*lines* of<br />code</pre>')

    def test_bullet_list(self):
        txt = slackdown.render(u'\u2022 item 1\n\u2022 item 2')
        self.assertEqual(txt, '<ul class="list-container-dot"><li>item 1</li><li>item 2</li></ul>')

    def test_hyphen_list(self):
        txt = slackdown.render(u'- item 1\n- item 2')
        self.assertEqual(txt, '<ul class="list-container-dash"><li>item 1</li><li>item 2</li></ul>')

    def test_numbered_list(self):
        txt = slackdown.render(u'1. item 1\n24. item 2')
        self.assertEqual(txt, '<ol class="list-container-numbered"><li>item 1</li><li>item 2</li></ol>')

    def test_single_line_blockquote(self):
        txt = slackdown.render('&gt; Someone else said this.')
        self.assertEqual(txt, '<blockquote>Someone else said this.</blockquote>')

    def test_multi_line_blockquote(self):
        txt = slackdown.render('&gt;&gt;&gt; Someone else\nsaid this.')
        self.assertEqual(txt, '<blockquote>Someone else<br />said this.</blockquote>')

    def test_multiple_same_lists(self):
        txt = slackdown.render('- item 1\n- item 2\n\n- item 3\n- item 4')
        self.assertEqual(txt, '''\
<ul class="list-container-dash">\
<li>item 1</li>\
<li>item 2</li>\
</ul>\
<ul class="list-container-dash">\
<li>item 3</li>\
<li>item 4</li>\
</ul>\
''')

    def test_multiple_diff_lists(self):
        txt = slackdown.render('These are *two* lists.\n- item 1\n- item 2\n1. item 3\n2. item 4\nRight?')
        self.assertEqual(txt, '''\
<p>These are <b>two</b> lists.</p>\
<ul class="list-container-dash">\
<li>item 1</li>\
<li>item 2</li>\
</ul>\
<ol class="list-container-numbered">\
<li>item 3</li>\
<li>item 4</li>\
</ol>\
<p>Right?</p>\
''')

    def test_multiple_parents(self):
        txt = slackdown.render('A blockquote looks like this:\n&gt; Someone else said this.')
        self.assertEqual(txt, '<p>A blockquote looks like this:</p><blockquote>Someone else said this.</blockquote>')

    def test_all_bold(self):
        txt = slackdown.render('*All bold text*')
        self.assertEqual(txt, '<p><b>All bold text</b></p>')

    def test_bold_in_list(self):
        txt = slackdown.render(u'- *item 1*\n- item 2')
        self.assertEqual(txt, '<ul class="list-container-dash"><li><b>item 1</b></li><li>item 2</li></ul>')

    def test_bad_bold_wrapping(self):
        txt = slackdown.render('*Multiple lines\nof bold text.*')
        self.assertEqual(txt, '<p>*Multiple lines</p><p>of bold text.*</p>')

    def test_escaping(self):
        txt = slackdown.render('The \*unbolded\* text should not be *bold*.')
        self.assertEqual(txt, '<p>The \*unbolded\* text should not be <b>bold</b>.</p>')


class CustomSlackdownParserTest(unittest.TestCase):
    def test_bad_open_list(self):
        bad_txt = '<li class="list-container-bad_type"></li>'
        error_msg = 'CustomSlackdownParser:_open_list: Not a valid list type.'
        parser = slackdown.CustomSlackdownParser(bad_txt)

        with self.assertRaises(Exception) as context:
            parser.clean()

        self.assertTrue(error_msg in str(context.exception))
