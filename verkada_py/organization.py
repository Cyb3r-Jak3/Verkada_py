"""Organization Class"""
# Built-in
import base64
import functools
from typing import List

# 3rd Party
from requests import HTTPError

# Internal
from verkada_py.shared import SharedAttributes
from verkada_py.camera import Camera
from verkada_py.modals import Notification, PersonofInterest


def get_poi_id_from_poi(func):
    """
    Decorator that gets a person of interest ID if using custom POI class
    """

    @functools.wraps(func)
    def inner(*args):
        if isinstance(args[0], PersonofInterest):
            args = args[0].person_id
        return func(*args)

    return inner


class Organization(SharedAttributes):
    """
    Organization represents a Verkada organization.
    It has a api-key and organization ID which is needed to make requests
    """

    def __init__(
        self, get_cameras: bool = True, org_id: str = None, api_key: str = None
    ):
        """
        :param get_cameras: ``bool`` Get all the cameras for the organization. Enabled by default
        :param org_id: ``str`` Organization ID
        :param api_key: ``str`` API Key for organization
        """
        super().__init__(api_key=api_key, org_id=org_id)
        if get_cameras:
            self.cameras = self._get_cameras()

    def _get_cameras(self) -> List[Camera]:
        """
        Get all the cameras for an organization.
        :return: ``list`` Cameras in the organization.
        """
        camera_resp = self._session.get(self.url + "cameras")
        try:
            camera_resp.raise_for_status()
        except HTTPError:
            return []

        return [
            Camera(camera, self.api_key, self.org_id)
            for camera in camera_resp.json()["cameras"]
        ]

    def get_notifications(
        self,
        start_time: int = None,
        end_time: int = None,
        include_image: bool = False,
        notification_types: str = "person_of_interest,tamper,crowd,"
        "motion,camera_offline,camera_online",
    ) -> List[Notification]:
        """
        Get all the notifications for an organization
        :param start_time: ``int`` Start epoch time
        :param end_time: ``int` End epoch time
        :param include_image: ``bool`` Include the image for notifications
        :param notification_types: ``str`` Notification types to query for
        :return: ``list`` Notifications where each notification is a dict
        """
        notification_resp = self._session.get(
            self.url + "notifications",
            params={
                "notification_types": notification_types,
                "start_time": start_time,
                "end_time": end_time,
                "include_image_url": include_image,
                "per_page": 200,
            },
        )
        notifications = notification_resp.json()["notifications"]
        page_cursor = notification_resp.json()["page_cursor"]
        while page_cursor is not None:
            sub_notification_resp = self._session.get(
                self.url + "notifications",
                params={
                    "notification_types": notification_types,
                    "start_time": start_time,
                    "end_time": end_time,
                    "include_image_url": include_image,
                    "page_cursor": page_cursor,
                    "per_page": 200,
                },
            )
            notifications.extend(sub_notification_resp.json()["notifications"])
            page_cursor = sub_notification_resp.json()["page_cursor"]
        return [Notification(x) for x in notifications]

    def get_poi(self) -> List[PersonofInterest]:
        """
        Get all the people of interest for an organization
        :return: ``list`` People of interest
        """
        get_poi_resp = self._session.get(self.url + "persons_of_interest")
        try:
            get_poi_resp.raise_for_status()
            return [
                PersonofInterest(x) for x in get_poi_resp.json()["persons_of_interest"]
            ]
        except HTTPError:
            return []

    def create_poi(self, image: str, label: str = None) -> str:
        """
        Create a person of interest for the organization
        :param image: ``str`` Path to a photo of the person
        :param label: ``str`` Label for the person
        :return: ``str`` Person ID who was created
        """
        with open(image, "rb") as image_file:
            encoded_image = base64.urlsafe_b64encode(image_file.read())
        return (
            self._session.post(
                self.url + "persons_of_interest",
                params={"base64_image": encoded_image, "label": label},
            )
            .json()
            .get("person_id")
        )

    @get_poi_id_from_poi
    def update_poi(self, person_id: str, label: str) -> str:
        """
        Change a label for a person of interest
        :param person_id: ``str`` Person id to change the label for
        :param label: ``str`` Label of the person
        :return: ``str`` Person ID that had a label change
        """
        return (
            self._session.patch(
                self.url + "persons_of_interest/{}".format(person_id),
                json={"label": label},
            )
            .json()
            .get("person_id")
        )

    @get_poi_id_from_poi
    def delete_poi(self, person_id: str) -> str:
        """
        Delete a person of interest
        :param person_id: ``str`` Person ID to delete
        :return: ``str`` Person ID that was deleted
        """
        return (
            self._session.delete(self.url + "persons_of_interest/{}".format(person_id))
            .json()
            .get("person_id")
        )

    def __str__(self):
        return f"Verkada Organization {self.org_id}"

    def __repr__(self):
        return f"Verkada Organization {self.org_id}"
