class myCar:

  def __init__(self, name: str):
    print("myCar 생성자 호출")
    print(self)
    self.name = name

  def drive(self):
    print(f"{self.name} drive")

if __name__ == "__main__":
  cl: myCar = myCar("소나타").drive()
  c2: myCar = myCar("모닝").drive()