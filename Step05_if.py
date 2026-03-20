input: str = input("8자리 비밀번호를 입력해주세요: ")

if len(input) < 8:
  print("사용불가입니다.")
else:
  print("사용 가능한 비밀번호입니다.")