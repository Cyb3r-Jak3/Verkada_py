"""Modals for common dicts that are returned by the API"""
from cached_property import cached_property


class Notification:
    """
    Represents a Verkada notification. Used when getting notification from an organzation.
    """

    def __init__(self, info: dict):
        self._info = info

    @cached_property
    def camera_id(self) -> str:
        """
        The camera ID that the notification was generated on
        :return: ``str`` Camera ID
        """
        return self._info["camera_id"]

    @cached_property
    def crowd_threshold(self) -> [int, None]:
        """
        The amount of people detected for a crowd threshold notification
        :return: Either an ``int`` for number of people or ``None``
                if it is not a crowd notification
        """
        return self._info["crowd_threshold"]

    @cached_property
    def person_label(self) -> str:
        """
        The person label if the notification was for person of interest
        :return: ``str`` person of interest ID
        """
        return self._info["person_label"]

    @cached_property
    def notification_type(self) -> str:
        """
        The type of notification.
        Can be one of person_of_interest, tamper, crowd, motion, camera_offline, camera_online
        :return: ``str`` Type of notification
        """
        return self._info["notification_type"]

    @cached_property
    def created(self) -> int:
        """
        The time that the notification was created
        :return: ``int`` epoch time of notification
        """
        return self._info["created"]

    @cached_property
    def objects(self) -> str:
        """
        The objects that were detected by the camera. Either people or vehicles
        :return: ``str`` the objects that were detected by the camera
        """
        return self._info["objects"]

    @cached_property
    def video_url(self) -> str:
        """
        Command URL that the can be viewed to watch the footage
        :return: ``str`` URL to open in a signed-in browser
        """
        return self._info["video_url"]

    @cached_property
    def image_url(self) -> str:
        """
        URL that can be used to download an image of the notification
        :return: ``str`` image URL that can be downloaded from AWS
        """
        return self._info["image_url"]


class PersonofInterest:
    """
    Modal the represents a person on interest in an organization
    """

    def __init__(self, info: dict):
        self._info = info

    @cached_property
    def label(self) -> str:
        """
        Label for the person of interest
        :return: ``str`` The label of the person
        """
        return self._info["label"]

    @cached_property
    def person_id(self) -> str:
        """
        Person ID of the person of interest
        :return: ``str`` Person ID
        """
        return self._info["person_id"]

    @cached_property
    def created(self) -> int:
        """
        Epoch time of when the person of interest was created
        :return: ``int`` Epoch time of creation
        """
        return self._info["created"]

    @cached_property
    def last_seen_camera(self) -> str:
        """
        Camera ID that the person was last seen on
        :return: ``str`` Camera ID that the person was seen on
        """
        return self._info["last_seen_camera_id"]

    @cached_property
    def last_seen(self) -> int:
        """
        Epoch time that the person was last seen
        :return: ``int`` Epoch time that the person was last detected
        """
        return self._info["last_seen"]
