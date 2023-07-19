'''
https://docs.python.org/ko/3/reference
'''
import pickle

def main():
    with open("profile.pickle", "rb") as profile_file:
        print(pickle.load(profile_file))
        # {'이름': '스누피', '나이': 22, '취미': ['자전거', '골프', '코딩']}

main()
