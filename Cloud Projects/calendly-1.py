import requests

uri1 = 'https://api.calendly.com/users/me'


token = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzc1MzE3NjE4LCJqdGkiOiI4NTNkYjBmZC03MDMzLTRhNjUtYThjYi1hMWFhODk2MTJhN2EiLCJ1c2VyX3V1aWQiOiJiM2VkZjgyMC0xMDIzLTQxMzMtODkxMS1jMmJmM2Q5Yjk1ODkiLCJzY29wZSI6ImF2YWlsYWJpbGl0eTpyZWFkIGF2YWlsYWJpbGl0eTp3cml0ZSBldmVudF90eXBlczpyZWFkIGV2ZW50X3R5cGVzOndyaXRlIGxvY2F0aW9uczpyZWFkIHJvdXRpbmdfZm9ybXM6cmVhZCBzaGFyZXM6d3JpdGUgc2NoZWR1bGVkX2V2ZW50czpyZWFkIHNjaGVkdWxlZF9ldmVudHM6d3JpdGUgc2NoZWR1bGluZ19saW5rczp3cml0ZSBncm91cHM6cmVhZCBvcmdhbml6YXRpb25zOnJlYWQgb3JnYW5pemF0aW9uczp3cml0ZSB1c2VyczpyZWFkIGFjdGl2aXR5X2xvZzpyZWFkIGRhdGFfY29tcGxpYW5jZTp3cml0ZSBvdXRnb2luZ19jb21tdW5pY2F0aW9uczpyZWFkIHdlYmhvb2tzOnJlYWQgd2ViaG9va3M6d3JpdGUifQ.BNeE55gU8lCGZvTzta9g5ZLJTtCkChnvZGNG-D0DSUdgyxw-cYi9alePW4Z465wAHsdogzmdDfczubieirOMTg'
headers = {'Authorization': f'Bearer {token}'}


# print(response.json().get('resource', {}).get('current_organization'))
def get_org_id():
    response = requests.get(uri1, headers = headers)
    return response.json().get('resource', {}).get('current_organization')

org_id = get_org_id()
print(org_id)
# print(event_types)

uri2 = "https://api.calendly.com/event_types?organization="f"{org_id}"
response = requests.get(uri2, headers=headers)
event_types = response.json().get('collection')
print("-----------------------------")
print("-----------------------------")
print(event_types)
print("-----------------------------")
for event_type in event_types:
    url = "https://api.calendly.com/scheduled_events?event_type={event_type}&organization="f"{org_id}"
    response = requests.get(url=url, headers=headers)
    print(response.json().get('collection'))
    print("-----------------------------")
    for event in response.json().get('collection'):
        print(event)