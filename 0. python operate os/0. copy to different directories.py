# _*_ encoding utf-8 _*_

import os
import pathlib
import shutil

def working_directory():
    """
    软件工作界面
    添加多个工作目录，添加完毕结束输入
    :return:无
    """
    print("=" * 50)
    print("")
    print("将指定文件拷贝到多个文件夹内\n")
    print("输入【1】：目标路径\n输入【2】：想拷贝的文件路径\n输入【0】：结束输入")
    print("")
    print("=" * 50)
    target_list = []   # 目标地址记录器
    file_list = []   # 拷贝文件记录器
    while True:
        print("-" * 50)
        action_str = input("请选择希望对工作目录执行的操作：")
        print("-" * 50)
        if action_str == "1":   # "1"开始输入工作目录
            while True:
                dir1 = input("\n请输入文件目标路径：")   # 给定工作目录
                dir1_to_path = pathlib.Path(dir1)
                dir1_validation = dir1_to_path.exists()
                if dir1_validation:
                    target_list.append(dir1)    # 获取工作目录名称列表
                    print("\n添加的目录%d为：%s" % (len(target_list), dir1))
                    print("\n当前共有%d个目标路径" % len(target_list))    # 统计工作目录数量
                    terminate1 = input("\n是否继续输入？\n【任意键】继续输入\n【0】返回上一级")
                    if terminate1 == "0":
                        break
                    else:
                        continue
                else:
                    print("\n目录有误，请重新输入！")
        elif action_str == "2":
            while True:
                dir2 = input("\n请输入文件所在路径：")   # 给定工作目录
                dir2_to_path = pathlib.Path(dir2)
                dir2_validation = dir2_to_path.exists()
                if dir2_validation:
                    file_list.append(dir2)    # 获取当前文件夹中的文件名称列表
                    print("\n添加的目录%d为：%s" % (len(file_list), dir2))
                    print("\n当前共有%d个文件" % len(file_list))    # 统计文件数量
                    terminate2 = input("\n是否继续输入？\n【任意键】继续输入\n【0】返回上一级")
                    if terminate2 == "0":
                        break
                    else:
                        continue
                else:
                    print("\n目录有误，请重新输入！")
        elif action_str == "0":     # "0"退出系统
            break
        else:
            print("\n输入错误，请重新输入！")    # 输入其他则报错
    return target_list, file_list

working_list = working_directory()
target_list_copy = working_list[0]
file_list_copy = working_list[1]
for file_copy in file_list_copy:
    print(file_copy)
    fpath,fname=os.path.split(file_copy)
    print("待复制的文件   " + fname)
    for target_copy in target_list_copy:
        shutil.copy(file_copy, target_copy)
        print("已复制完成任务   " + target_copy)
input("输入回车退出")