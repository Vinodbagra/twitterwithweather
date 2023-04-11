from app.posts.models import User
from math import sin, cos, sqrt, atan2, radians
from app import db

def create_post(text, latitude, longitude):
    post = User(text=text, latitude=latitude, longitude=longitude)
    db.session.add(post)
    db.session.commit()
    return post

distancelist = []
def get_posts(latitude,longitude):
    users = User.query.all()
   
    for user in users:
        userlat = user.latitude
        userlong = user.longitude
        d = get_distance(latitude,longitude,userlat,userlong)
        distancelist.append((d,user))

    distancelist.sort()
    sorted_data = []
    for x in distancelist:
        sorted_data.append(x[1])
        
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

