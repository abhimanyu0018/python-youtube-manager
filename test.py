import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []        

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def listAllVideos(videos):
   print("----------------- List of all youtube videos ----------------- \n")
   for index,video in enumerate(videos,start=1):
       print(f"{index}. {video['name']}, Duration: {video['time']}")
   print("\n------------------------------------------------------------ \n")

def addVideo(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name,'time': time})
    save_data_helper(videos)
    
def updateVideo(videos):
    listAllVideos(videos)
    
    index = int(input("Enter the video index:"))

    if index >= 1 <= len(videos):
        name = input("Enter video name:")
        time = input("Enter video duration:") 
        videos[index - 1 ] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid selected index") 


def deleteVideo(videos):
    listAllVideos(videos)

    index = int(input("Enter the video index you want to delete:"))

    if index >= 1 <= len(videos):
        videos.pop(index -1)
        save_data_helper(videos)
    else:
        print("Invalid selected index") 

def main():
    videos = load_data()
    while True: 

        print("\n YouTube Manager | Choose an option:")

        print("1. List all youtube videos ")
        print("2. Add a youtube video")
        print("3. Update a youtube video in details")
        print("4. Delete a youtube video")
        print("5. Exit the App \n")
    
        choice = input()
        print("\n")

        match choice:
            case "1":
                listAllVideos(videos)
            
            case "2":
                addVideo(videos)

            case "3":
                updateVideo(videos)
            
            case "4":
                deleteVideo(videos)
            
            case "5":
                break

            case _:
                print("Invaild Choice")


if __name__ == "__main__":
    main()