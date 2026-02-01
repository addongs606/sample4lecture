import csv

# -----------------------------
# import 실습
# -----------------------------

# __init__.py 덕분에 간단한 import
from utils_A import A

# __init__.py가 없어서 모듈까지 명시
from utils_B.b_module import B


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def main():
    print("=== 클래스 import 실습 ===")
    a = A("민준")
    a.say()

    b = B(1)
    b.say()

    # print("\n=== CSV 상대경로 읽기 ===")
    # relative_path = "data/sample.csv"
    # data1 = read_csv(relative_path)
    # print(data1)

    print("\n=== CSV 절대경로 읽기 ===")
    absolute_path = "C:/Users/user/Downloads/2일차실습/5차시/file_path_example/data/sample.csv"
    # 예:
    # "/home/user/project/data/sample.csv"
    # "C:/Users/user/project/data/sample.csv"

    # data2 = read_csv(absolute_path)
    # print(data2)


if __name__ == "__main__":
    main()
