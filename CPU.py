# import pandas as pd
# import numpy as np
# from Excel import ImportExcel
# import TableConfig
# day='05/05'
# data=pd.DataFrame(ImportExcel("Bang-cham-cong-[5-2020].xlsx"))
# index=TableConfig.GetColumn(data,0,day)
# l=data.iloc[:,index]
from Excel_usable import *
import TableConfig
def ConvertData(day,source,data,nameExcel):
    # day='05/05'
    data=pd.DataFrame(ImportExcel(data))
    ThongTin=pd.DataFrame(ImportExcel(source))
    id=TableConfig.GetColumn(data,0,day)
    # l=data.iloc[:,index]
    ThongTin.columns=ThongTin.iloc[0]
    k=ThongTin.iloc[1:len(ThongTin),3]

    l=list(set(k))

    # for i in l:
    # for i in range(len(data)):
    #     if data[data.iloc[]]
    # ThongTin.columns==ThongTin.iloc[0]
    datafr=pd.DataFrame()
    # datafr['Tên','Vị trí','Công trình','Ngày sinh','Sđt','Tổng quân']=''
    datafr['Tổng quân']=''
    datafr['STT']=''
    check=True
    # sodem=[]
    Lct=[]
    stt=0
    for i in range(len(l)):
        sodem = 0
        kk=ThongTin.where(ThongTin.iloc[1:len(data),3]==l[i]).dropna()
        for j in range(len(kk)):
            if len(data[data.index==kk.index[j]])>0:

                if (data.loc[kk.index[j]].iloc[id]!='x' and pd.isna(data.loc[kk.index[j]].iloc[id])==False):
                    sodem+=1
                    datafr = datafr.append(kk.iloc[j])
                    stt+=1
                    datafr.loc[kk.index[j], 'STT'] = stt
                    if check:
                        Lct.append(kk.index[j])
                        locate=j
                        check=not check

                    # print(data.loc[kk.index[j]].iloc[id])
            # test=kk.where(kk.index[locate]).dropna()
            if j == (len(kk) - 1) and len(kk)>0 and sodem!=0:
                datafr.loc[Lct[len(Lct)-1], 'Tổng quân'] = sodem



        check=True
    datafr=datafr[['STT','Họ Tên','Phòng Ban','Vị trí','Công trình','Ngày sinh','Sđt','Tổng quân']]
    D = 'Ngày ' + day[0:2] + '-' + day[3:5]
    ExportExcel(nameExcel,D,datafr)



