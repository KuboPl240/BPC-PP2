import requests
from HttpHandler import HttpRequestHandler
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}

#1
print("-----1-----")
response = requests.get(url, params=params)

if response.status_code == 200:
    posts = response.json()  
    print(f"Number of posts returned: {len(posts)}")  
else:
    print(f"Failed to fetch posts. Status code: {response.status_code}")


#2
print("-----2-----")
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "My New Post",
    "body": "This is the body of my new post.",
    "userId": 1
}
response = requests.post(url, json=payload)

if response.status_code == 201:  
    response_data = response.json()  
    print(f"Status Code: {response.status_code}")
    print(f"Created Post ID: {response_data.get('id')}")
else:
    print(f"Failed to create the post. Status code: {response.status_code}")


#3
print("-----3-----")
def fetch_comments(post_id):
    url = "https://jsonplaceholder.typicode.com/comments"
    post_id = 1
    params = {"postId": post_id}
    total_comments = []

    response = requests.get(url, params=params)
    if response.status_code == 200:
        comments = response.json()
        total_comments.extend(comments)
    else:
        print(f"Failed to fetch comments. Status code: {response.status_code}")
        return
    print(f"Total number of comments fetched for postId={post_id}: {len(total_comments)}")

fetch_comments(1)

#4
print("-----4-----")
handler = HttpRequestHandler()
get_url = "https://jsonplaceholder.typicode.com/posts/1"
get_result = handler.get(get_url)
print("GET Request Test:", get_result)

post_url = "https://jsonplaceholder.typicode.com/posts"
post_data = {"title": "foo", "body": "bar", "userId": 1}
post_result = handler.post(post_url, post_data)
print("POST Request Test:", post_result)