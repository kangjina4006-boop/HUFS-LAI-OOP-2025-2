import time
from tqdm import tqdm

class Country:
    def __init__(self, name: str, gold=0, silver=0, bronze=0):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __repr__(self):
        return f"{self.name}: G{self.gold} S{self.silver} B{self.bronze}"

    # Arithmetic overriding → 메달 합산
    def __add__(self, other):
        n_gold = self.gold + other.gold
        n_silver = self.silver + other.silver
        n_bronze = self.bronze + other.bronze
        return Country(self.name, new_gold, new_silver, new_bronze)
        
    

    # Comparison overriding → 금 > 은 > 동 순서로 비교
    def __lt__(self, other: "Country") -> bool:
        if self.gold != other.gold:
            return self.gold < other.gold
        if self.silver != other.silver:
            return self.silver < other.silver
            
        return self.bronze < other.bronze


    def __eq__(self, other: object) -> bool:
        if not isinstance (other, country): [cite: 131]
            return False 
    
        return (
            self.name == other.name
            and self.gold ==other.gold
            and self.silver == other.silver
            and self.bronze == other.bronze) 
        pass 


if __name__ == "__main__":
    # 샘플 이벤트: (국가, 메달종류)
    events = [
        ("KOR", "gold"), 
        ("KOR", "silver"),
        ("USA", "gold"), 
        ("USA", "gold"), 
        ("USA", "bronze"),
        ("JPN", "gold"), 
        ("JPN", "silver"),
        ("CHN", "bronze"), 
        ("CHN", "bronze"),
    ]

    for country, medal in tqdm(events, desc="Processing events"): [cite: 236]
  


    
    countries = {}

    # TODO: tqdm으로 집계 진행
    for country, medal in events:
        time.sleep(0.1)  # 진행바 확인용 딜레이
        if country not in countries:
            countries[country] = Country(country)
        if medal == "gold":
            countries[country].gold += 1
        elif medal == "silver":
            countries[country].silver += 1
        elif medal == "bronze":
            countries[country].bronze += 1

    # 리더보드 출력 (금→은→동 기준 내림차순)
    leaderboard = sorted(countries.values(), reverse=True)

    print("\n=== Medal Leaderboard ===")
    for rank, c in enumerate(leaderboard, start=1):
        print(f"{rank:>2}. {c}")

-----------------------------------------------------

import time
from tqdm import tqdm # 외부 라이브러리 tqdm을 import 합니다. 

class Country:
    def __init__(self, name: str, gold=0, silver=0, bronze=0):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __repr__(self):
        # 객체를 출력할 때 사용되는 문자열을 정의하여 과제 출력 형식에 맞춥니다.
        return f"{self.name}: G{self.gold} S{self.silver} B{self.bronze}"

    # --- 1. __add__ 구현: Arithmetic Operator Overloading [cite: 160, 162, 166] ---
    def __add__(self, other):
        """두 Country 객체의 메달 수를 합산하여 새로운 객체를 반환합니다."""
        
        # 메달 수를 합산합니다.
        new_gold = self.gold + other.gold
        new_silver = self.silver + other.silver
        new_bronze = self.bronze + other.bronze
        
        # 새로운 Country 객체를 생성하여 반환합니다. 이름은 self의 것을 따릅니다.
        return Country(self.name, new_gold, new_silver, new_bronze)

    # --- 2. __lt__ 구현: Comparison Method Overriding [cite: 145, 146, 152, 155] ---
    def __lt__(self, other: "Country") -> bool:
        """
        순위 결정을 위한 미만(Less Than) 비교 (self < other).
        sorted() 함수에 의해 사용됩니다. self가 other보다 순위가 낮으면(작으면) True를 반환합니다.
        순위 기준: 금메달 > 은메달 > 동메달
        """
        
        # 1. 금메달 비교 (가장 중요)
        if self.gold != other.gold:
            # 금메달이 적으면 순위가 낮음 (True)
            return self.gold < other.gold

        # 2. 은메달 비교 (금메달 수가 같을 때)
        if self.silver != other.silver:
            # 은메달이 적으면 순위가 낮음 (True)
            return self.silver < other.silver

        # 3. 동메달 비교 (금/은메달 수가 같을 때)
        # 동메달이 적으면 순위가 낮음 (True)
        return self.bronze < other.bronze

    # --- 3. __eq__ 구현: Comparison Method Overriding [cite: 150, 152] ---
    def __eq__(self, other: object) -> bool:
        """두 Country 객체의 메달 수가 완전히 같은지 비교합니다."""
        # 비교 대상이 Country 객체인지 먼저 확인합니다.
        if not isinstance(other, Country): [cite: 131]
            return False 
            
        return (self.gold == other.gold and
                self.silver == other.silver and
                self.bronze == other.bronze)
    

if __name__ == "__main__":
    events = [
        ("KOR", "gold"), 
        ("KOR", "silver"),
        ("USA", "gold"), 
        ("USA", "gold"), 
        ("USA", "bronze"),
        ("JPN", "gold"), 
        ("JPN", "silver"),
        ("CHN", "bronze"), 
        ("CHN", "bronze"),
    ]

    countries = {}

    # TODO: tqdm으로 집계 진행 (반복 가능한 객체를 tqdm()으로 감쌉니다.)
    for country, medal in tqdm(events, desc="Processing events"): [cite: 236]
        time.sleep(0.1)  # 진행바 확인용 딜레이
        
        if country not in countries:
            countries[country] = Country(country)
            
        if medal == "gold":
            countries[country].gold += 1
        elif medal == "silver":
            countries[country].silver += 1
        elif medal == "bronze":
            countries[country].bronze += 1

    # 리더보드 출력 (sorted() 함수가 Country 클래스의 __lt__를 사용합니다.) 
    # reverse=True 이므로 순위가 높은(메달이 많은) 국가가 먼저 옵니다.
    leaderboard = sorted(countries.values(), reverse=True)

    print("\n=== Medal Leaderboard ===")
    for rank, c in enumerate(leaderboard, start=1):
        print(f"{rank:>2}. {c}")



