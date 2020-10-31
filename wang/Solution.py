# matrix = [[3,7,8],[9,11,13],[15,16,17]]
# mins = {min(rows) for rows in matrix}
# print(mins)
# maxs = {max(columns) for columns in zip(*matrix)}
# print(maxs)
# print(list(mins & maxs))

# class Solution:
#     def sortedSquares(self,A):
#         res = [k**2 for k in A]
#         res.sort()
#         return res
#
# s = Solution()
# A = eval(input("输入一个列表： "))
# print(s.sortedSquares(A))
# class Solution:
#     def getWinner(self, arr, k):
#         n, i =1, 0
#         while i < k:
#             win1 = max(arr[0],arr[1])
#             remo = min(arr[0],arr[1])
#             arr.remove(remo)
#             arr.append(remo)
#             if win1 == max(arr[0],arr[1]):
#                 n += 1
#                 if n==k:return win1
#             else:n, win1 = 1, max(arr[0],arr[1])
#             if n==1:
#                 i = 0
#             else:i += 1
#
# s = Solution()
# a = eval(input("输入数组： "))
# b = int(input("输入数字： "))
# print(s.getWinner(a,b))

#last = 0
#print(int(1 != 0))
# str1 = r'hellow/world'
# print(str1)
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# pets.remove('cat')
# print(pets)

# def get_formatted_name(first_name, last_name, middle_name = ''):
#     """返回整洁的姓名"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#     musician = get_formatted_name('jimi', 'hendrix')
#     print(musician)
# musician = get_formatted_name('john', 'hooker')
# print(musician)

# def build_person(first_name, last_name, age=''):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', 27)
# print(musician)

# def make_pizza(size, *toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a " + str(size) +
#     "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)

# import pizza1
# data = int(input("输入一个整数："))
# angle = 0
# for i in range(1,data+1):
#     angle = angle + (2*i)+1
# print(angle)
# res = pizza1.funa(data)
# print(res)

# import random
# x = random.randint(100,999)
# print(x)

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         cont = 0
#         for i in nums:
#             if i < 0:
#                 cont += 1
#         nums.sort()
#         if cont >= 2:
#             return nums[0]*nums[1]*nums[-1]
#         else:return nums[-1]*nums[-2]*nums[-3]
# n = 5
# f = [5]+[0 for _ in range(n)]
# print(f)
#



# arr = [1,3,5]
# for i in range(len(arr)-2):
#     if (arr[i] == 1 or arr[i]%2 !=0) and (arr[i+1]%2 != 0 or arr[i+1] ==1)  and (arr[i+2]%2 != 0 or arr[i+2] ==1):
#         print(True)

def bubble_sort(a):#冒泡排序
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j + 1]:
                # a = nums[j]
                # nums[j] = nums[j+1]
                # nums[j+1] = a
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
print(bubble_sort([4,2,5,9,3,6]))

#########################################################

def selection_sort(a):#选择排序
    length = len(a)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if a[j] > a[i]:
                a[j], a[i] = a[i], a[j]
    return a
print(selection_sort([4,2,5,8,7,6]))


##########################################################

def quick_sort(a, start, end):#快速排序
    if start >= end:
        return
    low = start
    high = end
    mid = a[low]
    while low < high:
        while low < high and mid < a[high]:# 从右边开始找，如果元素小于基准，则把这个元素放到左边
            high -= 1
        a[low] = a[high]
        while low < high and mid > a[low]:# 从左边开始找，如果元素大于基准，则把元素放到右边
            low += 1
        a[high] = a[low]
# 循环退出，low==high，把基准元素放到这个位置
    a[low] = mid
# 递归调用，重新排列左边的和右边的序列
    quick_sort(a, start, low - 1)
    quick_sort(a, low + 1, end)
    return a
print(selection_sort([4,2,5,8,7,6]))

######################################################

def insert_sort(a):#插入排序
    for i in range(1, len(a)):
        # 从第二个元素开始，每次取出一个元素，插入前面的序列使其有序
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a
print(insert_sort([4,2,5,8,7,6]))

##########################################################

def shell_sort(a):#希尔排序
    n = len(a)# 初始步长
    gap = n // 2
    while gap > 0:# 按步长进行插入排序
        for i in range(gap, n):
            j = i# 插入排序
            while j >= gap and a[j - gap] > a[j]:
                a[j - gap], a[j] = a[j], a[j - gap]
                j -= gap
        gap = gap // 2# 得到新的步长
    return a
a = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
print(shell_sort(a))

##############################################################

def merge(left,right):#归并排序
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    #if l == len(left):
    for i in right[r:]:
        result.append(i)
    #else:
    for i in left[l:]:
        result.append(i)
    return result

