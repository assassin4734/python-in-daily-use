# -*- encoding utf-8 -*-
import ansys.fluent.core as pyFluent
import os


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


def log_replace_tec(save_place, journal):
    '''
    root_place: tecplot文件的保存地址
    save_place: 修改后的journal文件的保存地址
    '''
    journal_modify = journal.replace("replace1", dir_post_working+"\\central-1.plt")
    journal = journal_modify
    journal_modify = journal.replace("replace2", dir_post_working+"\\central-2.plt")
    journal = journal_modify
    journal_modify = journal.replace("replace3", dir_post_working+"\\45-0912.plt")
    journal = journal_modify
    new_log = open(save_place, "w", encoding="utf-8")
    new_log.write(journal_modify)
    new_log.close()


if __name__ == "__main__":
    # 定义计算根目录
    dir = 'G:\\calculations\\1-5nozzle-fullgridandcorexperiment\\'
    dir_post = dir + 'postprocessing\\'
    jou = dir_post + "dataexport.txt"
    # 定义目录变量
    distance_folder = ['48']
    operating_folder = ['1nozzle', '3nozzle', '5nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    # 定义fluent进程
    session = pyFluent.launch_fluent(meshing_mode = False,version='3d',precision='double', show_gui=True, processor_count=11)
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
                print(dir_working + ' is under calculatiing')
                files = os.listdir(dir_post_working)
                for file in files:
                    if '.plt' in file:
                        try:
                            os.remove(dir_post_working + '\\' + file)
                        except:
                            pass
                # 读取case文件
                session.solver.tui.file.read_case_data(case_file_name=dir_working + '\\' + distance + '-' + str_factors + '-0912.cas.h5')
                # 后处理
                jou_new = log_open(jou)
                log_replace_tec(save_place=dir_post_working+'\\dataexport_new.txt', journal=jou_new)
                session.solver.tui.file.read_journal(file_name=dir_post_working+'\\dataexport_new.txt')
    # 结束fluent进程
    session.exit()
    # 结束
    input("all done, input enter to exit")