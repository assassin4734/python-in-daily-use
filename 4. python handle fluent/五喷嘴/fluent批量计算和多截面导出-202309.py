# -*- encoding utf-8 -*-

"""
fluent批量计算不同缩比下的五喷嘴几何模化
1. 缩放模型
2. 更改质量流量
3. 更改进口边界类型

计算目录：F:\assassin\5nozzle-DLN2.6SIZE-NEW
"""


import ansys.fluent.core as pyFluent
import os
import psutil


def fluent_boundary(case, inlet, scale, mf_rate, nozzles):
    # 改进口质量流量和水力直径
    for id in inlet:
        # 改质量流量大小
        case.solver.root.setup.boundary_conditions.mass_flow_inlet[id].mass_flow={
        "option": "constant or expression",
        "constant": mf_rate,
    }
        # 改水力直径
        inlet_length = 96*scale*0.001
        case.solver.root.setup.boundary_conditions.mass_flow_inlet[id].turb_hydraulic_diam=inlet_length
    # 改进口质量分数
    case.solver.root.setup.boundary_conditions.mass_flow_inlet['inlet-middle'].fmean={
        "option": "constant or expression",
        "constant": 0.05532,
    }
    if nozzles == '5nozzle':
        i = 1
        while i < 5:
            inl = 'inlet-' + str(i)
            case.solver.root.setup.boundary_conditions.mass_flow_inlet[inl].fmean={
        "option": "constant or expression",
        "constant": 0.03786,
    }
            i += 1
    elif nozzles == '3nozzle':
        j = 1
        while j < 5:
            inl = 'inlet-' + str(j)
            case.solver.root.setup.boundary_conditions.mass_flow_inlet[inl].fmean={
        "option": "constant or expression",
        "constant": 0.03786,
    }
            j += 1
        case.solver.root.setup.boundary_conditions.mass_flow_inlet['inlet-2'].fmean={
        "option": "constant or expression",
        "constant": 0,
    }
        case.solver.root.setup.boundary_conditions.mass_flow_inlet['inlet-4'].fmean={
        "option": "constant or expression",
        "constant": 0,
    }
    elif nozzles == '1nozzle':
        k = 1
        while k < 5:
            inl = 'inlet-' + str(k)
            case.solver.root.setup.boundary_conditions.mass_flow_inlet[inl].fmean={
        "option": "constant or expression",
        "constant": 0,
    }
            k += 1
    else:
        pass
    # 改出口边界条件
    outlet_length = 836*scale*0.001
    case.solver.root.setup.boundary_conditions.pressure_outlet['outlet'].turb_hydraulic_diam=outlet_length
    session.solver.tui.file.read_journal(file_name = journal_place_model)
    # 继续计算
    case.solver.root.solution.run_calculation.iterate.get_attr('arguments')
    case.solver.root.solution.run_calculation.iterate(number_of_iterations=100)


def log_open(dir_j):
    '''
    ori_log: 基础的journal文件
    file_data: 把基础文件读入成文本文件存在内存中方便调用
    '''
    file_data = ""
    ori_log = open(dir_j, "r", encoding="utf-8")
    for line in ori_log:
        file_data += line
    ori_log.close()
    return(file_data)


def log_tecexport(save_place, journal, root_replace=''):
    '''
    root_place: tecplot文件的保存地址
    save_place: 修改后的journal文件的保存地址
    '''
    text_save = []
    plane_position = ['central-1', 'central-2', '0.25d', '0.5d', '0.75d', '1d']
    base_text = "replacehere"
    for n in range(len(plane_position)):
        rep = base_text + str(n)
        text = root_replace + plane_position[n] + '.plt'
        journal_modify = journal.replace(rep, text)
        journal = journal_modify
        text_save.append(text)
    new_log = open(save_place, "w", encoding="utf-8")
    new_log.write(journal_modify)
    new_log.close()
    return text_save


