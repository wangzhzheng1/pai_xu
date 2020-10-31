import numpy as np
import time

# FilePathone='D:/原电脑FileReceive/dataset/cifar/cifar_query.fvecs'#注意glove数据集用的cosine距离，排序时升序降序要注意
FilePathtwo = 'D:/原电脑FileReceive/dataset/cifar/cifar_base.fvecs'


def ivecs_read(fname):  # NumPy提供了多种存取数组内容的文件操作函数
    a = np.fromfile(fname, dtype='int32')  # fromfile()函数读回数据时需要用户指定元素类型，并对数组的形状进行适当的修改
    d = a[0]  # Int32, 等于int, 占4个字节
    return a.reshape(-1, d + 1)[:, 1:].copy()  # (-1,d+1)指行数未知，d+1列#X[:,  m:n]，即取所有数据的第m到n-1列数据，含左不含右


def fvecs_read(fname):
    return ivecs_read(fname).view('float32')


# x2=fvecs_read(FilePathone)
xj = fvecs_read(FilePathtwo)


def near_neigh(i, n):  # 查询点i的n个最近邻
    disa = {}
    for j in range(0, len(xj)):
        if i == j:
            continue
        '''dis1=np.dot(xj[i],xj[j])/(np.linalg.norm(xj[i]) * np.linalg.norm(xj[j]))#np.dot 点积,np.linalog.norm 向量的2范数, 即向量的每个元素的平方和再开平方根，
        disa[j]=dis1'''
        dis0 = xj[i] - xj[j]
        dis1 = np.sqrt(np.sum(dis0 * dis0))
        disa[j] = dis1
        # a=sorted(disa.items(), key=lambda item:item[1])
    a = sorted(disa.items(), key=lambda item: item[1], reverse=False)  # 按字典集合中，每一个元组的第二个元素排列,x相当于字典集合中遍历出来的一个元组
    # a=sorted(disa.items(), key=lambda item:item[1])
    b = []  # sorted(可迭代对象,key=函数名,reverse=False/True),key=lambda x : x[1], x：相当于字典集合中的一个元组,x[1]: 返回x中的第二个元素，即键值对元组中的值
    for k in range(0, n):
        b.append(a[k][0])
    # disb[i]=b
    return b


'''dis1=np.dot(xj[0],xj[1])/(np.linalg.norm(xj[0]) * np.linalg.norm(xj[1]))#
print(dis1)'''

clu_coe = []
start = time.process_time()
for p in range(0, 1):  # 500
    print(p)
    print('......')
    a = near_neigh(p, 20)  # 修改NN近邻的个数
    disb = {}
    for i in range(0, len(a)):
        b = near_neigh(a[i], 20)  # 修改近邻个数
        disb[a[i]] = b
    q = 0
    for m in range(0, len(a)):
        # q=0
        for n in range(m + 1, len(a)):
            if a[m] in disb[a[n]]:
                q = q + 1
    clustering_coeffient = q / (len(a) * (len(a) - 1) / 2)
    clu_coe.append(clustering_coeffient)
end = time.process_time()
print(end - start, 's')

sum = 0
for r in clu_coe:
    sum = sum + r
ave_clu_coe = sum / 100  # (len(xj)/2686)#修改聚类系数总点数
