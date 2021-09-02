# -*- coding:utf-8 -*-
import base64
import requests
import cv2
from base.config import IMAGE_PATH, URL

"""
- 图片处理方法及优缺点
1. 灰度处理并二值化，使用算法点、线降噪，最后识别
    缺点：算法有局限性，不能干净的清楚掉干扰线、点
    优点：百度ocr和pytesseract识别较为一致，识别正确率不高
2. 由于干扰线、点的色块大部分都是灰色，转化为HSV，按照灰色色域去掉干扰线、点
    缺点：
        处于灰色色域的字母内容也会被清除  -->  登录失败作判断重复登录即可
        百度ocr和pytesseract识别不是很一致   -->   用百度吧，pytesseract还是要训练过AI之后识别才高
    优点：处理干净，适用大部分验证码
"""


def download_image():
    src = URL + "/service/api/p/login/getVerify"
    r = requests.get(url=src)

    with open(IMAGE_PATH + '\\getVerify.png', 'wb') as i:
        i.write(r.content)


def get_dynamic_binary_image(img_name):
    """ 灰度处理&二值化
    加载彩色图像：cv2.imread(img_name)
    灰值化：cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    二值化：自适应二值化
    cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None)
        blockSize：要分成的区域大小，上面的N值，一般取奇数  -->  当blockSize越大，参与计算阈值的区域也越大，细节轮廓就变得越少，整体轮廓越粗越明显
        C：常数，每个区域计算出的阈值的基础上在减去这个常数作为这个区域的最终阈值，可以为负数  -->  当C越大，每个像素点的N*N邻域计算出的阈值就越小，中心点大于这个阈值的可能性也就越大，设置成255的概率就越大，整体图像白色像素就越多，反之亦然。
    :param img_name:
    :return:
    """
    filename = IMAGE_PATH + "\\" + 'getVerify-binary.png'
    img_name = IMAGE_PATH + '\\' + img_name
    print(img_name)
    im = cv2.imread(img_name)

    # imHSV = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(imHSV, numpy.array([0, 0, 40]), numpy.array([180, 43, 220]))
    # # cv2.imshow("mask", mask)
    # im[mask > 0] = (255, 255, 255)
    # # cv2.imshow(("imMask"), im)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 30)
    cv2.imwrite(filename, th1)
    # cv2.waitKey(0)
    return th1


# 去除边框
def clear_border(img):
    """ 去除边框
    根据验证码的生成样例除去宽度比较多一点，除去高度比较少一点
    :param img:
    :return:
    """
    filename = IMAGE_PATH + "\\" + 'getVerify-clearBorder.png'
    # 返回行，列和通道数的元组
    # print( img.shape ) -->  (342, 548, 3)
    h, w = img.shape[:2]
    for y in range(0, w):
        for x in range(0, h):
            if y < 10 or y > w - 10:
                img[x, y] = 255
            if x < 2 or x > h - 2:
                img[x, y] = 255
        cv2.imwrite(filename, img)
    return img


def interference_line(img):
    """ 干扰线降噪
    1.
    :param img:
    :param img_name:
    :return:
    """
    filename = IMAGE_PATH + "\\" + 'getVerify-interferenceline.png'
    h, w = img.shape[:2]
    # ！！！opencv矩阵点是反的
    # img[1,2] 1:图片的高度x，2：图片的宽度y
    # 四邻域算法
    for y in range(1, w - 1):
        for x in range(1, h - 1):
            count = 0
            if img[x, y - 1] > 245:
                count = count + 1
            if img[x, y + 1] > 245:
                count = count + 1
            if img[x - 1, y] > 245:
                count = count + 1
            if img[x + 1, y] > 245:
                count = count + 1
            if count > 2:
                img[x, y] = 255
    cv2.imwrite(filename, img)
    return img

    # 八邻域算法
    # for y in range(1, h - 1):
    #     for x in range(1, w - 1):
    #         count = 0
    #         if img[x, y - 1] > 245:  # 上
    #             count = count + 1
    #         if img[x, y + 1] > 245:  # 下
    #             count = count + 1
    #         if img[x - 1, y] > 245:  # 左
    #             count = count + 1
    #         if img[x + 1, y] > 245:  # 右
    #             count = count + 1
    #         if img[x - 1, y - 1] > 245:  # 左上
    #             count = count + 1
    #         if img[x - 1, y + 1] > 245:  # 左下
    #             count = count + 1
    #         if img[x + 1, y - 1] > 245:  # 右上
    #             count = count + 1
    #         if img[x + 1, y + 1] > 245:  # 右下
    #             count = count + 1
    #         if count > 4:
    #             pixdata[x, y] = 255

    # width = img.shape[1]
    # height = img.shape[0]
    # for w in range(width):
    #     count = 0
    #     for h in range(height):
    #         if img[h][w] < 100:
    #             count += 1
    #         else:
    #             if 1.5 > count > 0:
    #                 for c in range(count):
    #                     img[h - c - 1][w] = 255
    #             count = 0
    #
    # for h in range(height):
    #     count = 0
    #     for w in range(width):
    #         if img[h][w] < 100:
    #             count += 1
    #         else:
    #             if 1.5 > count > 0:
    #                 for c in range(count):
    #                     img[h][w - c - 1] = 255
    #             count = 0
    # cv2.imwrite(filename, img)
    # return img


