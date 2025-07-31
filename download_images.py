import multiprocessing
import concurrent.futures
import requests

def downloadFile(url,name):
    print(f"Downloading start {name}")
    response=requests.get(url)

    open(f"filesformultiprocessing/file{name}.jpg","wb").write(response.content)
    print(f"Downloading end {name}")
def main():
    url="https://picsum.photos/2000/3000"
    # pros=[]
    # for i in range(50):
    # # downloadFile(url,i)
    #     p=multiprocessing.Process(target=downloadFile,args=[url,i])
    #     p.start()
    #     pros.append(p) #this add in pros=[] in this list

    # for p in pros:
    #     p.join()
#above can also be done ///////////////////////////////////////////////////
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1=[url for i in range(60)]
        l2=[i for i in range(60)]

        results=executor.map(downloadFile,l1,l2)
        for r in results:
           print(r)


if __name__ == "__main__":
    main()