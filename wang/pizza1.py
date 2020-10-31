# def merge(left,right):
#     l, r = 0, 0
#     result = []
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     if l == len(left):
#         for i in right[r:]:
#             result.append(i)
#     else:
#         for i in left[l:]:
#             result.append(i)
#     return result
#
# def merge_sort(a):
#     if len(a) <= 1:
#         return a
#     num = len(a) // 2
#     left = merge_sort(a[:num])
#     right = merge_sort(a[num:])
#     return merge(left,right)
#
# if __name__ == '__main__':
#     a = [4, 7, 8, 3, 5, 9]
#     print(merge_sort(a))
# print(int(25/1%10))
# # coding=utf-8
# def radix_sort(array):
#     max_num = max(array)
#     place = 1
#     while max_num > 10 ** place:
#         place += 1
#     for i in range(place):
#         buckets = [[] for _ in range(10)]
#         for num in array:
#             radix = int(num / (10 ** i) % 10)
#             print(radix)
#             buckets[radix].append(num)
#         j = 0
#         for k in range(10):
#             for num in buckets[k]:
#                 array[j] = num
#                 j += 1
#     return array
#
#
# if __name__ == '__main__':
#     array = [25, 17, 33, 17, 22, 13, 32, 15, 9, 25, 27, 18]
#     print(radix_sort(array))

def heapsort(list):#此处xiao顶堆排序
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
	if left<=end and list[root]>list[left]:#控制左结点边界，判断父结点和左结点的大小
		small=left
	else:
		small=root
	if right<=end and list[small]>list[right]:#控制右结点边界，判断父结点、右结点和左结点的大小
		small=right#
	if small!=root:#如果计算出来的根结点不是初始设置值，则让根结点与初始值互换位置，直至函数满足这三个条件
		list[root],list[small]=list[small],list[root]
		rootsort(list,small,end)#递归函数，终止条件是larger不变
list1=[4,1,3,2,16,9,10,14,8,7,1000]
print(heapsort(list1))
