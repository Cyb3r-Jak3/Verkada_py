Organization
++++++++++++

``Organization`` class represents a Verkada organization. It will contain a list of Cameras in the organization. It has functions for getting notifications and handling person of interest.

Organization Example: ::

    from verkada_py import Organization
    org = Organization(org_id="test",api_key="test")

    print(org.cameras)
    # ["API Example Camera 1", "API Example Camera 2",...]

    # Get notifications from an organization
    notifications = org.get_notifications(start_time=100, end_time=200)
    print(notifications)
    # [ {"camera_id": "...",...}, {"camera_id": "...",...}, ...]

    # Get all people of interest
    people = org.get_poi()
    print(people)
    # [{"person_id": "", "label": "", ...}, ...]

    # Create a person of interest
    new_person = org.create_poi(image="/path/to/image")
    print(new_person)
    # "078bffa7-20cf-4307-a047-29e98b340e8e"

    # Updates a label for a person of interest
    org.update_poi(person_id: new_person, label="API Example")

    # Deletes a person of interest
    org.delete_poi(person_id: new_person)

