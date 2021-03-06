camera_response = {
    "cameras": [{
        "camera_id": "8438a7f2-fdbc-4392-8b9b-d47513bcf5c8",
        "cloud_rentention": 30,
        "date_added": 90,
        "device_retention": 30,
        "firmware": "Up to date",
        "local_ip": "192.168.0.1",
        "location": "cloud",
        "mac": "C9-67-EB-8D-BA-E3",
        "Model": "CD41",
        "name": "API MOCK Camera",
        "serial": "E38D-BAEB-67C8",
        "site": "API MOCK Site",
        "last_online": 200,
        "status": "Live"
        }
    ]
}
camera_object_response = {
    "object_counts": [
        {
            "people_count": 1,
            "detected_time": 1595287853,
            "vehicle_count": 0
        },
        {
            "people_count": 8,
            "detected_time": 1595287872,
            "vehicle_count": 4
        }
    ],
    "page_cursor": "go_to_two"
}

camera_object_response_two = {
    "object_counts": [
        {
            "people_count": 2,
            "detected_time": 1595287853,
            "vehicle_count": 0
        },
        {
            "people_count": 8,
            "detected_time": 1595287872,
            "vehicle_count": 4
        }
    ],
    "page_cursor": None
}

notification_response = {
    "notifications": [
        {
            "notification_type": "person_of_interest",
            "camera_id": "8438a7f2-fdbc-4392-8b9b-d47513bcf5c8",
            "crowd_threshold": None,
            "objects": [],
            "person_label": "API DUMMY",
            "created": 156156156,
            "video_url": "https://www.google.com/video",
            "image_url": "https://www.google.com/image"
        }
    ],
    "page_cursor": "go_to_two"
}

notification_pagination_response = {
    "notifications": [
        {
            "notification_type": "motion",
            "camera_id": "8438a7f2-fdbc-4392-8b9b-d47513bcf5c8",
            "crowd_threshold": None,
            "objects": [],
            "person_label": None,
            "created": 156156157,
            "video_url": "https://www.google.com/video",
            "image_url": "https://www.google.com/image"
        }
    ],
    "page_cursor": None
}

get_person_of_interest = {
    "persons_of_interest": [
        {
            "label": "API DUMMY",
            "person_id": "078bffa7-20cf-4307-a047-29e98b340e8e",
            "created": 156156156,
            "last_seen_camera_id": "8438a7f2-fdbc-4392-8b9b-d47513bcf5c8",
            "last_seen": 1561561565
        }
    ]
}
create_person_of_interest = {
    "label": "API DUMMY",
    "person_id": "078bffa7-20cf-4307-a047-29e98b340e8e"
}

footage_link_response = {
    "url": "https://command.verkada.com/footage"
}

time_response = {
    "url": "https://command.verkada.com/footage/default_time"
}

thumbnail_link_response = {
    "url": "https://command.verkada.com/thumbnail"
}