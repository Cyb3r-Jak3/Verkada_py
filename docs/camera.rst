Camera
++++++

``Camera`` class represents a camera in a organization. The api is only capable of retrieving information for the camera and can not make any changes. It has functions for getting links to footage thumbnails from the camera.

Camera example: ::

    from verkada_py import Organization
    org = Organization(org_id="test",api_key="test")
    camera = org.cameras[0]

    # Camera Attributes
    camera.id: str -> Camera ID. Used for getting footage and thumbnails
    camera.last_online: int -> Epoch time of when the camera was last online
    camera.cloud_retention: int -> Amount of cloud storage days for the camera
    camera.date_added: int -> Epoch time of when the camera was added to Command
    camera.device_retention: int -> Amount of local storage days for the camera
    camera.firmware: bool -> If the camera firmware is up to date
    camera.IP: str -> Camera's local IP address
    camera.location: str -> Camera's street address
    camera.MAC: str -> Camera's MAC address
    camera.model: str -> Model of the camera
    camera.name: str -> Name of the camera
    camera.serial: str -> Serial number of the camera
    camera.site: str -> Name of the site the camera is in
    camera.status: str -> Status of the camera

    # Get number of detected people and vehicle between two times
    object_results = camera.get_object_count(start_time=100, end_time=200)
    print(object_results)
    # {"people": 100, "vehicles": 5}

    # Get a link to footage
    footage_link = camera.get_footage_link(200)
    print(footage_link)
    # "https://command.verkada.com/cameras/<camera.id>/history/86400/1589007600/?duration=86400&initialVideoTime=1589007600000"

    # Get a link to a thumbnila
    thumbnail_link = camera.get_thumbnail_link(200)
    print(thumbnail_link)
    # "https://verkada-video-staging-us-west-2.s3.amazonaws.com/v2/5368/350618ef-37d7-45ef-bfda-4bf744206c6f-2bd115d9-b054-4cc0-b679-b2aead55ac39/574903.jpg"






