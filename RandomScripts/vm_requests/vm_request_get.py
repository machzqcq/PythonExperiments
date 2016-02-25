import requests,json



my_vmid_response = requests.get('"})

print(my_vmid_response.status_code)
print(json.loads(my_vmid_response.text))






