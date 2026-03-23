if __name__ == "__main__":
  try:
    num1_str: str = input("젯수 입력: ")
    num2_str: str = input("피젯수 입력: ")

    num1: int = int(num1_str)
    num2: int = int(num2_str)

    result: int = num1 / num2
    print(result)
  except Exception as e:
    print(e)
  else:
    pass
  finally:
    print("종료 합니다")