"""Camera class. Organization will have a lot of these class"""
# Built in
import functools
import time

# 3rd Party
from requests import HTTPError

# Internal
from cached_property import cached_property
from verkada_py.shared import SharedAttributes


def set_default_timestamp(func):
    """
    Decorator that sets the default time to the current time
    """

    @functools.wraps(func)
    def inner(*args):
        if len(args) == 1:
            args = (*args, int(time.time()))
        return func(*args)

    return inner


class Camera(SharedAttributes):
    # pylint: disable=invalid-name
    """
    Camera class represents a camera in a Verkada Organization.
    """

    def __init__(self, info: dict):
        super().__init__()
        self._info = info
        self.cam_url = self.url + f"cameras/{self.id}"

    def get_object_count(self, start_time: int = None, end_time: int = None) -> dict:
        """
            Gets the number of detected people and vehicles for a camera
        Parameters
        ----------
        start_time: The epoch time to start getting the count for
        end_time: The end epoch time to get the count for

        Returns
        -------
            A dict that contains "people" and "vehicles" with an int for each one.
        """
        object_resp = self._session.get(
            self.cam_url + "objects/counts",
            params={"start_time": start_time, "end_time": end_time, "per_page": 200},
        )
        count_objects = object_resp.json()["object_counts"]
        page_cursor = object_resp.json()["page_cursor"]
        while page_cursor is not None:
            sub_object_resp = self._session.get(
                self.cam_url + "object/counts",
                params={
                    "start_time": start_time,
                    "end_time": end_time,
                    "per_page": 200,
                    "page_cursor": page_cursor,
                },
            )
            count_objects.extend(sub_object_resp.json()["object_counts"])
            page_cursor = sub_object_resp.json()["page_cursor"]
        counts = {"people": 0, "vehicles": 0}
        for count in count_objects:
            counts["people"] += count["people_count"]
            counts["vehicles"] += count["vehicle_count"]
        return counts

    @set_default_timestamp
    def get_footage_link(self, timestamp: int) -> str:
        """
        Get a link to footage for an epoch timestamp
        Parameters
        ----------
        timestamp: Int of epoch timestamp to get footage for

        Returns
        -------
        A string of the link to the footage
        """
        footage_resp = self._session.get(self.cam_url + f"/history/{timestamp}")
        try:
            footage_resp.raise_for_status()
        except HTTPError:
            return ""
        return footage_resp.json()["url"]

    @set_default_timestamp
    def get_thumbnail(self, timestamp: int) -> str:
        """
        Gets the thumbnail for an epoch time
        Parameters
        ----------
        timestamp: Epoch time to get a thumbnail for

        Returns
        -------
        A url of the thumbnail
        """
        thumbnail_resp = self._session.get(self.cam_url + f"/thumbnail/{timestamp}")
        try:
            thumbnail_resp.raise_for_status()
        except HTTPError:
            return ""
        return thumbnail_resp.json()["url"]

    def __str__(self):
        return f"Verkada Camera {self.name}"

    def __repr__(self):
        return f"Verkada Camera {self.name}"

    # Properties

    @cached_property
    def id(self) -> str:
        """The camera ID"""
        return self._info["camera_id"]

    @cached_property
    def last_online(self) -> int:
        """Epoch time of when the camera was last online"""
        return self._info["last_online"]

    @cached_property
    def cloud_retention(self) -> str:
        """The amount of days of cloud retention"""
        return self._info["cloud_rentention"]

    @cached_property
    def date_added(self) -> int:
        """The epoch time when the camera was added to Command"""
        return int(self._info["date_added"])

    @cached_property
    def device_retention(self) -> int:
        """The amount days of storage on the camera"""
        return int(self._info["device_retention"])

    @cached_property
    def firmware(self) -> bool:
        """A bool the firmware is up to date."""
        return self._info["firmware"] == "Up to date"

    @cached_property
    def IP(self) -> str:
        """The IP of the camera. Likely a private IP"""
        return self._info["local_ip"]

    @cached_property
    def location(self) -> str:
        """The street address of the camera"""
        return self._info["location"]

    @cached_property
    def MAC(self) -> str:
        """The MAC address of the camera"""
        return self._info["mac"]

    @cached_property
    def model(self) -> str:
        """Returns the model of the camera"""
        return self._info["Model"]

    @cached_property
    def name(self) -> str:
        """Returns the name of the camera"""
        return self._info["name"]

    @cached_property
    def serial(self) -> str:
        """Returns the serial number of the camera"""
        return self._info["serial"]

    @cached_property
    def site(self) -> str:
        """Returns the site that the camera is in"""
        return self._info["site"]

    @cached_property
    def status(self) -> str:
        """The status of the camera"""
        return self._info["status"]
