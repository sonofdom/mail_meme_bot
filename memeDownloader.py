# All libraries required
import os
import requests

#in seperate def so can be called for meme_bot
def base_directory():
    #establishes downloads folder
    #finds path of dir
    THIS_FILE_PATH = os.path.abspath(__file__)
    #sets base_dir 
    BASE_DIR = os.path.dirname(THIS_FILE_PATH)
    #joins memes folder to base_dir gives a full path
    MEME_DOWNLOADS = os.path.join(BASE_DIR,"Meme_Downloads")
    #This makes the folder
    os.makedirs(MEME_DOWNLOADS,exist_ok=True)
    return MEME_DOWNLOADS


def url_list():
    url_list = []
    with open("memeUrl.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            url_list.append(str(line.strip()))   
    return url_list

def download_img(url_list,MEME_DOWNLOADS):
    for i,x in enumerate(url_list):
        #names file
        fname = f"Meme{i}.jpeg"
        #gives the path of the file meme_downloads + file name
        file_path = os.path.join(MEME_DOWNLOADS,fname)
        #skips file if image already collected
        if os.path.exists(file_path):
            print(f"skipped {fname}")
            continue
        #gets url and ensure it is available
        with requests.get(x) as r:
            #print(x)
            if r.status_code == 200:
                with open(file_path,"wb") as f_image:
                    f_image.write(r.content)
                    print("image obtained")
            else:
                print("Image not available")

def main():
    MEME_DOWNLOADS = base_directory()
    list_of_url = url_list()
    download_img(list_of_url,MEME_DOWNLOADS)

if __name__ == "__main__":
    main()
