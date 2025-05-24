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


def load_users_from_json(filepath='users.json'):
    with open(filepath, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    users = load_users_from_json()

    filtered_users = filter_by_age(users, min_age=18, max_age=30)
    print("Gefilterte User (25-30 Jahre):")
    for user in filtered_users:
        print(user)