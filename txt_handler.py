# -*- coding: utf-8 -*-
inf = open("$fault.inf","r")
f10 = open("$fault_10.out", "r")
f02 = open("$fault_02.out", "r")
f11 = open("$fault_11.out", "r")
f12 = open("$fault_12.out", "r")
f13 = open("$fault_13.out", "r")
f14 = open("$fault_14.out", "r")
#f15 = open("$fault_15.out", "r")
fout = open('out_FDIA.txt','w')
#要采集的数据类型有52种，对应的列范围在93-144.即在fault_10~fault_15.out中   104-155，即在fault 11~fault_16中---原特性72+差分特性36+叠加特性48
#最终的排序：95-130共36个差分特性，即在fault 10~fault 14.out中    95-202但是差分和原始特性没有分开
#aout_fake信号编号是12，即在fault_02.out中；aout_real信号编号是16，即在fault_02.out中
ln0 = 0
f02.__next__()
line0 = f02.__next__()
ln0 = ln0+1
ln1 = ln0
#time0和time1即aout信号
time0 = line0[2]
res = []
while(True):
    try:
        line1 = f02.__next__()
    except StopIteration:
        break
    ln1 = ln1+1
    if not line1:
        break
    L0 = line0.split()
    L1 = line1.split()
    if(len(L0)==0):
        continue
    time1 = L1[2]
    if time1 != time0:
        res.append(ln0) #记录故障发生的时间点
        res.append(ln1+1)
    time0 = L1[2]
    line0 = line1
    ln0 = ln0+1
print('故障发生时间前后时间点:',len(res))
print(res)
datas = []
line10 = f10.readlines()
line11 = f11.readlines()
line12 = f12.readlines()
line13 = f13.readlines()
line14 = f14.readlines()
#line15 = f15.readlines()
j = 0
for i in range(0,len(res),2):
        datas.append([])
        datas[j].append(line10[res[i]].split()[5:]+line11[res[i]].split()[1:]+line12[res[i]].split()[1:]+line13[res[i]].split()[1:]+line14[res[i]].split()[1:])
        datas[j].append(line10[res[i+1]].split()[5:]+line11[res[i+1]].split()[1:]+line12[res[i+1]].split()[1:]+line13[res[i+1]].split()[1:]+line14[res[i+1]].split()[1:])
        j=j+1
print(len(datas))
print(len(datas[1]))
print(len(datas[1][1]))
#for list in datas:
#    fout.writelines(list)
#f10.__next__()
#line0 = f10.__next__()
#time0 = line0[0]
#while(True):
#    line1 = f10.__next__()
#    line2 = f10.__next__()
  #  if line1[0] in res:
#        datas.append(line0[1,]) # 提取时刻相同的f10中的行数据，并且首先去除掉第一列数据
#        datas.append(line2[1,])
#    line0 = line1
#    line1 = line2
#f1.close()
f10.close()
f11.close()
f12.close()
f13.close()
f14.close()
#f15.close()
inf.close()
fout.close()
#构造叠加特性
#Vdif
#datas：