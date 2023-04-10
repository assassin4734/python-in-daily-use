from PIL import Image


print('定位后处理的目录')
onenozzlefolder = {'变当量比': 'eq\\postprocessing-transport\\',
                   '变旋流数': 'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-40.5", "z-45.5", "z-52.5"],
          'eq_folder': ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
positions = [1, 2, 3, 4]
data_val = ['无量纲轴向速度', '无量纲径向速度']
dir = 'E:\\0-PhD\\1 nozzle\\'
for para in onenozzlefolder:
    # E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\
    dir_para = dir + onenozzlefolder[para]
    print(dir_para + '正被处理')
    if para == '变当量比':
        fol = 'eq_folder'
    elif para == '变旋流数':
        fol = 'sw_folder'
    else:
        pass
    for var in folder[fol]:
        dir_origin = dir_para + var + '\\'
        for data in data_val:
            dir_graph = dir_origin + var + '-' + data
            for pos in positions:
                dir_pos = dir_graph + '-' + str(pos) + '.png'
                print(dir_pos)
                image = Image.open(dir_pos)
                image_cut = image.crop((0, 0, 1448, 1404))
                image_cut.save(dir_pos.strip('.png') + '-cut.png')
input('all done')