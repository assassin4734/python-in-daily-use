# -*- encoding utf-8 -*-

"""
fluent批量计算不同缩比下的五喷嘴几何模化
1. 缩放模型
2. 更改质量流量
3. 更改进口边界类型

计算目录：G:\Assassin\5nozzle-DLN2.6SIZE
"""


import ansys.fluent.core as pyFluent
import os
import psutil


def fluent_boundary(case, inlet, scale, mf_rate, nozzles):
    # 更改单位
    case.solver.tui.define.units('length', 'mm')
    # 进行缩放
    case.solver.tui.mesh.scale(scale, scale, scale)
    # 改进口边界条件
    for id in inlet:
        # 改质量流量大小
        case.solver.root.setup.boundary_conditions.mass_flow_inlet[id].mass_flow={
        "option": "constant or expression",
        "constant": mf_rate,
    }
        # 改水力直径
        inlet_length = 96*scale*0.001
        case.solver.root.setup.boundary_conditions.mass_flow_inlet[id].turb_hydraulic_diam=inlet_length
    # 改墙
    if nozzles == '3nozzle':
        case.solver.root.setup.boundary_conditions.mass_flow_inlet['inlet-2'].fmean={
        "option": "constant or expression",
        "constant": 0,
    }
        case.solver.root.setup.boundary_conditions.mass_flow_inlet['inlet-4'].fmean={
        "option": "constant or expression",
        "constant": 0,
    }
    elif nozzles == '1nozzle':
        i = 1
        while i < 5:
            inl = 'inlet-' + str(i)
            case.solver.root.setup.boundary_conditions.mass_flow_inlet[inl].fmean={
        "option": "constant or expression",
        "constant": 0,
    }
            i += 1
    else:
        pass
    # 改出口边界条件
    outlet_length = 836*scale*0.001
    case.solver.root.setup.boundary_conditions.pressure_outlet['outlet'].turb_hydraulic_diam=outlet_length
    # 从进口初始化
    case.solver.tui.file.read_journal(file_name=ini_journal) 
    case.solver.root.solution.run_calculation.iterate.get_attr('arguments')
    case.solver.root.solution.run_calculation.iterate(number_of_iterations=500)
    # 点火
    case.solver.tui.file.read_journal(file_name=patch_journal) 
    # 继续计算
    case.solver.root.solution.run_calculation.iterate(number_of_iterations=500)


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
    # 定义目录变量
    distance_folder = ['48', '60', '72']
    operating_folder = ['5nozzle', '3nozzle', '1nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    # 定义物理量变量
    inlet_folder = ['inlet-1', 'inlet-2', 'inlet-3', 'inlet-4', 'inlet-middle']
    massflow_folder = [0.35, 0.25515, 0.1792, 0.12005, 0.0756, 0.04375, 0.03189375, 0.01500625, 0.00546875, 0.0028]
    patch_journal = 'G:\\Assassin\\5nozzle-DLN2.6SIZE\\patch_log.txt'
    ini_journal = 'G:\\Assassin\\5nozzle-DLN2.6SIZE\\ini_log.txt'
    # 定义计算根目录
    dir = 'G:\\Assassin\\5nozzle-DLN2.6SIZE\\'
    # 定义未成功计算的目录集合
    failed_case = []
    # 工况目录
    for operates in operating_folder:
        dir_op = dir + operates
        # 变间距目录
        for folders in distance_folder:
            dir_fluent = dir_op + '\\' + folders
            print(dir_fluent + ' is under calculatiing')
            # 变缩比目录
            for num in range(len(scale_factor)):
                str_factors = str(scale_factor[num])
                dir_working = dir_fluent + '\\' + folders + '-' + str_factors
                print('----------------------------------------------')
                print(dir_working + ' is under calculatiing')
                print('----------------------------------------------')
                # 如果已经计算完成就略过
                if os.path.lexists(dir_working + '\\' + folders + '-' + str_factors + ".cas.h5") == False:
                    # 定义fluent进程
                    session = pyFluent.launch_fluent(meshing_mode = False,version='3d',precision='double', show_gui=True, processor_count=23)
                    try:
                    # 读取case文件
                        session.solver.tui.file.read_case_data(file_name = dir_fluent + '\\' + folders + '-1.cas.h5')
                    # 如果遇到输出错误则跳过，并结束fluent在内存中的进程
                    except:
                        killed_resluts = fluent_failed()
                        for r in killed_resluts:
                            print(r)
                        # 添加到未成功输出后处理文件的目录集合
                        failed_case.append(dir_working)
                        continue
                    # 进行计算设置
                    fluent_boundary(session, inlet_folder, scale_factor[num], massflow_folder[num], operates)
                    # 保存
                    session.solver.tui.file.write_case_data(dir_working + '\\' + folders + '-' + str_factors + '.cas.h5')
                    # 结束fluent进程
                    session.exit()
    # 结束
    print("失败的case：")
    print(failed_case)
    input("all done, input enter to exit")