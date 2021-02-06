camera_response = {
    "cameras": [{
        "camera_id": "rzabvxfk-7a67-zc4lm-8p0v-k23mi9houom3g68",
        "cloud_rentention": "30 Days",
        "date_added": 90,
        "device_retention": "30 Days",
        "firmware": "latest",
        "local_ip": "192.168.0.1",
        "location": "cloud",
        "mac": "C9-67-EB-8D-BA-E3",
        "Model": "CD41",
        "name": "API MOCK Camera",
        "serial": "E38D-BAEB-67C8",
        "site": "API MOCK Site",
        }
    ]
}

notification_response = {
    "notifications": [
        {
            "notification_type": "person_of_interest",
            "camera_id": "rzabvxfk-7a67-zc4lm-8p0v-k23mi9houom3g68",
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
            "camera_id": "rzabvxfk-7a67-zc4lm-8p0v-k23mi9houom3g68",
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
            "person_id": "86g3mouo-h9im-32kv-0p8m-l4cz76a7kfxvbazr",
            "created": 156156156,
            "last_seen_camera_id": "rzabvxfk-7a67-zc4lm-8p0v-k23mi9houom3g68",
            "last_seen": 1561561565
        }
    ]
}
create_person_of_interest = {
    "label": "API DUMMY",
    "person_id": "86g3mouo-h9im-32kv-0p8m-l4cz76a7kfxvbazr"
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