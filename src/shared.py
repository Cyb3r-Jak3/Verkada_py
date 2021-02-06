"""Shared Classes and values"""
import requests

__version__ = "0.0.1-dev"


class SharedAttributes:
    """Class that gets used by Organization and Camera class to share attributes"""
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.api_key = "test_api_key"
        self.org_id = "test_org_id"
        self.url = "https://api.verkada.com/orgs/{}/".format(self.org_id)
        self._session = self._create_session()

    def _create_session(self) -> requests.Session:
        session = requests.Session()
        session.headers.update(
            {"x-api-key": self.api_key,
             "User-Agent": f"verkadapy v:{__version__}"}
        )
        return session
