import requests
import sys
import time

def downloadFile(url, directory) :
  localFilename = url.split('/')[-1]
  with open(directory + '/' + localFilename, 'wb') as f:
    start = time.clock()
    r = requests.get(url, stream=True)
    total_length = r.headers.get('content-length')
    dl = 0
    if total_length is None: # no content length header
      f.write(r.content)
    else:
      for chunk in r.iter_content(1024):
        dl += len(chunk)
        f.write(chunk)
        done = int(50 * dl / total_length)
        sys.stdout.write("\r[%s%s] %s bps" % ('=' * done, ' ' * (50-done), dl//(time.clock() - start)))
        print ('') 
  return (time.clock() - start)

def main() :
  if len(sys.argv) > 1 :
        url = sys.argv[1]
  else :
        url = raw_input("Enter the URL : ")
  directory = raw_input("Where would you want to save the file ?")

  time_elapsed = downloadFile(url, directory)
  print ("Download complete...") 
  print ("Time Elapsed: " + time_elapsed) 


if __name__ == "__main__" :
  main()




downloadFile('https://img1.looper.com/img/gallery/the-untold-truth-of-naruto/intro-1566998687.jpg', '/storage/sdcard0/pydown/') 