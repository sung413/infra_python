class Phone:
  def call(self):
    print("call")

class HandPhone(Phone):
  def take_picture(self):
    print("take picture")

class SmartPhone(HandPhone):
  def internet(self):
    print("internet")

  def take_picture(self):
    print("take picture!!!!")

if __name__ == "__main__":
  p1: Phone = Phone()
  p1.call()

  p2: HandPhone = HandPhone()
  p2.take_picture()

  p3: SmartPhone = SmartPhone()
  p3.call()
  p3.take_picture()