def interference_point(img, x=0, y=0):
    """ 点降噪
    9邻域框,以当前点为中心的田字框,黑点个数
    :param x:
    :param y:
    :return:
    """
    filename = IMAGE_PATH + "\\" + 'getVerify-interferencePoint.png'
    # todo 判断图片的长宽度下限
    cur_pixel = img[x, y]  # 当前像素点的值
    height, width = img.shape[:2]

    for y in range(0, width - 1):
        for x in range(0, height - 1):
            if y == 0:  # 第一行
                if x == 0:  # 左上顶点,4邻域
                    # 中心点旁边3个点
                    sum = int(cur_pixel) + int(img[x, y + 1]) + int(img[x + 1, y]) + int(img[x + 1, y + 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                elif x == height - 1:  # 右上顶点
                    sum = int(cur_pixel) + int(img[x, y + 1]) + int(img[x - 1, y]) + int(img[x - 1, y + 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                else:  # 最上非顶点,6邻域
                    sum = int(img[x - 1, y]) + int(img[x - 1, y + 1]) + int(cur_pixel) + int(img[x, y + 1]) + int(
                        img[x + 1, y]) + int(img[x + 1, y + 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
            elif y == width - 1:  # 最下面一行
                if x == 0:  # 左下顶点
                    # 中心点旁边3个点
                    sum = int(cur_pixel) + int(img[x + 1, y]) + int(img[x + 1, y - 1]) + int(img[x, y - 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                elif x == height - 1:  # 右下顶点
                    sum = int(cur_pixel) + int(img[x, y - 1]) + int(img[x - 1, y]) + int(img[x - 1, y - 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                else:  # 最下非顶点,6邻域
                    sum = int(cur_pixel) + int(img[x - 1, y]) + int(img[x + 1, y]) + int(img[x, y - 1]) + int(
                        img[x - 1, y - 1]) + int(img[x + 1, y - 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
            else:  # y不在边界
                if x == 0:  # 左边非顶点
                    sum = int(img[x, y - 1]) + int(cur_pixel) + int(img[x, y + 1]) + int(img[x + 1, y - 1]) + int(
                        img[x + 1, y]) + int(img[x + 1, y + 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
                elif x == height - 1:  # 右边非顶点
                    sum = int(img[x, y - 1]) + int(cur_pixel) + int(img[x, y + 1]) + int(img[x - 1, y - 1]) + int(
                        img[x - 1, y]) + int(img[x - 1, y + 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
                else:  # 具备9领域条件的
                    sum = int(img[x - 1, y - 1]) + int(img[x - 1, y]) + int(img[x - 1, y + 1]) + int(
                        img[x, y - 1]) + int(cur_pixel) + int(img[x, y + 1]) + int(img[x + 1, y - 1]) + int(
                        img[x + 1, y]) + int(img[x + 1, y + 1])
                    if sum <= 4 * 245:
                        img[x, y] = 0
    cv2.imwrite(filename, img)
    return img


def picture_to_text():
    im = get_dynamic_binary_image("getVerify.png")
    clear_border(im)
    interference_line(im)
    interference_point(im)

    with open(IMAGE_PATH + '\\getVerify-interferenceline.png', 'rb') as f:
        img = base64.b64encode(f.read())

    token = requests.session().post(
        url="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=r1URhNMyGA9novTAWdANmf8k&client_secret=z9dvcHgagoIWSIVhpLsZpcG6BpkY6aEk",
        headers={'content-type': 'application/x-www-form-urlencoded'}
    ).json()

    res = requests.session().post(
        url="https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + token['access_token'],
        data={"image": img},
        headers={'content-type': 'application/x-www-form-urlencoded'}
    )

    if res.json()["words_result"] is []:
        return None
    else:
        return res.json()["words_result"][0]['words']


if __name__ == "__main__":
    print(picture_to_text())

    # download_image()
    # im = get_dynamic_binary_image("getVerify.png")
    # clear_border(im)
    # interference_line(im)
    # interference_point(im)
    #
    # # 不切割直接识别，精度不太行
    # image = Image.open(IMAGE_PATH + "\\getVerify-interferenceline.png")
    # code = pytesseract.image_to_string(image)
    # print(code)
    #
    # with open(IMAGE_PATH+'\\getVerify-interferenceline.png', 'rb') as f:
    #     img = base64.b64encode(f.read())
    #
    # token = requests.session().post(
    #     url="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=r1URhNMyGA9novTAWdANmf8k&client_secret=z9dvcHgagoIWSIVhpLsZpcG6BpkY6aEk",
    #     headers={'content-type': 'application/x-www-form-urlencoded'}
    # ).json()
    #
    # res = requests.session().post(
    #     url="https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token="+token['access_token'],
    #     data={"image": img},
    #     headers={'content-type': 'application/x-www-form-urlencoded'}
    # )
    #
    # print(res.json())
