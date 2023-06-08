# Сортировка слиянием
def merge_sort(nums):
  if len(nums) > 1: # Делим список надвое до тех пор пока не осталось по одному элементу:
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right): # Затем начинаем их упорядочевать-создаём пары: Сравниваем между списками два значения и добавляем в nums[k]
      if left[i] < right[j]:
        nums[k] = left[i]
        i += 1
      else:
        nums[k] = right[j]
        j += 1
      k += 1
    while i < len(left): # С помощью двух циклов добавляем значения оставшиеся в каком-либо списке в конец
      nums[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      nums[k] = right[j]
      j += 1
      k += 1
list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)