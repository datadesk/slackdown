def render_author(**kwargs):
    """
    Unstrict template block for rendering authors:
    <div class="author">
        <img class="author-avatar" src="{author_avatar}">
        <p class="author-name">
            <a href="{author_link}">{author_name}</a>
        </p>
        <p class="user-handle">{author_handle}</p>
    </div>
    """
    html = '<div class="user">'

    author_avatar = kwargs.get('author_avatar', None)
    if author_avatar:
        html += '<img class="user-avatar" src="{}">'.format(author_avatar)

    author_name = kwargs.get('author_name', None)
    if author_name:
        html += '<p class="user-name">'

        author_link = kwargs.get('author_link', None)
        if author_link:
            html += '<a href="{author_link}">{author_name}</a>'.format(
                author_link=author_link,
                author_name=author_name
            )
        else:
            html += author_name

        html += '</p>'

    author_handle = kwargs.get('author_handle', None)
    if author_handle:
        html += '<p class="user-handle">{}</p>'.format(author_handle)

    html += '</div>'


def render_metadata(**kwargs):
    """
    Unstrict template block for rendering metadata:
    <div class="metadata">
        <img class="metadata-logo" src="{service_logo}">
        <p class="metadata-name">{service_name}</p>
        <p class="metadata-timestamp">
            <a href="{timestamp_link}">{timestamp}</a>
        </p>
    </div>
    """
    html = '<div class="metadata">'

    service_logo = kwargs.get('service_logo', None)
    if service_logo:
        html += '<img class="metadata-logo" src="{}">'.format(service_logo)

    service_name = kwargs.get('service_name', None)
    if service_name:
        html += '<p class="metadata-name">{}</p>'.format(service_name)

    timestamp = kwargs.get('timestamp', None)
    if timestamp:
        html += '<p class="user-name">'

        timestamp_link = kwargs.get('timestamp_link', None)
        if timestamp_link:
            html += '<a href="{timestamp_link}">{timestamp}</a>'.format(
                timestamp_link=timestamp_link,
                timestamp=timestamp
            )
        else:
            html += timestamp

        html += '</p>'

    html += '</div>'


def render_image(**kwargs):
    """
    Unstrict template block for rendering an image:
    <img alt="{alt_text}" title="{title}" src="{url}">
    """
    html = ''

    url = kwargs.get('url', None)
    if url:
        html = '<img'

        alt_text = kwargs.get('alt_text', None)
        if alt_text:
            html += ' alt="{}"'.format(alt_text)

        title = kwargs.get('title', None)
        if title:
            html += ' title="{}"'.format(title)

        html += ' src="{}">'.format(url)

    return html


def render_twitter(text, **kwargs):
    """
    Strict template block for rendering twitter embeds.
    """
    author = render_author(**kwargs['author'])
    metadata = render_metadata(**kwargs['metadata'])
    image = render_image(**kwargs['image'])

    html = """
        <div class="attachment attachment-twitter">
            {author}
            <p class="twitter-content">{text}</p>
            {metadata}
            {image}
        </div>
    """.format(
        author=author,
        text=text,
        metadata=metadata,
        image=image
    ).strip()

    return html
