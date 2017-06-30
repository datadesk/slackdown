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

Importing the library

```python
import slackdown
```

Convert a Slack message to HTML

```python
>>> slackdown.render('*Bold*')
'<b>Bold</b>'
```

```python
>>> slackdown.render('_italics_')
'<i>italics</i>'
```
