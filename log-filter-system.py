# System log event filter project

# A simple list of server alerts to inspect
server_events = [
    "[INFO] user logged in successfully.",
    "[WARNING!] high memory usage detected.",
    "[ERROR!] Database connection failed!",
    "[INFO] File uploaded to main branch.",
    "[ERROR!] Security handshake timeout.",
]


def clear_and_filter_logs(log_list):
    print("Initializing log security Scan....")
    error_count = 0
    warning_count = 0

    # Scanning each log entry one by one
    for index, log in enumerate(log_list):
        if "[ERROR!]" in log:
            print(f"Alert at index {index}: Found a system failure!")
            error_count += 1
        elif "[WARNING!]" in log:
            print(f"Alert at index {index}: Found a non-critical risk warning.")
            warning_count += 1

    print("\nDiagnostic scan summary....")
    print(f"Total errors spotted: {error_count}")
    print(f"Total risk warnings spotted: {warning_count}")

clear_and_filter_logs(server_events)



