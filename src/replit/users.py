from requests import Session as HTTPSession
from requests_html import HTMLSession

http = HTTPSession()
html_http = HTMLSession()

# TODO: provide a way to list repls.


class ReplitUser:
    def __init__(self):
        self.username = None
        self.name = None
        self.bio = None
        self.avatar_url = None
        self.languages = None

    @classmethod
    def from_username(_class, username):
        """Creates a new ReplitUser object from a given Repl.it profile name."""
        # TODO: catch non-existient users.
        url = _class._replit_url_from_username(username)
        return _class.from_replit_profile_url(url)

    @classmethod
    def from_replit_profile_url(_class, url):
        """Creates a new ReplitUser object from a given Repl.it profile URL."""

        # Fetch the profile from the web, and encapsulate its HTML.
        r = html_http.get(url=url)
        html = r.html

        # Instantiate the class.
        user = _class()

        # Populate the user instance from parsed HTML.
        user.name = user.__extract_name(html)
        user.bio = user.__extract_bio(html)
        user.avatar_url = user.__extract_avatar_url(html)

        return user

    @property
    def avatar_content(self):
        if self.avatar_url:
            return http.get(self.avatar_url).content

    @staticmethod
    def _replit_url_from_username(username):
        return f"https://repl.it/@{username}"

    def __extract_name(self, html):
        return html.find("h1", first=True).text

    def __extract_bio(self, html):
        return html.find(".Linkify", first=True).text

    def __extract_avatar_url(self, html):
        e = html.find(".profile-icon > span", first=True)
        style_str = e.attrs["style"]

        # Remove the CSS-y parts of the image URL, in a clear manner.
        len_0 = len('background-image:url("')
        len_1 = len('"]')

        # Slice the background string up.
        avatar_url = style_str[len_0 : (len(style_str) - len_1)]

        return avatar_url


# Syntax suagar.
User = ReplitUser
