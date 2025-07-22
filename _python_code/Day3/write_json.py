import json

# Convert dict to JSON 1
with open('data1.json', 'w') as f:
    json.dump({"name": "Alice"}, f)

# Convert dict to JSON 2
# Serialize to JSON
json_string = json.dumps({"name": "Alice"})

# Deserialize from JSON
data = json.loads(json_string)

# Save to file
with open("data2.json", "w") as f:
    json.dump(data, f, indent=4)

# Read JSON file
with open('data2.json') as f:
    data = json.load(f)
    print(data['name'])