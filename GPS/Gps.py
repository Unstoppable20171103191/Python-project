import re
import exifread

def FindGPSimage(filepath):

    GPS = {}
    date = ""
    f=open(filepath,'rb')  #字典格式
    tags=exifread.process_file(f)
    #print(tags)  #字典可以循环，但是不能获取数据
    for tag,value in tags.items():
        #print(tag,value)

        if re.match('GPS GPSLatitudeRef',tag):
            GPS['GPS GPSLatitudeRef(纬度标识）'] = str(value)

        elif re.match('GPS GPSLongitudeRef',tag):
            GPS['GPS GPSLongitudeRef(经度标识）'] = str(value)

        elif re.match('GPS GPSAltitudeRef', tag):
            GPS['GPS GPSAltitudeRef(高度标识）'] = str(value)   #变量转换成字符串

        elif re.match('GPS GPSLatitude',tag):
            #处理异常
            try:
                match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]',str(value)).group()
                GPS['GPSLatitudeRef(纬度)'] = int(match_result[0]),int(match_result[1]),int(match_result[2]/int(match_result[3]))

                #print(match_result)   #提取数据
            except:
                GPS['GPSLatitudeRef(纬度)'] = str(value)

        elif re.match('GPS GPSLongitude', tag):
            # 处理异常
            try:
                match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).group()
                GPS['GPSLongitudeRef(纬度)'] = int(match_result[0]), int(match_result[1]), int(
                    match_result[2] / int(match_result[3]))

                # print(match_result)   #提取数据
            except:
                GPS['GPSLongitudeRef(纬度)'] = str(value)


        elif re.match('GPS GPSAltitude', tag):
            GPS['GPSAltitude(高度）'] = str(value)

        elif re.match('Image DateTime ',tag):
            date = str(value)
    return{'GPS信息':GPS,'时间信息':date}

if __name__== '__main__':
    print(FindGPSimage(r'C:\Users\LENOVO\Desktop\image.jpg'))


#28  + 10/60+125513/10000/3600