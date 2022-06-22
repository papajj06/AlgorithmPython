text = input().upper()
text_element = list(set(text)) # 중복되는 text 다 필터링

text_count = [text.count(i) for i in text_element] # 각 구성된 알파벳 개수를 센 리스트

if text_count.count(max(text_count)) > 1: # 만약 개수를 센 리스트에서 max 최대값을 가진 것이 2개나 나오면 ? 물음표 출력 
    print("?")
else:
    print(text_element[text_count.index(max(text_count))]) #아니면 해당 max 개수 가지는 인덱스 -> 알파벳 출력
