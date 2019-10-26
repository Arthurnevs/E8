pivot = int(input())
maior = []
menos = []
while True:
  nums = int(input())
  if nums < 0:
    break
  if nums > pivot:
    maior.append(nums)
  else:
    menos.append(nums) 

print(menos)
print(pivot)
print(maior)
