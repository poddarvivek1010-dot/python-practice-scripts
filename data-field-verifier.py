 # User Profile Data Validator (Dictionaries & sets)

# list of user profiles to check
user_profiles = [
    {"user_id": "u101", "name": "Vivek", "days_active": 8, "status": "Active"},
    {"user_id": "u102", "name": "Rahul", "days_active": 45, "status": "Inactive"},
    {"user_id": "error_id", "name": "Aman", "days_active": -5, "status": "Active"},
    {"user_id": "u104", "name": "Siddharth", "days_active": 12, "status": "Pending"},
]


def validate_profiles(profiles_list):
    print("Starting Data Integrity Check....")
    all_clear = True


    for index, user in enumerate(profiles_list):
        is_id_valid = user["user_id"].startswith("u")   #User ID must start with a small 'u'
        are_days_valid = user["days_active"] >= 0  # Days active must be a positive number
        is_status_valid = user["status"] in ("Active", "Inactive")  # Status must be either 'Active' or 'Inactive'

        # If any rule fails then log the specific error
        if not is_id_valid:
            print(f"Error at position {index}: Bad User ID format '{user['user_id']}'")
            all_clear = False

        if not are_days_valid:
            print(f"Error at position {index}: Days active cannot be negative ({user['days_active']})")
            all_clear = False

        if not is_status_valid:
            print(f"Error at position {index}: Invalid status option '{user['status']}'")
            all_clear = False

    # overall result checking
    if all_clear:
        print("\nSuccess: All profile records are perfectly valid!")
    else:
        print("\nFailure: Data errors detected in the profile list.")

validate_profiles(user_profiles)


