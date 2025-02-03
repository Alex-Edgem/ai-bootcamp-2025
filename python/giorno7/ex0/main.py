import csv
from fileinput import close

# data = []
# with open("data.csv") as fd:
#     reader = csv.reader(fd)
#     for line in reader:
#         data.append(line)
#     head = data[0]
#     body = data[1:]
#     sorted_data = sorted(body, key =lambda x: x[1])
#
#     idx = 1
#     for s in sorted_data:
#         s.insert(0, f"{idx}")
#         idx += 1
#         print(s)



with open("data.csv") as fd:
    reader = csv.reader(fd)
    head = next(reader)
    sorted_data = sorted(reader, key =lambda x: (x[1],x[0]))
    print(sorted_data)
    for k, v in enumerate(sorted_data):
        # head.append(v)
        v.insert(0, f"{k + 1}")
        print(v)

with open("data_output.csv", "w") as fd:
    writer = csv.writer(fd)
    writer.writerow(head)
    writer.writerows([s[1:] for s in sorted_data])