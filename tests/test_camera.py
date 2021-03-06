from time import time
from verkada_py import Organization
from .mock_responses import time_response, camera_object_response_two


def test_camera(default_org):
    org = Organization(org_id="test_org_id", api_key="test_api_key")
    camera = org.cameras[0]
    assert camera.id == "8438a7f2-fdbc-4392-8b9b-d47513bcf5c8"
    assert camera.cloud_retention == 30
    assert camera.date_added == 90
    assert camera.device_retention == 30
    assert camera.firmware
    assert camera.IP == "192.168.0.1"
    assert camera.location == "cloud"
    assert camera.MAC == "C9-67-EB-8D-BA-E3"
    assert camera.model == "CD41"
    assert camera.name == "API MOCK Camera"
    assert camera.serial == "E38D-BAEB-67C8"
    assert camera.site == "API MOCK Site"
    assert camera.cam_url == "https://api.verkada.com/orgs/test_org_id/cameras/8438a7f2-fdbc-4392-8b9b-d47513bcf5c8"
    assert camera.last_online == 200
    assert camera.status == "Live"
    assert str(camera) == repr(camera) == "Verkada Camera API MOCK Camera"


def test_camera_objects(requests_mock, camera_objects):
    org = Organization(org_id="test_org_id", api_key="test_api_key")
    camera = org.cameras[0]
    requests_mock.get(
        "https://api.verkada.com/orgs/test_org_id/cameras/8438a7f2-fdbc-4392-8b9b-d47513bcf5c8/object/counts?start_time=100&end_time=200&per_page=200&page_cursor=go_to_two",
        json=camera_object_response_two
    )
    assert isinstance(camera.get_object_count(100, 200), dict)


def test_camera_footage(footage_link, requests_mock):
    org = Organization(org_id="test_org_id", api_key="test_api_key")
    camera = org.cameras[0]
    assert camera.get_footage_link(200) == "https://command.verkada.com/footage"
    requests_mock.get(
        f'https://api.verkada.com/orgs/test_org_id/cameras/8438a7f2-fdbc-4392-8b9b-d47513bcf5c8/history/{int(time())}',
        json=time_response
    )
    assert camera.get_footage_link() == "https://command.verkada.com/footage/default_time"


def test_failed_camera_footage(failed_footage_link):
    org = Organization(org_id="test_org_id", api_key="test_api_key")
    camera = org.cameras[0]
    assert camera.get_footage_link(200) == ""


def test_camera_thumbnail(camera_thumbnail_link):
    org = Organization(org_id="test_org_id", api_key="test_api_key")
    camera = org.cameras[0]
    assert camera.get_thumbnail_link(200) == "https://command.verkada.com/thumbnail"


def test_failed_thumbnail(failed_camera_thumbnail):
    org = Organization(org_id="test_org_id", api_key="test_api_key")
    camera = org.cameras[0]
    assert camera.get_thumbnail_link(200) == ""
