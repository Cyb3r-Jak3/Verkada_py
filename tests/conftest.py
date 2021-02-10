"""Custom Fixtures"""
import pytest
from .mock_responses import *


@pytest.fixture
def default_org(requests_mock):
    return requests_mock.get("https://api.verkada.com/orgs/test_org_id/cameras",
                             json=camera_response)


@pytest.fixture
def camera_objects(requests_mock, default_org):
    return requests_mock.get(
        "https://api.verkada.com/orgs/test_org_id/cameras/8438a7f2-fdbc-4392-8b9b-d47513bcf5c8/objects/counts?start_time=100&end_time=200",
        json=camera_object_response
    )


@pytest.fixture
def failure_org(requests_mock):
    return requests_mock.get("https://api.verkada.com/orgs/test_org_id/cameras",
                             status_code=500)


@pytest.fixture
def get_poi(requests_mock, default_org):
    return requests_mock.get("https://api.verkada.com/orgs/test_org_id/persons_of_interest",
                             json=get_person_of_interest)


@pytest.fixture
def get_failed_poi(requests_mock, default_org):
    return requests_mock.get("https://api.verkada.com/orgs/test_org_id/persons_of_interest",
                             status_code=500)


@pytest.fixture
def create_poi(requests_mock, default_org):
    return requests_mock.post("https://api.verkada.com/orgs/test_org_id/persons_of_interest",
                              json=create_person_of_interest)


@pytest.fixture
def update_poi(requests_mock, default_org):
    return requests_mock.patch(
        "https://api.verkada.com/orgs/test_org_id/persons_of_interest/078bffa7-20cf-4307-a047-29e98b340e8e",
        json=create_person_of_interest)


@pytest.fixture
def delete_poi(requests_mock, default_org):
    return requests_mock.delete(
        "https://api.verkada.com/orgs/test_org_id/persons_of_interest/078bffa7-20cf-4307-a047-29e98b340e8e",
        json=create_person_of_interest)


@pytest.fixture
def footage_link(requests_mock, default_org):
    return requests_mock.get(
        "https://api.verkada.com/orgs/test_org_id/cameras/8438a7f2-fdbc-4392-8b9b-d47513bcf5c8/history/200",
        json=footage_link_response
    )


@pytest.fixture
def failed_footage_link(requests_mock, default_org):
    return requests_mock.get(
        "https://api.verkada.com/orgs/test_org_id/cameras/8438a7f2-fdbc-4392-8b9b-d47513bcf5c8/history/200",
        status_code=500
    )


@pytest.fixture
def camera_thumbnail_link(requests_mock, default_org):
    return requests_mock.get(
        "https://api.verkada.com/orgs/test_org_id/cameras/8438a7f2-fdbc-4392-8b9b-d47513bcf5c8/thumbnail/200",
        json=thumbnail_link_response
    )


@pytest.fixture
def failed_camera_thumbnail(requests_mock, default_org):
    return requests_mock.get(
        "https://api.verkada.com/orgs/test_org_id/cameras/8438a7f2-fdbc-4392-8b9b-d47513bcf5c8/thumbnail/200",
        status_code=500
    )
