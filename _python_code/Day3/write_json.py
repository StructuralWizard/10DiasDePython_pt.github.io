import json

# Converte dict para JSON 1
with open('data1.json', 'w') as f:
    json.dump({"name": "Alice"}, f)

# Converte dict para JSON 2
# Serializa para JSON
json_string = json.dumps({"name": "Alice"})

# Desserializa de JSON
data = json.loads(json_string)

# Salva em arquivo
with open("data2.json", "w") as f:
    json.dump(data, f, indent=4)

# Lê arquivo JSON
with open('data2.json') as f:
    data = json.load(f)
    print(data['name'])
