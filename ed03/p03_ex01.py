'''
https://docs.python.org/ko/3/reference
'''


def main():
    url = "http://naver.com"

    startIdx = url.find("/")
    # print(startIdx)  # 5
    startIdx += 2

    endIdx = url.find(".")
    # print(endIdx)  # 12

    siteName = url[startIdx:endIdx]
    # print(siteName)  # naver

    nameThree = siteName[:3]
    namelen = len(siteName)
    eCount = siteName.count("e")
    spChar = "!"

    passwd = nameThree + str(namelen) + str(eCount) + '!'
    print(passwd)

    print("{}의 비밀번호는 {}{}{}{}입니다.".format(url, nameThree, namelen, eCount, spChar))



main()
