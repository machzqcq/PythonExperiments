import requests,json



my_vmid_response = requests.get('https://pwslvracp001.inmar.com/catalog-service/api/consumer/resources/?$filter=request/requestNumber+eq+508', verify=False, headers={"Content-Type":"application/json","Authorization":"Bearer MTQzNTIzNTUxNzg3OTo2YWI5MGJlN2RjYTFmNDZlZTYwMTp0ZW5hbnQ6dnNwaGVyZS5sb2NhbHVzZXJuYW1lOmlubVxwbWFjaGFybDo4OTQwNzA1MTM0Njk3MGFmY2UyMzExNGRjYTNlN2E3YTE2ZWY0MTNkNjY2YTllNzgxN2VkMWI4ZjBmZjM4NTFhNTEzMjIxMGMwZDI3ZDhhNTI5NmM2NGJiYTllMmI0MWUwOGFhNDlmMWYyMTQxZjhlNGIzYTM2YTY4MWQwOWIxOA=="})

print(my_vmid_response.status_code)
print(json.loads(my_vmid_response.text))






