import csv


COMMIT_FILES = 5


data = []
i = 0
while i < COMMIT_FILES:
    i += 1
    with open(f"./commit{i}.diff") as diff_file:
        code_diff = ""
        for line in diff_file:
            code_diff += line.strip().replace("\n", "") + "\\n"
        code_diff = code_diff.replace(",", "<comma-char>")
        split_data = code_diff.split("\\n", 1)
        data += [[split_data[0], split_data[1]]]

with open("dataset.csv", "w") as csv_file:
    fields = ["input_ids", "labels"]
    writer=csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    for datum in data:
        writer.writerow({"input_ids": datum[0], "labels": datum[1]})
