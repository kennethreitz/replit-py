from requests import Session as HTTPSession
from requests_html import HTMLSession

http = HTTPSession()
html_http = HTMLSession()


class ReplitUser:
    def __init__(self):
        #  validate_username=False
        # self.user_id = None
        self.username = None
        self.name = None
        self.bio = None
        self.avatar_url = None
        self.languages = None
        # self.roles = None

    # @classmethod
    # def from_user_id(_class, user_id):
    #     # TODO: find a way to reverse username from user_id (ask eng?)
    #     pass

    @classmethod
    def from_username(_class, username):
        # TODO: catch non-existient users.
        url = _class._replit_url_from_username(username)
        return _class.from_replit_profile_url(url)

    @classmethod
    def from_replit_profile_url(_class, url):
        # https://repl.it/@kennethreitz42
        r = html_http.get(url=url)
        html = r.html

        user = _class()

        user.name = user.__extract_name(html)
        user.bio = user.__extract_bio(html)
        user.avatar_url = user.__extract_avatar_url(html)
        # user.languages = user.__extract_languages(html)
        # user.roles = user.__extract_roles(html)

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

    # def __extract_languages(self, html):
    #     pass

    # def __extract_roles(self, html):
    #     pass

    # list repls


print(ReplitUser.from_username("kennethreitz42").avatar_content)
