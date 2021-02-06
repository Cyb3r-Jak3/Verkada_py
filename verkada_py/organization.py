"""Organization Class"""
# Built-in
import base64
from typing import List

# 3rd Party
from requests import HTTPError

# Internal
from verkada_py.shared import SharedAttributes
from verkada_py.camera import Camera


class Organization(SharedAttributes):
    """
    Organization represents a Verkada organization.
    It has a api-key and organization ID which is needed to make requests
    """

    def __init__(self, get_cameras: bool = True, org_id: str = None, api_key: str = None):
        """
        Parameters
        ----------
        get_cameras: A bool if to get all the cameras for the organization. Enabled by default
        """
        super().__init__(api_key=api_key, org_id=org_id)
        if get_cameras:
            self.cameras = self._get_cameras()

    def _get_cameras(self) -> List[Camera]:
        """
        Gets all the cameras for an organization.
        Returns
        -------
            A list of cameras in the organzation.
        """
        camera_resp = self._session.get(self.url + "cameras")
        try:
            camera_resp.raise_for_status()
        except HTTPError:
            return []

        return [Camera(camera, self.api_key, self.org_id) for camera in camera_resp.json()["cameras"]]

    def get_notifications(
        self,
        start_time: int = None,
        end_time: int = None,
        include_image: str = "false",
        notification_types: str = "person_of_interest,tamper,crowd,"
        "motion,camera_offline,camera_online",
    ) -> list:
        """
        Gets all the notifications for an organization

        TODO: Create a class representing an notification
        Parameters
        ----------
        start_time: The start epoch time
        end_time: The end epoch time
        include_image: If to include the image for related events
        notification_types: The notification types to query for

        Returns
        -------
        A list of notifications
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
        return notifications

    def get_poi(self) -> list:
        """
        Gets all the people of interest for an organization

        ToDo: Create custom POI class
        Returns
        -------
        A list of people of interest
        """
        get_poi_resp = self._session.get(self.url + "persons_of_interest")
        try:
            get_poi_resp.raise_for_status()
            return get_poi_resp.json()["persons_of_interest"]
        except HTTPError:
            return []

    def create_poi(self, image: str, label: str = None) -> str:
        """
        Creates a person of interest for the organization
        ToDo: Create custom POI class
        Parameters
        ----------
        image: The path to a photo of the person
        label: The label for the person

        Returns
        -------
        A string of the person ID who was created
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

    def update_poi(self, person_id: str, label: str) -> str:
        """
        Adds/changes a label for a person of interest

        ToDo: Create custom POI class
        Parameters
        ----------
        person_id: The person id to add/change the label for
        label: The label to all the person

        Returns
        -------
        The person ID that had a label change
        """
        return (
            self._session.patch(
                self.url + "persons_of_interest/{}".format(person_id),
                json={"label": label},
            )
            .json()
            .get("person_id")
        )

    def delete_poi(self, person_id: str):
        """
        Deletes a person of interest

        ToDo: Create custom POI class
        Parameters
        ----------
        person_id: The person ID to delete

        Returns
        -------
        A string of the person of interest that was deleted
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
