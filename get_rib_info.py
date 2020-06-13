import os.path
import urllib.request

def get_rib_info():

    url = 'http://archive.routeviews.org/oix-route-views/oix-full-snapshot-latest.dat.bz2'
    filename = url.split("/")[-1]
    file_unzip = '.'.join(filename.split('.')[:-1])
 
    if not os.path.exists(file_unzip):
        print("Downloading latest BGP data from http://routeviews.org")
        u = urllib.request.urlopen(url)
        file_size = u.info()["Content-Length"]
        print(f"Downloading: {filename} Bytes: {file_size}  ........Please wait\n")

        urllib.request.urlretrieve(url, filename)
        print("Download Completed\n\nExtracting bzip")
        os.system(f"bzip2 -d {filename}")

    return file_unzip

def main():
    get_rib_info()

if __name__=="__main__":
    main()
   
