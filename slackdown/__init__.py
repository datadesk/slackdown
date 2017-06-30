import re


def render(txt):
    """
    Accepts Slack formatted text and returns HTML.
    """
    # handle ordered and unordered lists
    lists = {
        '\-': 'ul',
        u'\u2022': 'ul',
        '\d*\.': 'ol',
    }
    for html_list in lists:
        slack_tag = html_list
        html_tag = lists[html_list]

        # Wrap any lines that start with the slack_tag in <li></li>
        list_regex = u'(?:^|\n){}\s?(.*)'.format(slack_tag)
        list_repl = r'<li>\g<1></li>'
        txt = re.sub(list_regex, list_repl, txt)

        # Wrap any <li></li> groups not already wrapped in html_tag
        """
        List Wrapping Regex
        r'(?<!(?<=<[u|o]l>)|(?<=</li>\n)|(?<=</li>))(<li>.+?</li>)\n?(?!\n?<li>)'

        - Match any group of <li> elements that aren't wrapped in <ol></ol> or <ul></ul> tags.

        - The capture group is located in the middle: (<li>.+?</li>)
           which means grab (non-greedy) any set of characters inside and including <li></li> tags.

        - The capture group cannot be proceeded by a <ul>,<ol>,or</li>.
          -- If it's proceeded by a <ul> or <ol>, then it's already wrapped.
          -- If it's proceeded by an </li>, then it's not the first item in the list.
          To do this it includes a negative lookbehind (?<!...) which disqualifies those prefixes.
          Inside that negative lookbehind is three possible positive lookbehinds.
          Those three possible options (separated by pipe) are:
          -- (?<=<[u|o]l>): a <ul> or <ol>
          -- (?<=</li>\n): an </li> followed by a line break
          -- (?<=</li>): an </li> (note that lookbehinds must be a fixed length so (?<=</li>\n?) wouldn't work.)
           Here's a traditional boolean logic to regex translation:
           !(   (starts_with_ol|starts_with_ul) | (starts_with_li_break) | (starts_with_li)   )
           (?<!          (?<=<[u|o]l>)          |      (?<=</li>\n)      |    (?<=</li>)      )

        - The capture group should end with an </li> that is not immediately followed by an <li>
          (with the optional addition of a single line break between them).
          This signifies the end of the list. For this I used a negative lookahead (?!...)
          with a single optional \n and an <li>.

        - There's also an extra optional single space \n? after the capture group. That's there to remove the line
          break at the end of the list.
        """
        unwwrapped_lists_regex = r'(?<!(?<=<[u|o]l>)|(?<=</li>\n)|(?<=</li>))(<li>.+?</li>)\n?(?!\n?<li>)'
        wrapper_string_repl = r'<{t}>\g<1></{t}>'.format(t=html_tag)
        txt = re.sub(unwwrapped_lists_regex, wrapper_string_repl, txt)

    # hanlde blockquotes
    txt = re.sub(u'(?:^|\n)(?:&gt;){3}\s?(.*)$', r'<blockquote>\1</blockquote>', txt, flags=re.DOTALL)
    txt = re.sub(u'(?:^|\n)&gt;\s?(.*)\n?', r'<blockquote>\1</blockquote>', txt)

    # handle code blocks
    txt = re.sub(r'```\n?(.*)```', r'<pre>\g<1></pre>', txt, flags=re.DOTALL)
    txt = re.sub(r'\n(</pre>)', r'\g<1>', txt)

    # handle bolding, italics, and strikethrough
    wrappers = {
        '*': 'b',
        '_': 'i',
        '~': 's',
        '`': 'code',
    }
    for wrapper in wrappers:
        slack_tag = wrapper
        html_tag = wrappers[wrapper]

        regex_string = '\{t}([^\{t}]*)\{t}'.format(t=slack_tag)
        regex = re.compile(regex_string, flags=re.DOTALL)
        repl = r'<{t}>\g<1></{t}>'.format(t=html_tag)
        txt = re.sub(regex, repl, txt)

    # convert multiple spaces
    txt = txt.replace(r'  ', ' &nbsp')

    # convert line breaks
    txt = txt.replace('\n', '<br />')

    return txt
