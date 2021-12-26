import json


def check_and_send_notification(dataset, config_path, debug: bool = False):
    f = open(config_path)
    config = json.load(f)

    notifications = []

    zips = []

    for conf in config["trigger"]:
        zips.append(conf["zip"])

    if debug:
        print(config["trigger"])
        print(zips)

    for row in dataset:
        if row[2] in zips:
            notifications.append(row)

    if notifications:
        print("SENDING NOTIFICATION", len(notifications))
