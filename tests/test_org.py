from verkada_py import Organization
import os
from .mock_responses import notification_response, notification_pagination_response

TEST_PATH = os.path.abspath(os.path.dirname(__file__))


def test_organization(default_org):
    org = Organization()
    assert isinstance(org, Organization)
    assert org.api_key == "test_api_key"
    assert org.org_id == "test_org_id"
    assert org.url == "https://api.verkada.com/orgs/test_org_id/"
    assert org._session.headers["x-api-key"] == "test_api_key"
    assert len(org.cameras) == 1
    assert str(org) == repr(org) == "Verkada Organization test_org_id"


def test_failed_organization(failure_org):
    org = Organization()
    assert len(org.cameras) == 0


def test_organization_notifications(requests_mock, default_org):
    requests_mock.get(
        "https://api.verkada.com/orgs/test_org_id/notifications",
        json=notification_response
    )
    requests_mock.get(
        "https://api.verkada.com/orgs/test_org_id/notifications?notification_types=person_of_interest%2Ctamper"
        "%2Ccrowd%2Cmotion%2Ccamera_offline%2Ccamera_online&include_image_url=false&page_cursor=go_to_two&per_page"
        "=200",
        json=notification_pagination_response
    )
    org = Organization()
    notifications = org.get_notifications()
    assert isinstance(notifications, list)
    assert len(notifications) == 2
    notification = notifications[0]
    assert notification["notification_type"] == "person_of_interest"
    assert len(notification["objects"]) == 0
    assert notification["camera_id"] == "8438a7f2-fdbc-4392-8b9b-d47513bcf5c8"
    assert notification["crowd_threshold"] is None
    assert notification["person_label"] == "API DUMMY"
    assert notification["created"] == 156156156
    assert notification["video_url"] == "https://www.google.com/video"
    assert notification["image_url"] == "https://www.google.com/image"


def test_organization_get_poi(get_poi):
    org = Organization()
    poi = org.get_poi()
    assert len(poi) == 1
    single_entry = poi[0]
    assert single_entry["label"] == "API DUMMY"
    assert single_entry["person_id"] == "078bffa7-20cf-4307-a047-29e98b340e8e"
    assert single_entry["created"] == 156156156
    assert single_entry["last_seen_camera_id"] == "8438a7f2-fdbc-4392-8b9b-d47513bcf5c8"
    assert single_entry["last_seen"] == 1561561565


def test_failed_poi(get_failed_poi):
    org = Organization()
    poi = org.get_poi()
    assert len(poi) == 0


def test_organization_create_poi(create_poi):
    org = Organization()
    new_poi = org.create_poi(image="{}/criminal.jpg".format(TEST_PATH), label="API DUMMY")
    assert new_poi == "078bffa7-20cf-4307-a047-29e98b340e8e"


def test_organization_update_poi(update_poi):
    org = Organization()
    updated_poi = org.update_poi("078bffa7-20cf-4307-a047-29e98b340e8e", "API_DUMMY_2")
    assert updated_poi == "078bffa7-20cf-4307-a047-29e98b340e8e"


def test_organization_delete_poi(delete_poi):
    org = Organization()
    deleted_poi = org.delete_poi("078bffa7-20cf-4307-a047-29e98b340e8e")
    assert deleted_poi == "078bffa7-20cf-4307-a047-29e98b340e8e"
