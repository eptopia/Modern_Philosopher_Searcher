philosophers = {
    "프리드리히 니체" : {
        "quote" : "Gott ist tot",
        "concept" : ["초인", "영원회귀", "힘에의 의지"],
        "description" : "서구적 전통과 이원론을 비판하였다."
    },
    
    "칼 마르크스" : {
        "quote" : "Proletarians of all countries, unite!",
        "concept" : ["유물론", "프롤레타리아 혁명", "공산주의"],
        "description" : "자본주의 비판"
    }
}

while True :    
    print("=====Modern Philosopher Searcher=====")
    print("1. 철학자 목록")
    print("2. 철학자 이름으로 검색")
    print("3. 키워드로 검색")
    print("4. 랜덤 철학자 정보")
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
