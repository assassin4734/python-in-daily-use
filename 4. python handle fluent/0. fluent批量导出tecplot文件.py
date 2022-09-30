# -*- encoding utf-8 -*-

import ansys.fluent.core as pyFluent
import os
import psutil


def log_open():
    file_data = ""
    ori_log = open("F:\\PhD\\1 nozzle\\data export journal.txt", "r", encoding="utf-8")
    for line in ori_log:
        file_data += line
    ori_log.close()
    return(file_data)


def log_replace_root(root_replace, save_place, journal):
    text = root_replace
    journal_modify = journal.replace("replacehere", text)
    new_log = open(save_place, "w", encoding="utf-8")
    new_log.write(journal_modify)
    new_log.close()


# 打开原始日志文件
log = log_open()
# 定义未成功输出后处理文件的目录集合
failed_case = []
# 定义目录变量
file_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# 定义一级目录
for folders in file_folder:
    str_folders = str(folders)
    dir_fluent = 'F:\\PhD\\1 nozzle\\eq\\' + str_folders
    dir_collection = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + str_folders
    print(dir_fluent + ' is on processing')
# 定义二级目录
    for num in range(len(scale_factor)):
        factors = scale_factor[num]
        str_factors = str(factors)  
        dir_working = dir_fluent + '\\40.5-' + str_factors
        journal_place = dir_collection + '\\40.5-' + str_factors + '\\40.5-' + str_factors + '.txt'
        tecplot_place = dir_collection + '\\40.5-' + str_factors + '\\40.5-' + str_factors
        print(journal_place + ' is on going')
# 已经处理好的就跳过
        if os.path.lexists(tecplot_place + ".plt") == False:
# 修改日志中的目标路径
            log_replace_root(tecplot_place, journal_place, log)
# 定义fluent进程
            session = pyFluent.launch_fluent(meshing_mode = False,version='3d',precision='double', show_gui=False, processor_count=1)
            try:
# 读取结果文件
                session.solver.tui.file.read_case_data(file_name = dir_working + '.cas.h5')
# 读取日志文件  
                session.solver.tui.file.read_journal(file_name = journal_place) 
# 如果遇到输出错误则跳过，并结束fluent在内存中的进程
            except:
                session_list = psutil.pids()
                for i in session_list:
                    try:
                        fluent_process = psutil.Process(i)
                        if fluent_process.name() == "fluent.exe":
                            fluent_process.terminate()
                            break
                    except:
                        pass
# 添加到未成功输出后处理文件的目录集合
                failed_case.append(journal_place)
                continue
# 结束fluent进程
            session.exit()
        else:
            continue
print("失败的case：")
print(failed_case)
input("all done, input enter to exit")