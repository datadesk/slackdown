# slackdown

A simple [Slack message text formatting](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages) to HTML code converter.

[![Build Status](https://travis-ci.org/datadesk/slackdown.png?branch=master)](https://travis-ci.org/datadesk/slackdown)
[![PyPI version](https://badge.fury.io/py/slackdown.png)](http://badge.fury.io/py/slackdown)
[![Coverage Status](https://coveralls.io/repos/datadesk/slackdown/badge.png?branch=master)](https://coveralls.io/r/datadesk/slackdown?branch=master)

* Issues: [github.com/datadesk/slackdown/issues](https://github.com/datadesk/slackdown/issues)
* Packaging: [pypi.python.org/pypi/slackdown](https://pypi.python.org/pypi/slackdown)
* Testing: [travis-ci.org/datadesk/slackdown](https://travis-ci.org/datadesk/slackdown)
* Coverage: [coveralls.io/r/datadesk/slackdown](https://coveralls.io/r/datadesk/slackdown)

### Installation

```python
pip install slackdown
```

### Basic usage

Import the library.

```python
import slackdown
```

Convert a Slack message to HTML using the render function.

```python
>>> slackdown.render('*bold*')
'<p><b>bold</b></p>'
```

```python
>>> slackdown.render('_italics_')
'<p><i>italics</i></p>'
```

All inline elements will be rendered inside `<p>` tags unless they are already wrapped in another block element like `<pre>`,`<blockquote>`,`<ul>`, or `<ol>` tags.

### Features
slackdown includes multiple features of Slack messages including all the one's highlighted in Slack's [message formatting documentation](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages).

#### [Emphasis](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages#emphasis)
- Text surrounded by \_underscores\_ will be rendered inside `<i>` tags.
- Text surrounded by \*asterisks\* will be rendered inside `<b>` tags.

#### [Strikethrough](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages#strikethrough)
- Text surrounded by \~tildes\~ will be rendered inside `<s>` tags.

#### [Lists](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages#lists)
- Lines of text that begin with a bullet(`•`), hyphen(`-`), or digit followed by a period(`1.`) will be rendered inside `<li>` tags.
- Bulleted and hyphened lists are rendered inside `<ul>` tags.
- Numbered lists are rendered inside `<ol>` tags.
    - _Note that the numbers used in the original text will be ignored and they will instead be rendered using your CSS list style._
- To include multiple lists add an extra line break between them. This line break will not be rendered in the final HTML.
```
- item 1
- item 2
- item 3

1. item 1
2. item 2
3. item 3
```
is rendered as
```
<ul>
   <li>item 1</li>
   <li>item 2</li>
   <li>item 3</li>
</ul>
<ol>
   <li>item 1</li>
   <li>item 2</li>
   <li>item 3</li>
</ol>
```

#### [Blockquotes](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages#blockquotes)
- Lines of text that start with a `&gt;`s are rendered inside `<blockquote>` tags.
- Text blocks that include a line starting with three `&gt;`s will render the message from that point on inside `<blockquote>` tags.
_Note: the Slack API returns all `>` as `&gt;` because angle brackets are used for links in Slack text formatting See [the documentation](https://api.slack.com/docs/message-formatting#how_to_escape_characters) for more._
```
> A blockquote line
>>> Multiple lines
of a
blockquote
```
is rendered as
```
<blockquote>A blockquote line</blockquote>
<blockquote>
    Multiple lines </br>
    of a </br>
    blockquote
</blockquote>
```

####  [Code Blocks](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages#code-blocks)
- Text surrounded in \`backticks\` will be rendered inside `<code>` tags.
- Text surrounded by \`\`\`three backticks\`\`\` will be rendered inside `<pre>` tags.

####  Line Breaks
- Line breaks rendered inside `<p>` tags will close the tag and start a new paragraph. Line breaks in other block elements will be rendered as `<br />` tags.
```
Multiple
lines of
paragraph text

` ` `
Multiple
lines of
pre text
` ` `
```
is rendered as
```
<p>Multiple</p>
<p>lines of</p>
<p>paragraph text</p>
<p></p>
<pre>
Multiple <br />
lines of <br />
pre text
</pre>
```

####  Spaces
- Since extra whitespace is stripped in HTML, any extra space is rendered using &nbsp. Every two space characters are rendered as a space character and a &nbsp. This minimizes added characters while keeping the same amount of rendered whitespace as the original text.
