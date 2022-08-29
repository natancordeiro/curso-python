import json

with open('abc.json', 'r') as file: 
    d1_json = file.read()

    # convertendo o JSON para dicionário 
    d1_json = json.loads(d1_json)

# indentando sobre os valores
for key, value in d1_json.items():
    print(key)
    for k1, v1 in value.items():
        print(k1, v1)
