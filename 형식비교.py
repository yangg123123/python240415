# 리스트와 튜플 생성
data_list = [1, 2, 3, 4, 5]
data_tuple = (1, 2, 3, 4, 5)

# 자료형 확인
print(f"리스트 자료형: {type(data_list)}")
print(f"튜플 자료형: {type(data_tuple)}")

# 요소 변경
try:
  data_list[0] = 10
  print("리스트 요소 변경 성공")
except TypeError:
  print("리스트 요소 변경 불가능")

try:
  data_tuple[0] = 10
  print("튜플 요소 변경 성공")
except TypeError:
  print("튜플 요소 변경 불가능")

# 요소 추가
data_list.append(6)
print(f"리스트 요소 추가: {data_list}")

try:
  data_tuple.append(6)
  print("튜플 요소 추가 성공")
except TypeError:
  print("튜플 요소 추가 불가능")

# 요소 삭제
del data_list[0]
print(f"리스트 첫 번째 요소 삭제: {data_list}")

try:
  del data_tuple[0]
  print("튜플 첫 번째 요소 삭제 성공")
except TypeError:
  print("튜플 요소 삭제 불가능")

# 객체 복사
data_list_copy = data_list[:]
data_tuple_copy = data_tuple

print(f"리스트 복사: {data_list_copy}")
print(f"튜플 복사: {data_tuple_copy}")

# 객체 동일성 확인
if data_list is data_list_copy:
  print("리스트 복사본은 동일한 객체")
else:
  print("리스트 복사본은 다른 객체")

if data_tuple is data_tuple_copy:
  print("튜플 복사본은 동일한 객체")
else:
  print("튜플 복사본은 다른 객체")
  