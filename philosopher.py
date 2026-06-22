import random

philosophers = {
    "아르투르 쇼펜하우어" : {
        "quote" : "Life swings like a pendulum backward and forward between pain and boredom.",
        "concept" : ["의지", "표상", "염세주의"],
        "description" : "인간을 맹목적인 의지에 지배되는 존재로 보며 고통과 욕망의 문제를 탐구하였다."
        },
    "칼 마르크스" : {
        "quote" : "Proletarians of all countries, unite!",
        "concept" : ["유물론", "프롤레타리아 혁명", "공산주의"],
        "description" : "자본주의를 비판하고, 사회 변화를 계급투쟁과 유물론을 통해 설명하였다."
        },
    "프리드리히 니체" : {
        "quote" : "Gott ist tot",
        "concept" : ["초인", "영원회귀", "의지", "힘에의 의지"],
        "description" : "기존 도덕을 비판하고 인간의 자기극복과 가치 창조를 강조하였다."
        },
    "지그문트 프로이트" : {
            "quote" : "The ego is not master in its own house.",
            "concept" : ["이드", "자아", "초자아", "무의식"],
            "description" : "정신분석학을 창시하였으며, 인간 행동의 근원을 무의식에서 찾았다."
        },
    "마르틴 하이데거" : {
        "quote" : "Man is not the lord of beings. Man is the shepherd of Being.",
        "concept" : ["존재", "현존재", "불안", "실존"],
        "description" : "존재의 의미를 탐구하고 인간을 현존재로 규정하였다."
        },
    "장폴 사르트르" : {
        "quote" : "Existence precedes essence.",
        "concept" : ["실존", "자유", "책임", "존재"],
        "description" : "실존은 본질에 앞선다고 보며 인간의 자유와 선택을 강조하였다."
        },
    "알베르 카뮈" : {
        "quote" : "One must imagine Sisyphus happy.",
        "concept" : ["부조리", "실존", "반항", "자유"],
        "description" : "부조리와 반항을 통해 인간 존재의 의미를 탐구하였다."
        },
    "미셸 푸코" : {
        "quote" : "Where there is power, there is resistance.",
        "concept" : ["권력", "주체", "담론"],
        "description" : "권력과 담론이 인간의 지식과 주체를 형성한다고 보았다."
        },
    "자크 데리다" : {
        "quote" : "There is nothing outside the text.",
        "concept" : ["해체", "차연", "텍스트"],
        "description" : "해체를 통해 언어와 의미의 고정성을 비판하였다."
        },
    "위르겐 하버마스" : {
        "quote" : "Only those norms can claim legitimacy that could meet with the assent of all affected in rational discourse.",
        "concept" : ["공론장", "의사소통 행위", "합의", "담론"],
        "description" : "의사소통과 공론장을 통해 합리적 합의를 추구하였다."
        }
}

while True :    
    print("=====Modern Philosopher Searcher=====")
    print("1. 철학자 목록")
    print("2. 철학자 이름으로 검색")
    print("3. 키워드로 검색")
    print("4. 오늘의 철학자")
    print("5. 랜덤 명언")
    print("6. 프로그램 종료")

    select = input("메뉴 선택 : ")

    if select == "6" :
        print("프로그램을 종료합니다.")
        break

    if select == "1" :
        print("==철학자 목록==")
        
        for i, philosopher in enumerate(philosophers, start=1) :
            print(f"{i}. {philosopher}")

    if select == "2" :
        print("== 철학자 이름 검색 ==")

        name = input("철학자 이름 입력 : ")
        if name in philosophers :
            print(f"\n- 이름 : {name}\n")
            
            print(f'- 명언 :  "{philosophers[name]["quote"]}"\n')

            print(f"- 설명 :  {philosophers[name]["description"]}\n")

            print("- 주요 개념")
            for concept in philosophers[name]["concept"] :
                print(f" # {concept}")
            print()

    if select == "3" :

        keyword = input("검색할 철학자의 개념 입력 : ")
        exist = False

        for philosopher in philosophers :
                if keyword in philosophers[philosopher]["concept"] :
                        print(f"\n => {philosopher}")
                        print(f"\n - {philosophers[philosopher]['description']}\n")
                        exist = True

        if not exist :
            print("검색 결과가 없습니다.")
    
    if select == "4" :
        name = random.choice(list(philosophers.keys()))

        print(f"\n- 이름 : {name}\n")

        print(f"- 설명 :  {philosophers[name]["description"]}\n")

        print("- 주요 개념")
        for concept in philosophers[name]["concept"] :
            print(f" # {concept}")
        print()

    if select == "5" :
        name = random.choice(list(philosophers.keys()))

        print(f'\n"{philosophers[name]['quote']}"')
        print(f" - {name}\n")



    
