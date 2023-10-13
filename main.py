# Day37 API Post and Habit Tracker
import requests
import datetime as dt


USERNAME = "ebusch01"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": USER_TOKEN
}

pixela_user_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": "",
#     "username": "ebusch01",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# user_response = requests.post(url=pixela_user_endpoint, json=user_params)
# print(user_response.text)

graph_params = {
    "id": "graph1",
    "name": "Studying Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}

pixela_graph_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs"
graph_response = requests.post(headers=headers, url=pixela_graph_endpoint, json=graph_params)
# print(graph_response.text)

print("How many hours did you study today? ")
hours_studied = input()

today = dt.datetime.now().strftime("%Y%m%d")
print(today)
pixel_params = {
    "date": today,
    "quantity": hours_studied,
}

pixela_pixel_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_response = requests.post(headers=headers, url=pixela_pixel_endpoint, json=pixel_params)
print(pixel_response.text)
#
# # put practice
# print("How many hours did you REALLY study today? ")
# hours_studied = input()
#
# put_params = {
#     "quantity": hours_studied
# }
#
# pixela_pixel_edit_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# put_response = requests.put(headers=headers, url=pixela_pixel_edit_endpoint, json=put_params)
# print(put_response.text)
# # delete practice
# print("Deleting which days hours(yyyyMMdd)?")
# date = input()
#
# del_pixel_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# del_response = requests.delete(headers=headers, url=pixela_pixel_endpoint)
# print(del_response.text)
