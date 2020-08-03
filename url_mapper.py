from nanoid import generate


class UrlMapper:
    def create_url_map_item(self, long_url='', domain_name='', path=''):
        random_chars = self.get_random_chars()
        # in a dev SLS environment, this "short" url is very long
        short_url = 'https://%s%s%s' % (domain_name, path, random_chars)

        return {
            # remember pk (and sk when appropriate) solely exists for data access
            'pk': random_chars,
            'type': 'url_map',
            'id':  random_chars,
            'long_url': long_url,
            'short_url': short_url
        }

    def get_random_chars(self):
        return generate(size=5)
