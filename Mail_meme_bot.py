import os
import random
from MemeScraper import main as ms_main
from memeDownloader import main as md_main, base_directory
from Send import main as s_main

def choose_meme():
    img_folder = base_directory()
    #makes a list of all files in the directory
    files = os.listdir(img_folder)
    index = random.randrange(0,len(files))
    #joins base dir to path of image
    img_path = os.path.join(img_folder,files[index])
    return img_path,files[index]

def main():
    #run scraper
    #ms_main
    #run downloader
    md_main
    #run meme chooser
    img_path,img_name = choose_meme()
    print(img_name)
    #send email
    print("sending mail")
    flag = s_main(img_name,img_path)
    print(flag)


if __name__ == "__main__":
    main()