def merge_sort(a):
    if len(a) <= 1:
        return a
    num = len(a) // 2
    left = merge_sort(a[:num])
    right = merge_sort(a[num:])
    return merge(left,right)

#if __name__ == '__main__':
a = [4, 7, 8, 3, 5, 9, 2, 10]
print(merge_sort(a))



#################################################################################

def heap_sort(elems):#此处小顶堆排序。如果是小顶堆，得到的是降序序列；如果是大顶堆，得到的是升序序列
    def siftdown(elems, e, begin, end):  # 向下筛选
        i, j = begin, begin * 2 + 1   # j为i的左子结点
        while j < end:
            if j + 1 < end and elems[j] > elems[j + 1]:  # 如果左子结点大于右子结点
                j += 1  # 则将j指向右子结点
            if e < elems[j]:  # j已经指向两个子结点中较小的位置，
                break  # 如果插入元素e小于j位置的值，则为3者中最小的
            elems[i] = elems[j]  # 能执行到这一步的话，说明j位置元素是三者中最小的，则将其上移到父结点位置
            i, j = j, j * 2 + 1  # 更新i为被上移为父结点的原来的j的位置，更新j为更新后i位置的左子结点
        elems[i] = e  # 如果e已经是某个子树3者中最小的元素，则将其赋给这个子树的父结点
        # 或者位置i已经更新到叶结点位置，则将e赋给这个叶结点。

    end = len(elems)
    for i in range(end // 2 - 1, -1, -1):  # 构造堆序。
        siftdown(elems, elems[i], i, end)
    for i in range((end - 1), 0, -1): # 进行堆排序.i最后一个值为1，不需要到0
        #print(elems,100)
        e = elems[i]  # 将末尾元素赋给e
        elems[i] = elems[0]  # 交换堆顶与最后一个元素
        siftdown(elems, e, 0, i)
    return (elems)

#if __name__ == "__main__":
print(heap_sort([5, 6, 8, 1, 2, 4, 12, 9]))



def heapsort(list):#此处大顶堆排序
	if list!=None:
		if list==1:
			pass
		else:
			for start in range((len(list))//2,-1,-1):#顶层循环第一步，找到堆的根结点
				rootsort(list,start,len(list)-1)
			for end in range(len(list)-1,-1,-1):#顶层循环第二步，讲根结点依次提取并排序
					list[0],list[end]=list[end],list[0]
					end-=1
					rootsort(list,0,end)
	return list
def rootsort(list,root,end):#递归函数，对list做最大堆调整
	left=2*root #父结点的左结点
	right=left+1#父结点的右结点
	if left<=end and list[root]<list[left]:#控制左结点边界，判断父结点和左结点的大小
		largest=left#
	else:
		largest=root
	if right<=end and list[largest]<list[right]:#控制右结点边界，判断父结点、右结点和左结点的大小
		largest=right#
	if largest!=root:#如果计算出来的根结点不是初始设置值，则让根结点与初始值互换位置，直至函数满足这三个条件
		list[root],list[largest]=list[largest],list[root]
		rootsort(list,largest,end)#递归函数，终止条件是larger不变
list1=[4,1,3,2,16,9,10,14,8,7,1000]
print(heapsort(list1))


#################################################################################

# coding=utf-8
def radix_sort(array):#基数排序
    max_num = max(array)
    place = 1
    while max_num > 10 ** place:
        place += 1
    for i in range(place):
        buckets = [[] for _ in range(10)]
        for num in array:
            radix = int(num / (10 ** i) % 10)
            buckets[radix].append(num)
        j = 0
        for k in range(10):
            for num in buckets[k]:
                array[j] = num
                j += 1
    return array


# if __name__ == '__main__':
array = [25, 17, 33, 17, 22, 13, 32, 15, 9, 25, 27, 18]
print(radix_sort(array))




###############################################################################


def binary_search(lis, num):#二分查找，返回索引值...序列必须有序，无序可先排序
    left = 0
    right = len(lis) - 1
    while left <= right:  # 循环条件
        mid = (left + right) // 2  # 获取中间位置，数字的索引（序列前提是有序的）
        if num < lis[mid]:  # 如果查询数字比中间数字小，那就去二分后的左边找，
            right = mid - 1  # 来到左边后，需要将右变的边界换为mid-1
        elif num > lis[mid]:  # 如果查询数字比中间数字大，那么去二分后的右边找
            left = mid + 1  # 来到右边后，需要将左边的边界换为mid+1
        else:
            return mid  # 如果查询数字刚好为中间值，返回该值得索引
    return -1  # 如果循环结束，左边大于了右边，代表没有找到

a = [1,3,5,6,7,8,9,11,14,16,19]
print(binary_search(a, 5))