# from mod import encodeQR

# res=encodeQR("CMS")
# print("Domain Name : CMS")
# print("Encoded String is : ",''.join(res))


# b

class CmsMedia:
    allowedFileType = "png"

    def __init__(self, conType, postCount):
        self.contentType = conType
        # self.fileName=fileName
        self.postCount = postCount

    def getMediadetails(self):
        print('-'*40)
        self.postTitle = input("enter your post title ")
        self.fileName = input("enter your filename ")
        print("Post Title : ", self.postTitle, "\nFile Name : ", self.fileName)

    def fileCheck(self):
        fileext = self.fileName.split('.')
        if (fileext[1] == self.allowedFileType):
            print("file format is acceptable")


class ImageProvider(CmsMedia):
    imageProvider = "cloudinary"
    AllowedFileSize = "2"  # 2mb

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def fileCheck(self, fileSize, fileType):
        super().getMediadetails()
        print("File size : ", fileSize)
        fileext = fileType.split('.')
        if (fileext[1] == super().allowedFileType and fileSize <= self.AllowedFileSize):
            print("Your file has been uploaded to cloudinary")


media = CmsMedia("image", 2)
obj = ImageProvider("asaksas9askskdksd")
obj.fileCheck("2", "untitled.png")
