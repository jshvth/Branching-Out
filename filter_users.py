import json

def filter_by_age(users, min_age, max_age):
    """
    Filtert eine Liste von Usern nach Altersbereich.
    """
    filtered = []
    for user in users:
        age = user.get('age')
        if age is None:
            continue
        if min_age is not None and age < min_age:
            continue
        if max_age is not None and age > max_age:
            continue
        filtered.append(user)
    return filtered


def filter_by_email(users, email_substring):
    """
    Filtert User nach E-Mail-Substring (case-insensitive).
    """
    email_substring = email_substring.lower()
    return [user for user in users if email_substring in user.get('email', '').lower()]


def load_users_from_json(filepath='users.json'):
    with open(filepath, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    users = load_users_from_json()

    # Beispiel: Filter nach Alter 25-30
    filtered_by_age = filter_by_age(users, min_age=25, max_age=30)
    print("Gefilterte User nach Alter (25-30):")
    for user in filtered_by_age:
        print(user)

    # Beispiel: Filter nach Email mit "example"
    filtered_by_email = filter_by_email(users, 'example')
    print("\nGefilterte User nach Email mit 'example':")
    for user in filtered_by_email:
        print(user)