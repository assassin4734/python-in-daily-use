# -*- encoding utf-8 -*-
import ansys.fluent.core as pyFluent
import shutil


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


def log_replace_plane(save_place, journal, scale):
    text_f = ['replace0', 'replace1', 'replace2', 'replace3', 'replace4', 'replace5']
    num_f = [0.192, -0.384, -0.192, -0.384, 0.192, -0.008]
    for num in range(len(text_f)):
        journal_modify = journal.replace(text_f[num], str(scale*num_f[num]))
        journal = journal_modify
    new_log = open(save_place, "w", encoding="utf-8")
    new_log.write(journal_modify)
    new_log.close()


def log_replace_tec(save_place, journal, root_replace=''):
    '''
    root_place: tecplot文件的保存地址
    save_place: 修改后的journal文件的保存地址
    '''
    text = root_replace + '45-1101.plt'
    journal_modify = journal.replace("replacehere", text)
    journal = journal_modify
    new_log = open(save_place, "w", encoding="utf-8")
    new_log.write(journal_modify)
    new_log.close()


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
         print('Error: %s' % e.strerror)


if __name__ == "__main__":
    journal_newp = 'G:\\calculations\\0-newadjustment\\createnewplane.txt'
    journal_export = 'G:\\calculations\\0-newadjustment\\data export journal.txt'
    # 定义计算根目录
    dir = 'G:\\calculations\\5nozzle-20231024\\'
    dir_post = dir + 'postprocessing\\'
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
                # copyFile(dir+'0.5.pdf', dir_working+'\\0.5.pdf')
                journal_place = dir_post_working + '\\' + distance + '-' + str_factors + '45.txt'
                journal_newplane = dir_post_working + '\\' + distance + '-' + str_factors + '45plane.txt'
                tecplot_place = dir_post_working + '\\'
                print(dir_working + ' is under calculatiing')
                # 读取case文件
                session.solver.tui.file.read_case_data(case_file_name = dir_working + '\\' + distance + '-' + str_factors + '-1101.cas.h5')
                # 后处理
                plane = log_open(journal_newp)
                log_replace_plane(save_place=journal_newplane, scale=scale_factor[num], journal=plane)
                session.solver.tui.file.read_journal(file_name = journal_newplane)
                tecex = log_open(journal_export)
                log_replace_tec(root_replace=tecplot_place, save_place=journal_place, journal=tecex)
                session.solver.tui.file.read_journal(file_name = journal_place)
                # 保存
                session.solver.tui.file.write_case_data(dir_working + '\\' + distance + '-' + str_factors + '-1101.cas.h5')
    # 结束fluent进程
    session.exit()
    # 结束
    input("all done, input enter to exit")