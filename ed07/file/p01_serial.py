'''
https://docs.python.org/ko/3/reference
'''
import pickle


def main():
    profile_file = open('profile.pickle', 'wb')  # 바이너리 형태로 저장
    # profile_file = open('profile.pickle', 'wt')  # TypeError: write() argument must be str, not bytes

    profile = {"이름": "스누피", "나이": 22, "취미": ["자전거", "골프", "코딩"]}
    print(profile)

    # pickle: 파일에 저장
    pickle.dump(profile, profile_file)  # profile 데이터를 파일에 저장
    profile_file.close()

    print("-" * 50)
    profile_file = open('profile.pickle', 'rb')  # 읽어올 때도 바이너리 모드 명시

    profile = pickle.load(profile_file)
    print(profile)
    profile_file.close()


main()
