from time import time
from verkada_py import Organization
from .mock_responses import time_response


def test_camera(default_org):
    org = Organization()
    camera = org.cameras[0]
    assert camera.id == "rzabvxfk-7a67-zc4lm-8p0v-k23mi9houom3g68"
    assert camera.cloud_retention == "30 Days"
    assert camera.date_added == 90
    assert camera.device_retention == "30 Days"
    assert camera.firmware == "latest"
    assert camera.IP == "192.168.0.1"
    assert camera.location == "cloud"
    assert camera.MAC == "C9-67-EB-8D-BA-E3"
    assert camera.model == "CD41"
    assert camera.name == "API MOCK Camera"
    assert camera.serial == "E38D-BAEB-67C8"
    assert camera.site == "API MOCK Site"
    assert camera.cam_url == "https://api.verkada.com/orgs/test_org_id/cameras/rzabvxfk-7a67-zc4lm-8p0v-k23mi9houom3g68"
    assert str(camera) == repr(camera) == "Verkada Camera API MOCK Camera"


def test_camera_footage(footage_link, requests_mock):
    org = Organization()
    camera = org.cameras[0]
    assert camera.get_footage_link(200) == "https://command.verkada.com/footage"
    requests_mock.get(
        f'https://api.verkada.com/orgs/test_org_id/cameras/rzabvxfk-7a67-zc4lm-8p0v-k23mi9houom3g68/history/{int(time())}',
        json=time_response
    )
    assert camera.get_footage_link() == "https://command.verkada.com/footage/default_time"


def test_failed_camera_footage(failed_footage_link):
    org = Organization()
    camera = org.cameras[0]
    assert camera.get_footage_link(200) == ""


def test_camera_thumbnail(camera_thumbnail_link):
    org = Organization()
    camera = org.cameras[0]
    assert camera.get_thumbnail(200) == "https://command.verkada.com/thumbnail"


def test_failed_thumbnail(failed_camera_thumbnail):
    org = Organization()
    camera = org.cameras[0]
    assert camera.get_thumbnail(200) == ""
