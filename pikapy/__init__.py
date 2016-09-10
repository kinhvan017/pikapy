#!/usr/bin/python
import urllib2
import json


class PikaError(Exception):
    pass


class PikaClient(object):

    # Valid paste_expire_after values
    # (Never, 1 minute, 5 minutes, 10 minutes, 1 hour, 1 day)
    paste_expire_date = ('0',  # Delete paste after reading
                         '-1',  # No expire
                         '1m', '5m', '10m', '1h', '1d')

    def __init__(self, url='https://pikab.in/'):
        self.base_url = url

    def paste(self, content, paste_title='Untitled', paste_expire_after='5m',
              paste_syntax='plain'):
        """Submit a code snippet to Pika using API.


        Usage Example::
            >>> from pikapy import PikaClient
            >>> x = PikabClient('https://pikab.in/')
            >>> url = x.paste('String ABC',
            ...               paste_title="demo paste",
            ...               paste_expire_after = '10m',
            ...               paste_syntax = 'python')
            >>> print url
            https://pikab.in/d91a0bf2e0979ca8648262da4ebbfdc357a79s

        @type   content: string
        @param  content: String to paste to body of the U{http://pikab.in} paste.

        @type   paste_name: string
        @param  paste_name: (Optional) Title of the paste.
            Default is to paste anonymously.

        @type  paste_expire_after: str
        @param paste_expire_after: (Optional) Expiration time for the paste.
            The paste will be deleted automatically.
            Valid values are found in the L{PikaClient.paste_expire_date}.
            If not provided, the paste expires after 5 minutes.

        @type  paste_syntax: string
        @param paste_format: (Optional) Programming language of the code being
            pasted. This enables syntax highlighting when reading the code in
            U{http://pikab.in}. Default is no syntax highlighting (text is
            just text and not source code).
            Valid values are found in the http://goo.gl/nLFqyB
        """
        payload = {
            'document': {
                'content': content,
                'title': paste_title,
                'expired_at': paste_expire_after,
                'syntax': paste_syntax
            }
        }

        data = json.dumps(payload)
        try:
            req = urllib2.Request(self.base_url, data,
                                  {'Content-Type': 'application/json'})

            response = urllib2.urlopen(req)
            # return pikab.in url
            return json.loads(response.read())['uri']

        except urllib2.HTTPError:
            raise PikaError("Content can't be blank")
        except Exception as e:
            raise PikaError(e)

if __name__ == "__main__":
    client = PikaClient('https://pikab.in/')
    print client.paste("asd")
