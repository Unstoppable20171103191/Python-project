import os
import exifread
import re
import json
import requests


def getExif(path, filename):
    old_full_file_name = os.path.join(imgpath, filename)
    FIELD = 'EXIF DateTimeOriginal'
    fd = open(old_full_file_name, 'rb')
    tags = exifread.process_file(fd)
    fd.close()
    # 显示图片所有的exif信息
    print("showing res of getExif: \n")
    print(tags)
    print("\n\n\n\n");
    if FIELD in tags:
        print("\nstr(tags[FIELD]): %s" % (str(tags[FIELD])))  # 获取到的结果格式类似为：2018:12:07 03:10:34
        print("\nstr(tags[FIELD]).replace(':', '').replace(' ', '_'): %s" % (
            str(tags[FIELD]).replace(':', '').replace(' ', '_')))  # 获取结果格式类似为：20181207_031034
        print("\nos.path.splitext(filename)[1]: %s" % (os.path.splitext(filename)[1]))  # 获取了图片的格式，结果类似为：.jpg
        new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + os.path.splitext(filename)[1]
        print("\nnew_name: %s" % (new_name))  # 20181207_031034.jpg

        time = new_name.split(".")[0][:13]
        new_name2 = new_name.split(".")[0][:8] + '_' + filename
        print("\nfilename: %s" % filename)
        print("\n%s的拍摄时间是: %s年%s月%s日%s时%s分" % (filename, time[0:4], time[4:6], time[6:8], time[9:11], time[11:13]))

        # 可对图片进行重命名
        new_full_file_name = os.path.join(imgpath, new_name2)
        # print(old_full_file_name," ---> ", new_full_file_name)
        # os.rename(old_full_file_name, new_full_file_name)
    else:
        print('No {} found'.format(FIELD), ' in: ', old_full_file_name)


imgpath = "C:\\Users\\LENOVO\\Desktop\\image\\"
for filename in os.listdir(imgpath):

    # os.path.join用于路径拼接，将imgpath和filename连在一起得到完整的路径，后面的参数可有多个，从第一个以”/”开头的参数开始拼接
    full_file_name = os.path.join(imgpath, filename)

    # os.path.isfile用于判断路径指向的是否为文件，相类似的os.path.isdir用于判断是否为文件夹
    if os.path.isfile(full_file_name):
        getExif(imgpath, filename)
        print(full_file_name)




def latitude_and_longitude_convert_to_decimal_system(*arg):
    """
    经纬度转为小数, param arg:
    :return: 十进制小数
    """
    return float(arg[0]) + ((float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)

def find_GPS_image(pic_path):
    GPS = {}
    date = ''
    with open(pic_path, 'rb') as f:
        tags = exifread.process_file(f)
        for tag, value in tags.items():
            if re.match('GPS GPSLatitudeRef', tag):
                GPS['GPSLatitudeRef'] = str(value)
            elif re.match('GPS GPSLongitudeRef', tag):
                GPS['GPSLongitudeRef'] = str(value)
            elif re.match('GPS GPSAltitudeRef', tag):
                GPS['GPSAltitudeRef'] = str(value)
            elif re.match('GPS GPSLatitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLatitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            elif re.match('GPS GPSLongitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLongitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            elif re.match('GPS GPSAltitude', tag):
                GPS['GPSAltitude'] = str(value)
            elif re.match('.*Date.*', tag):
                date = str(value)
    return {'GPS_information': GPS, 'date_information': date}

def find_address_from_GPS(GPS):
    """
    使用Geocoding API把经纬度坐标转换为结构化地址。
    :param GPS:
    :return:
    """
    secret_key = 'zbLsuDDL4CS2U0M4KezOZZbGUY9iWtVf'
    if not GPS['GPS_information']:
        return '该照片无GPS信息'
    lat, lng = GPS['GPS_information']['GPSLatitude'], GPS['GPS_information']['GPSLongitude']
    baidu_map_api = "http://api.map.baidu.com/geocoder/v2/?ak={0}&callback=renderReverse&location={1},{2}s&output=json&pois=0".format(
        secret_key, lat, lng)
    response = requests.get(baidu_map_api)
    content = response.text.replace("renderReverse&&renderReverse(", "")[:-1]
    baidu_map_address = json.loads(content)
    formatted_address = baidu_map_address["result"]["formatted_address"]
    province = baidu_map_address["result"]["addressComponent"]["province"]
    city = baidu_map_address["result"]["addressComponent"]["city"]
    district = baidu_map_address["result"]["addressComponent"]["district"]
    return formatted_address,province,city,district

GPS_info = find_GPS_image(pic_path='C:\\Users\\LENOVO\\Desktop\\image.jpg')
address = find_address_from_GPS(GPS=GPS_info)
print(address)

