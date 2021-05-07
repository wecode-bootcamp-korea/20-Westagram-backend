import re

class PostValidation:

    def check_required_fields(self, *args):
        return None in args

    def check_image_urls(self, image_urls):
        image_url_pattern = re.compile('^(http(s?):)([/|.|\w|\s])*\.(?:jpg|gif|png|gif)+$')

        for image_url in image_urls:
            if image_url_pattern.match(image_url) is None:
                return True
