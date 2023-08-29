import pandas as pd

dir = "E:\\0-PhD\\1 nozzle\\"
name = "正交试验对比.xlsx"
dir_name =dir + name
fini = pd.read_excel(io=dir_name, sheet_name='Sheet1')
doe = pd.read_excel(io=dir_name, sheet_name='Sheet2')
dupl = []
new_fini = []
print(fini.shape)
print(doe.shape)
lis_doe = []
for i in range(49):
    l_doe = list(doe.iloc[i])
    lis_doe.append(l_doe)
    for j in range(79):
        l_fini = list(fini.iloc[j])
        if l_doe == l_fini:
            dupl.append(l_doe)
            try:
                lis_doe.pop(lis_doe.index(l_doe))
            except:
                pass
for k in dupl:
    print(k)
new_fini_df = pd.DataFrame(lis_doe)
new_fini_df.to_csv(path_or_buf=dir + "对比后的新工况筛选.csv")