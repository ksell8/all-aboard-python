from typing import List


class FizzBuzz:
    summary = {"fizz":0, "buzz":0, "fizzbuzz":0}

    def __init__(self, fizz: str = "fizz", buzz: str = "buzz"):
        self.fizz = fizz
        self.buzz = buzz

    def instantiate_summary(self):
        self.summary = {"fizz":0, "buzz":0, "fizzbuzz":0}

    def get_summary(self):
        print(f"-----------{self.fizz}{self.buzz} Summary--------------")
        print(f"{self.fizz}: {self.summary['fizz']}")
        print(f"{self.buzz}: {self.summary['buzz']}")
        print(f"{self.fizz}{self.buzz}: {self.summary['fizzbuzz']}")

    def fizzbuzz(self, nums: List[int]):
        self.instantiate_summary()
        for n in nums:
            if n % 15 == 0:
                print(f"{n}: {self.fizz}{self.buzz}")
                self.summary["fizzbuzz"] += 1
            elif n % 5 == 0:
                print(f"{n}: {self.fizz}")
                self.summary["fizz"] += 1
            elif n % 3 == 0:
                print(f"{n}: {self.buzz}")
                self.summary["buzz"] += 1

class Banana:
    def __init__(self):
        self.fizzbuzz = FizzBuzz("banana", "plátano")

class FizzBuzzCumulative(FizzBuzz):

    def instantiate_summary(self):
        self.summary = self.summary


if __name__ == "__main__":
    trad = FizzBuzz()

    print("-----------------------trad.fizzbuzz([1,2,3,4,5])-----------------------------")
    trad.fizzbuzz([1,2,3,4,5])
    trad.get_summary()
    print("----------------------trad.fizzbuzz(list(range(5)))---------------------------")
    trad.fizzbuzz(list(range(5)))
    trad.get_summary()


    french = FizzBuzz("fuck", "shit")

    print("---------------------french.fizzbuzz(list(range(100)))-------------------------")
    french.fizzbuzz(list(range(100)))

    french.get_summary()

    banana = Banana()
    banana.fizzbuzz.get_summary()

    print("----------------banana.fizzbuzz.fizzbuzz(list(range(200)))----------------------")
    banana.fizzbuzz.fizzbuzz(list(range(200)))
    banana.fizzbuzz.get_summary()

    cum = FizzBuzzCumulative()

    print('-----------------------cum.fizzbuzz(list(range(10)))-----------------------------')
    cum.fizzbuzz(list(range(10)))
    cum.get_summary()

    print('-------------------------cum.fizzbuzz(list(range(100)))---------------------------')
    cum.fizzbuzz(list(range(100)))
    cum.get_summary()


