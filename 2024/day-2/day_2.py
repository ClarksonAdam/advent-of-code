def extract_reports_from_file(filepath):
    with open(filepath, "r") as file:
        return [[int(level) for level in line.strip().split(" ")] for line in file]


def is_ascending_or_descending(report):
    is_ascending = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    if not (is_ascending or is_descending): return False
    else: return True


def has_valid_difference(report):
    return all(0 < abs(report[l] - report[l + 1]) < 4 for l in range(len(report) - 1))


def is_report_safe(report):
    return is_ascending_or_descending(report) and has_valid_difference(report)


def evaluate_reports(reports):
    safe, unsafe = 0, 0
    for report in reports:
        if is_report_safe(report):
            safe += 1
        else:
            unsafe += 1
    return safe, unsafe


def evaluate_reports_with_removal(reports):
    safe_reports, unsafe_reports = 0, 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
        else:
            safe_levels, unsafe_levels = 0, 0
            for i in range(len(report)):
                temp_report = report.copy()
                del temp_report[i]
                if is_report_safe(temp_report):
                    safe_levels += 1
                else:
                    unsafe_levels += 1
            if safe_levels == 0: unsafe_reports += 1
            elif safe_levels >= 1: safe_reports += 1

    return safe_reports, unsafe_reports


reports = extract_reports_from_file("day_2_input.txt")

# Task 1
safe_reports_task_1, unsafe_reports_task_1 = evaluate_reports(reports)
print(f"Task 1. Safe reports: {safe_reports_task_1}. "
      f"Unsafe reports: {unsafe_reports_task_1}. "
      f"Total: {safe_reports_task_1 + unsafe_reports_task_1}")

# Task 2
safe_reports_task_2, unsafe_reports_task_2 = evaluate_reports_with_removal(reports)
print(f"Task 2. Safe reports: {safe_reports_task_2}. "
      f"Unsafe reports: {unsafe_reports_task_2}. "
      f"Total: {safe_reports_task_2 + unsafe_reports_task_2}")