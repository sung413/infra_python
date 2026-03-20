print(__name__)

class TestClass:
  pass

# 아래 if문은 main으로 실행됐을 때만 실행된다. 다른곳에서 import 될 때는 실행되지 않는다.
if __name__ == "__main__":
  print("main 함수 실행")