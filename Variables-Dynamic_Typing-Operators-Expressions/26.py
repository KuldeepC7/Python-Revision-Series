# 26. You are validating JSON payloads for a strict FastAPI endpoint. Write a single expression that verifies a payload variable is exactly a standard dictionary (and not a custom subclass of a dictionary) by checking its type directly against type({}) instead of using isinstance().

json_payload = {
    'a': {}
}

dictionary_or_not = (type(json_payload) == type({}))
print(dictionary_or_not)