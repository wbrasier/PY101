def greetings(names, job):
    return (f'Hello, {" ".join(names)}! '
    f'Nice to have a {job["title"]} {job["occupation"]} around.')


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.