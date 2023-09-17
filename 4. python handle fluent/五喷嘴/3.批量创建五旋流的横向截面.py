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
    ori_log = open("E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\create plane.txt", "r", encoding="utf-8")
    for line in ori_log:
        file_data += line
    ori_log.close()
    return(file_data)


def log_replace_root(plane_position, save_place, journal):
    '''
    plane_position: 生成的模化平面
    save_place: 修改后的journal文件的保存地址
    '''
    text = plane_position
    base_text = "replacehere"
    new_log = open(save_place, "w", encoding="utf-8")
    for num in range(len(text)):
        positions = str(text[num])
        replace_text = base_text + str(num)
        journal_modify = journal.replace(replace_text, positions)
        journal = journal_modify
    new_log.write(journal_modify)
    new_log.close()
    print(save_place + " created succeed")


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
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
plane_025 = [0.024, 0.048, 0.072, 0.096]
# 定义一级目录
for nozzles in nozzles_folder:
    '''
    变量中间是fluent，就是说明这个变量是fluent的地址
    变量中间是post，就是说明这个变量是后处理的地址
    '''
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle
    dir_fluent_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\' + nozzles
    dir_post_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_fluent_nozzles + ' is on processing')
    # 定义二级目录
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_fluent_distance = dir_fluent_nozzles + '\\' + distance
        dir_post_distance = dir_post_nozzles + '\\' + distance
        # 定义三级目录
        for num in range(len(scale_factor)):
            newplane = []
            factors = scale_factor[num]
            str_factors = str(factors) 
            #  E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48\\48-1\\48-1
            dir_fluent_scale = dir_fluent_distance + '\\' + distance + '-' + str_factors + '\\' + distance + '-' + str_factors
            # 日志的保存路径
            journal_place = dir_post_distance + '\\' + distance + '-' + str_factors + '\\' + distance + '-' + str_factors + '-plane create.txt'
            # 生成平面
            for num in plane_025:
                newnum = num * factors
                newplane.append(newnum)
            print(journal_place + ' is on going')
            # 修改日志中的目标路径
            log_replace_root(newplane, journal_place, log)
            # 定义fluent进程
            session = pyFluent.launch_fluent(meshing_mode = False,version='3d',precision='double', show_gui=False, processor_count=7)
            try:
                # 读取结果文件
                session.solver.tui.file.read_case_data(file_name = dir_fluent_scale + '.cas.h5')
                # 读取日志文件  
                session.solver.tui.file.read_journal(file_name = journal_place) 
                # 保存
                session.solver.tui.file.write_case_data()
            # 如果遇到输出错误则跳过，并结束fluent在内存中的进程
            except:
                killed_resluts = fluent_failed()
                for r in killed_resluts:
                    print(r)
                # 添加到未成功输出后处理文件的目录集合
                failed_case.append(dir_fluent_scale)
                continue
            # 结束fluent进程
            session.exit()
print("失败的case：")
print(failed_case)
input("all done, input enter to exit")