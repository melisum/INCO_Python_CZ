#!/usr/bin/env python3
import re
import operator
import csv

error = {}
per_user = {}

file = 'syslog.log'

per_user_pattern = r"ticky: (INFO|ERROR) [\w ]+.*\((\w+.?\w+)\)$"
error_pattern = r"ticky: ERROR (\w+.*) "

with open(file, "r") as f:
     """Used to open a new file """    

     for line in f:
        error_match = re.search(error_pattern, line)
        if error_match:
            error_type = error_match.group(1)
            if error_type in error:
                error[error_type] += 1
            else:
                error[error_type] = 1

error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

with open(file, "r") as f:
    for line in f:
        per_user_match = re.search(per_user_pattern, line)
        if per_user_match:
            log_type, user = per_user_match.groups()
            if user not in per_user:
                per_user[user] = {"INFO": 0, "ERROR": 0}
            per_user[user][log_type] += 1
per_user = sorted(per_user.items(), key=operator.itemgetter(0))

with open("error_message.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Error", "Count"])
    writer.writerows(error)

with open("user_statistics.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Username", "INFO", "ERROR"])

    for username, counts in per_user:
        writer.writerow([username, counts.get("INFO", 0), counts.get("ERROR", 0)])
