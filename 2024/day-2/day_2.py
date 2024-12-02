def extract_reports_from_file(filepath):
    with open(filepath, "r") as file:
        return [[int(level) for level in line.strip().split(" ")] for line in file]


def check_is_report_safe(report):
    #check that the arrays are ascending or descending
    is_ascending = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    if not (is_ascending or is_descending): return False

    # Check that the difference between numbers is correct
    return all(0 < abs(report[l] - report[l + 1]) < 4 for l in range(len(report) - 1))

def count_safe_and_unsafe_reports(reports):
    safe_reports = 0
    not_safe_reports = 0
    for report in reports:
        if check_is_report_safe(report):
            safe_reports += 1
        else:
            not_safe_reports += 1
    return safe_reports, not_safe_reports

reports = extract_reports_from_file("day_2_input.txt")

# Task 1
safe_reports, not_safe_reports = count_safe_and_unsafe_reports(reports)
print(f"Task 1. Safe reports: {safe_reports}. "
      f"Not safe reports: {not_safe_reports}. "
      f"Total: {safe_reports + not_safe_reports}")