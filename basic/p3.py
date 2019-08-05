'''
연속데이터(시퀀스 타입)
    > 리스트   : [] -> js의 배열과 동일, 순서가 존재, 값 중복 OK
                      인덱스는 정방향/역방향(-1, -2, ...) 존재
'''

# 비어있는 리스트 생성
# 정적 생성 : 일반적으로 문제는 없으나, 간혹 추가가 안 되는 경우가 생긴다
#            이런 경우 동적 생성으로 대체
#            => 자료구조를 직접 맞춰서 데이터를 세팅하는 리스트 내포같은 케이스에 사용
nums = [] 
print(nums, len(nums), type(nums)) # [] 0 <class 'list'>
# 동적 생성 -> 대량의 작업 시 조금 더 안정적
nums = list() 
print(nums, len(nums), type(nums)) # [] 0 <class 'list'>
nums=[1, 3, 5, 7, 9]
print(nums, len(nums), type(nums))
animals = ['dog', 'cat', 'bird']
print(animals, len(animals), type(animals))

# 리스트의 멤버들의 타입이 다르면 리스트를 구성할 수 없다? X
# 파이썬의 모든 것은 객체이므로, 멤버들도 모두 객체
# -> 주소를 가지고 있고, 이것이 포함
mix = [1, 2, 3, 'dog', 'cat']
print(mix, len(mix), type(mix))
# 차원을 섞으면? 멤버 중에 하나가 리스트라면? 
# -> 차원도 상관없다!
multiTypeMatrix = [1, 2, 3, 'dog', 'cat', ['bird', 100]]
print(multiTypeMatrix, len(multiTypeMatrix), type(multiTypeMatrix))

# (인덱싱) multiTypeMatrix에서 100을 출력
print(multiTypeMatrix[-1][-1])

# (슬라이싱) nums에서 3, 5, 7만 가진 리스트를 구하시오 : 리스트 -> 리스트(슬라이싱 : 차원 유지)
nums = [1, 3, 5, 7, 9]
print(nums[1:-1])
# 슬라이싱의 본질은 사본작업
# 원본은 유지된다
# 원본 변경 방법은 인덱싱을 활용해서
nums[0] = 100
print(nums)
# 3, 5, 7을 모두 -1로 변경하시오
# nums[1:-1] = -1 -> 에러 : 데이터 타입이 안 맞는다
# nums[1:-1] = '-1' -> 가능은 하다 / 같은 시퀀스(연속데이터) 타입일 때
print(nums)

# 멤버 삭제
del nums[0]
print(nums)
# 9값을 가진 멤버를 제거
nums.remove(9)
print(nums)
# 같은 멤버가 여러 개 있다면?
# -> 중복되는 데이터 중 (정방향으로) 가장 먼저 찾은 멤버를 제거
nums = [1, 3, 2, 3, 4, 3, 5, 7]
nums.remove(3)
print(nums)
# 모두 제거
nums.clear()
print(nums) # []

# 멤버 추가 : append vs extend
nums.append(1)
print(nums)
tmp = [3, 5]
nums.append(tmp) # [1, [3, 5]] : 자식으로 추가
print(nums) 
nums.extend(tmp) # [1, [3, 5], 3, 5] : 리스트를 이어붙인다
print(nums)
print(nums + tmp) # [1, [3, 5], 3, 5, 3, 5] : extend와 유사, but 메모리 관점에서는 다르다
                  #                           두 개를 이어붙여서 return -> 사본작업
                  #                           extend는 원본을 변경






