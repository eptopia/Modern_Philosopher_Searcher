philosophers = {
    "Friedrich Nietzsche" : {
        "quote" : "Gott ist tot",
        "concept" : ["초인", "영원회귀", "힘에의 의지"],
        "description" : "서구적 전통과 이원론을 비판하였다."
    },
    
    "Karl Marx" : {
        "quote" : "Proletarians of all countries, unite!",
        "concept" : ["유물론", "프롤레타리아 혁명", "공산주의"],
        "description" : "자본주의 비판"
    }
}

while True :    
    print("=====Modern Philosopher Searcher=====")
    print("1. 철학자 목록")
    print("2. 철학자 정보 보기")
    print("3. 이름으로 검색")
    print("4. 키워드로 검색")
    print("5. 랜덤 철학자 정보")
    print("6. 랜덤 명언")
    print("7. 프로그램 종료")

    select = input("메뉴 선택 : ")

    if select == "7" :
        print("프로그램을 종료합니다.")
        break
    if select == "1" :
        print("==철학자 목록==")
        
        for philosopher in philosophers :
            print(philosopher)
