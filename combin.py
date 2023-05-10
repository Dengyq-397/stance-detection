import os
import pandas as pd

file_dir="/Users/nuoen/Documents/DeepLearning/wiki-enhanced-stance-detection/data/pstance/csv/"

files=os.listdir(file_dir)

name=['BongBong','Leni']
for i in (0,1):
    dflist=[]
    for each in files:
        if(each.find(name[i])!=-1):
            dfEach=pd.read_csv(file_dir+each,error_bad_lines=False,encoding='utf-8')
            print(file_dir+each)
            print(dfEach.shape[0])
            dfEach.loc[:,'target']=name[i].lower()
            dflist.append(dfEach)
    df=pd.concat(dflist)
    #df.drop_duplicates()
    #df.drop_duplicates('full_text','first',inplace=True)
    #df["label"]=None
    #df.loc[:,'target']=name[i]
    df=df.sample(frac=1.0)
    df=df.reset_index()
    mapping = {'Against': 0,
           'None': 2,
           'Favor': 1}

    df['label'] = df['label'].apply(lambda x: mapping[x])
    df = df[df['label'] != 2]
    len=df.shape[0]
    print(len)
    a=int(len/10*6)-1
    print(a)
    b=int(a+len/10*2)-1
    print(b)
    train=df.loc[0:a]
    val=df.loc[a+1:b]
    test=df.loc[b+1:]
    mapping = {'Against': 0,
           'None': 2,
           'Favor': 1}
    train.to_csv("/Users/nuoen/Documents/DeepLearning/wiki-enhanced-stance-detection/data/pstance/processed"+"_train_"+name[i].lower()+".csv",index=False,encoding='utf-8')
    val.to_csv("/Users/nuoen/Documents/DeepLearning/wiki-enhanced-stance-detection/data/pstance/processed"+"_val_"+name[i].lower()+".csv",index=False,encoding='utf-8')
    test.to_csv("/Users/nuoen/Documents/DeepLearning/wiki-enhanced-stance-detection/data/pstance/processed"+"_test_"+name[i].lower()+".csv",index=False,encoding='utf-8')



