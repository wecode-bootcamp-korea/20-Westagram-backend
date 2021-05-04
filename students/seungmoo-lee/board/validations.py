import re

class PostValidation:

    def check_required_fields(self, *args):
        return None in args

    def check_image_url(self, image_url):
        image_url_pattern = re.compile('^(http(s?):)([/|.|\w|\s])*\.(?:jpg|gif|png|gif)+$')
        return image_url_pattern.match(image_url) is None