def changemodel(save_place, journal):
    '''
    save_place: 修改后的journal文件的保存地址
    '''
    base_text_1 = "replacehere1"
    base_text_2 = "replacehere2"
    journal_modify = journal.replace(base_text_1, dir_working + '\\' + distance + '-' + str_factors + '.fla')
    journal = journal_modify
    journal_modify = journal.replace(base_text_2, dir_working + '\\' + distance + '-' + str_factors + '.pdf')
    journal = journal_modify
    new_log = open(save_place, "w", encoding="utf-8")
    new_log.write(journal_modify)
    new_log.close()



def fluent_failed():
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


if __name__ == "__main__":
    # 定义计算根目录
    dir = 'D:\\5nozzle-DLN2.6SIZE-NEW\\'
    dir_post = dir + 'postprocessing\\'
    # 定义目录变量
    distance_folder = ['48']
    operating_folder = ['3nozzle', '5nozzle', '1nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    # 定义物理量变量
    inlet_folder = ['inlet-1', 'inlet-2', 'inlet-3', 'inlet-4', 'inlet-middle']
    massflow_folder = [0.175, 0.1276, 0.0896, 0.060025, 0.0378, 0.0159, 0.0112, 0.0075, 0.004725, 0.002734]
    # 定义未成功计算的目录集合
    failed_case = []
    # 定义fluent进程
    session = pyFluent.launch_fluent(meshing_mode = False,version='3d',precision='double', show_gui=True, processor_count=47)
    # 工况目录
    for operates in operating_folder:
        # G:\\Assassin\\5nozzle-DLN2.6SIZE\\5nozzle
        dir_op = dir + operates
        dir_post_op = dir_post + operates
        # 变间距目录
        for distance in distance_folder:
            # G:\\Assassin\\5nozzle-DLN2.6SIZE\\5nozzle\\48
            dir_D = dir_op + '\\' + distance
            dir_post_D = dir_post_op + '\\' + distance
            print(dir_D + ' is under calculatiing')
            # 变缩比目录
            for num in range(len(scale_factor)):
                str_factors = str(scale_factor[num])
                # G:\\Assassin\\5nozzle-DLN2.6SIZE\\5nozzle\\48\\48-1
                dir_working = dir_D + '\\' + distance + '-' + str_factors
                # 后处理目录
                dir_post_working = dir_post_D + '\\' + distance + '-' + str_factors
                journal_place = dir_post_working + '\\' + distance + '-' + str_factors + '.txt'
                tecplot_place = dir_post_working + '\\'
                if os.path.lexists(dir_working + '\\' + distance + '-' + str_factors + '-0912.cas.h5') == False:
                    print(dir_working + ' is under calculatiing')
                    try:
                        # 读取case文件
                        session.solver.tui.file.read_case(case_file_name = dir_working + '\\' + distance + '-' + str_factors + '.cas.h5')
                        # 进行计算设置
                        mf = massflow_folder[num] * 2
                        journal_place_model = dir_post_working + '\\' + distance + '-' + str_factors + '-model.txt'
                        log = log_open(dir+'changemodel.txt')
                        changemodel(journal_place_model, log)
                        fluent_boundary(session, inlet_folder, scale_factor[num], mf, operates)
                        # 后处理
                        log = log_open(dir+'data export journal.txt')
                        alljournal = log_tecexport(root_replace=tecplot_place, save_place=journal_place, journal=log)
                        session.solver.tui.file.read_journal(file_name = journal_place)
                        # 保存
                        session.solver.tui.file.write_case_data(dir_working + '\\' + distance + '-' + str_factors + '-0912.cas.h5')
                    # 如果遇到输出错误则跳过，并结束fluent在内存中的进程
                    except:
                        killed_resluts = fluent_failed()
                        for r in killed_resluts:
                            print(r)
                        # 添加到未成功输出后处理文件的目录集合
                        failed_case.append(dir_working)
                        continue
    # 结束fluent进程
    session.exit()
    # 结束
    print("失败的case：")
    print(failed_case)
    input("all done, input enter to exit")