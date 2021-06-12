import os
import json

dir_content = os.listdir(".")
json_files = [file for file in dir_content if file.endswith("json")]
count = 0

csv = open("./summary.csv", "w")
csv.write("username, posts, followers, following\n")

for doc in json_files:
    with open(doc, "r") as json_file:
        try:
            content = json.loads(json_file.read())
            user = content["graphql"]["user"]
            username = user["username"]
            posts = user["edge_owner_to_timeline_media"]["count"]
            followers = user["edge_followed_by"]["count"]
            following = user["edge_follow"]["count"]

            csv.write(f"{username}, {posts}, {followers}, {following}\n")
            count += 1
            # print(f"{username}, {posts}, {followers}, {following}\n")

        except json.decoder.JSONDecodeError as error:
            print("Could not read file. Error: ", error)

csv.close()
print("Processed", count, "of", len(json_files), "json files")
