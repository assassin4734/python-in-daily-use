# -*- encoding utf-8 -*-


import ansys.fluent.core as pyFluent
import os
import psutil


def log_open():
    '''
    ori_log: 基础的journal文件
    file_data: 把基础文件读入成文本文件存在内存中方便调用
    '''
    file_data = ""
    ori_log = open("E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\data export journal.txt", "r", encoding="utf-8")
    for line in ori_log:
        file_data += line
    ori_log.close()
    return(file_data)


def log_replace_root(root_replace, save_place, journal):
    '''
    root_place: tecplot文件的保存地址
    save_place: 修改后的journal文件的保存地址
    '''
    text = root_replace
    journal_modify = journal.replace("replacehere", text)
    new_log = open(save_place, "w", encoding="utf-8")
    new_log.write(journal_modify)
    new_log.close()


def fluent_failed():
    '''
    有四个进程是属于fluent的，需要依次取消，不然关不掉fluent
    '''
    session_list = psutil.pids()
    killed_process = []
    for i in session_list:
        try:
            fluent_process = psutil.Process(i)
            if fluent_process.name() == "fl2220.exe":
                fluent_process.kill()
                killed_process.append(fluent_process.name() + " has been killed")
                continue
            elif fluent_process.name() == "cx2220.exe":
                fluent_process.kill()
                killed_process.append(fluent_process.name() + " has been killed")
                continue
            elif fluent_process.name() == "fluent.exe":
                fluent_process.kill()
                killed_process.append(fluent_process.name() + " has been killed")
                continue
            elif fluent_process.name() == "fl_mpi2220.exe":
                fluent_process.kill()
                killed_process.append(fluent_process.name() + " has been killed")
                continue
            else:
                continue
        except:
            pass
    return(killed_process)


# 打开原始日志文件
log = log_open()
# 定义未成功输出后处理文件的目录集合
failed_case = []
# 定义目录变量
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# 定义一级目录
for eq in eq_folder:
    '''
    变量中间是fluent，就是说明这个变量是fluent的地址
    变量中间是post，就是说明这个变量是后处理的地址
    '''
    dir_fluent = 'E:\\0-PhD\\1 nozzle\\eq\\' + eq
    dir_post = 'E:\\0-PhD\\1 nozzle\eq\\postprocessing\\' + eq
    print(dir_fluent + ' is on processing')
    for num in range(len(scale_factor)):
        factors = scale_factor[num]
        str_factors = str(factors) 
        dir_fluent_scale = dir_fluent + '\\40.5-' + str_factors
        # 日志的保存路径
        journal_place = dir_post + '\\40.5-' + str_factors + '\\' + eq + '-' + str_factors + '.txt'
        # plt的保存路径
        tecplot_place = dir_post + '\\40.5-' + str_factors + '\\28.5-1-V'
        print(journal_place + ' is on going')
        # # 已经处理好的就跳过
        # if os.path.lexists(tecplot_place + ".plt") == False:
            # 修改日志中的目标路径
        log_replace_root(tecplot_place, journal_place, log)
        # 定义fluent进程
        session = pyFluent.launch_fluent(version='3d',precision='double', show_gui=False, processor_count=1)
        try:
            # 读取结果文件
            session.solver.tui.file.read_case_data(file_name = dir_fluent_scale + '.cas.h5')
            # 读取日志文件  
            session.solver.tui.file.read_journal(file_name = journal_place) 
        # 如果遇到输出错误则跳过，并结束fluent在内存中的进程
        except:
            killed_resluts = fluent_failed()
            for r in killed_resluts:
                print(r)
            # 添加到未成功输出后处理文件的目录集合
            failed_case.append(dir_fluent_scale)
            continue
print("失败的case：")
for fail in failed_case:
    print(fail)
input("all done, input enter to exit")