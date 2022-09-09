import requests
import json

"""Task_4.1"""
# Make an HTTP read request, save the result to a file
response_get = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data_json = response_get.json()

with open('requests/response.json', 'w') as file_json:
    json.dump(data_json, file_json, indent=4)

print(f'{data_json = }')
print(f'{response_get.ok = }')


"""Task_4.2"""
# Read the information from the file and make an HTTP request to save
with open('requests/response.json', 'r') as read_response_json:
    data_response_json = json.load(read_response_json)

status_put = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=data_response_json)

print(f'{data_response_json = }')
print(f'{status_put.ok = }')


"""Task_4.3"""
# Come up with some more tasks, practice with the module
# 1
status_wiki = requests.get('https://en.wikipedia.org/wiki/Main_Page')

print(f'User-Agent = {status_wiki.request.headers["User-Agent"]}')

# 2
status_wiki_txt = status_wiki.text

with open('requests/status_wiki.html', 'w', encoding='utf-8') as wiki_html:
    wiki_html.write(status_wiki_txt)


"""Task_5"""
# Download any picture from the Internet, save it
response_picture = requests.get('https://img-9gag-fun.9cache.com/photo/a0R8EbQ_460s.jpg')

with open('requests/img.jpg', 'wb') as picture:
    picture.write(response_picture.content)
