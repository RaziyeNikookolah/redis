from redis import Redis
import json

redis_host = "127.0.0.1"
redis_port=6379
redis_db=0
redis_pass=""

rd=Redis(host=redis_host,port=redis_port,password=redis_pass,db=redis_db)

# rd.set("name","razye")
# print(rd.get("name"))
# print(rd.client_list())

with open("persons.json") as file:
    data=json.load(file)

with rd.pipeline(data) as pip:
    for id,person in enumerate(data):
        pip.hsetnx("persons",id,str(person))
    pip.execute()