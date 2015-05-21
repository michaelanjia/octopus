__author__ = 'at'

from urllib import urlencode
import requests


class FetchUrl(object):
    """
    Form urls, parse and
    """
    def __init__(self, base_url, metric, username, apikey, granularity, start_date, end_date):
        """
        :param base_url:
        :param metric:
        :param username:
        :param apikey:
        :param granularity:
        :param start_date:
        :param end_date:
        :return: url object
        """
        self.base_url = base_url
        self.metric = metric
        self.username = username
        self.apikey = apikey
        self.granularity = granularity
        self.start_date = start_date
        self.end_date = end_date

    def form_url(self):
        query_args = {'granularity': self.granularity, 'startDate': self.start_date,
                      'endDate': self.end_date, 'metric': self.metric, 'username': self.username}
        _url = urlencode(query_args)
        return self.base_url + _url

    def get_apikey(self):
        return self.apikey


class MakeRequests(object):
    """
    Some request helper classes
    """
    def __init__(self, url, apikey, method='GET'):
        """
        :param url:
        :param apikey:
        :param method:
        :return: None
        """
        self.method = method
        self.url = url
        self.apikey = apikey

    def send_(self):
        """
        :param self
        :return: response object
        """
        if self.method is 'GET':
            headers = {'apikey': self.apikey}
            r = requests.get(self.url, headers=headers)
            return r


def make_call():
    pass


def send_text():
    pass