import dropbox
class TransferData:
    def __init__(self,accessTocken):
        self.accessTocken=accessTocken
    def uplodFile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accessTocken)
        with open(filefrom,'rb')as f:
            dbx.files_upload(f.read(),fileto)

def main():
    accessTocken='3rQmEN87qfgAAAAAAAAAATsnfUxnZsKn5avxVXRbzpNZrz3ukFLbAQYg3AdOxIl5'
    transferData=TransferData(accessTocken)
    filefrom=input('Enter a file name')
    fileto=input('Enter the location where to upload a file')
    transferData.uplodFile(filefrom,fileto)
    print('File Uploded!')
main()