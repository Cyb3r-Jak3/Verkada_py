"""Shared Classes and values"""
import requests
import os

__version__ = "0.0.1-dev"


class SharedAttributes:
    """Class that gets used by Organization and Camera class to share attributes"""

    # pylint: disable=too-few-public-methods
    def __init__(self, api_key: str = None, org_id: str = None):
        self.api_key = api_key if api_key else os.environ["API_KEY"]
        self.org_id = org_id if org_id else os.environ["ORG_ID"]
        self.url = "https://api.verkada.com/orgs/{}/".format(self.org_id)
        self._session = self._create_session()

    def _create_session(self) -> requests.Session:
        session = requests.Session()
        session.headers.update(
            {"x-api-key": self.api_key, "User-Agent": f"verkadapy v:{__version__}"}
        )
        return session
