from app.posts.models import User
from math import sin, cos, sqrt, atan2, radians
from app import db
import queue

# create a PriorityQueue object
pq = queue.PriorityQueue()

def create_post(text, latitude, longitude):
    post = User(text=text, latitude=latitude, longitude=longitude)
    db.session.add(post)
    db.session.commit()
    return post

min_heap = []
def get_posts(latitude,longitude):
    users = User.query.all()
   
    for user in users:
        userlat = user.latitude
        userlong = user.longitude
        d = get_distance(latitude,longitude,userlat,userlong)
        pq.put((d,user))

 
    sorted_data = []
    cnt = 0
    while not pq.empty():
        if(cnt < 10):
            item = pq.get()
            sorted_data.append(item[1])
            cnt = cnt+1
        else:
            break
        

    return sorted_data

def get_distance(latitude1,longitude1,latitude2,longitude2):
    R = 6373.0
    lat1 = radians(latitude1)
    lon1 = radians(longitude1)
    lat2 = radians(latitude2)
    lon2 = radians(longitude2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

