import os
import time
import hashlib
import sys
import json

base_url = "http://dc-sitf-ail/gallery/"

def generate_images():
    images = []
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            name = dir
            locale = "en-US"
            publisher = "Draper"
            lastUpdated = time.strftime("%Y-%m-%dT%TZ", time.localtime())
          
            for root, dirs, files in os.walk('./'+dir):
                for file in files:
                    uri = base_url+dir+'/'+file 
                    hash = "sha256:" + sha256_checksum(dir+'/'+file)
                    f = {"uri":uri, "hash":hash}
                        
                    if "disk" in file:
                        disk = f
                    elif "logo" in file:
                        logo = f
                    elif "symbol" in file:
                        symbol = f
                    elif "thumbnail" in file:
                        thumbnail = f
                    elif "description" in file:
                        with open(dir+'/description.txt', 'r') as myfile:
                            description = myfile.readlines()
                    elif "version" in file:
                        with open(dir+'/version.txt', 'r') as myfile:
                            version=myfile.read().replace('\n', '')
                    elif "details" in file:
                        with open(dir+'/details.json') as myfile:
                            details = json.load(myfile)

            image = {
                "name":name,
                "version":version,
                "locale":locale,
                "publisher":publisher,
                "lastUpdated":lastUpdated,
                "description":description,
                "disk":disk,
                "logo":logo,
                "symbol":symbol,
                "thumbnail":thumbnail,
                "details":details
                }           
            images.append(image)
    return images


def sha256_checksum(filename, block_size=65536):
    print("HASHING - "+filename)
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


if __name__ == "__main__":
    print("Starting...")
    images = generate_images()
    gallery = {"images":images}

    with open('gallery.json', 'w') as outfile:
        json.dump(gallery, outfile)

    print("Success!")
