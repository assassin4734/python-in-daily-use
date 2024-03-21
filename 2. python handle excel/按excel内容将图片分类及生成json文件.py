# _*_ encoding utf-8 _*_
'''
按excel内容将图片分类及生成json文件
jpg或者png图片类型要对应着改
'''
import xlwings as xw
import json
import re
import shutil


def copyFile(num, src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
        input("press to continue")
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)
        missing.append('问题' + str(num) + "：" +src)


def has_chinese(text):
    pattern =re.compile(r'[\u4e00-\u9fff]+')
    try:
        result = pattern.search(text)
        return True if result else False
    except:
        pass


if __name__ == "__main__":
    # 所有变量
    vars = ['biology', 'chemistry', 'geography', 'history', 'math', 'physics']
    for var in vars:
        # 工作文件夹
        dir_ori = "E:\\3-work\\4-other\\20240307\\0-" + var + "\\"
        images = dir_ori + "images\\"
        questions = dir_ori + "questions\\"
        # 打开excel，读取对应sheet
        app_ori = xw.App(visible=True, add_book=False)
        wb_ori = app_ori.books.open("E:\\3-work\\4-other\\20240307\\" + var + "\\questions\\" + var + "Questions.xlsx")
        sht_ori = wb_ori.sheets[0]
        # 按行号取值，表中第一行是标题
        i = 2
        j = 1
        while i < 10002:
            # 读取问题
            data = sht_ori.range('B'+str(i)).value
            print(data)
            # 读取对应问题的annotation
            k = 4
            annotation = ""
            while k < 25:
                anno = sht_ori.range((i, k)).value
                if has_chinese(anno) == True:
                    annotation = annotation + "，" + anno
                k += 1
            # 判断是否包含图片
            if "img src" in data:
                dir_image_washed_1 = re.findall(r'<img src.*>',data)
                print(dir_image_washed_1)
                # 定义存放图片名的列表
                name_img_all= []
                # 得到的是列表
                for dir_washed in dir_image_washed_1:
                    # 再次清洗
                    dir_washed_2 = str(re.findall(r'book-eec/(.*?).png',dir_washed)).strip('[]').strip("'")
                    # 修补文件名
                    dir_image = "E:\\3-work\\4-other\\20240307\\" + var + "\\" + var + "Questions-Images\\book-eec\\" + dir_washed_2 + ".png"
                    # 按问题序号和问题中的图片编号重命名整理图片
                    name_img = (str(j)+'-'+str(dir_image_washed_1.index(dir_washed))+'.png')
                    # 名字放入列表中
                    name_img_all.append(name_img)
                    print('开始复制问题'+str(i-1))
                    print(dir_image)
                    print(images+name_img)
                    # 定义找不到路径的图片
                    missing = []
                    copyFile((i-1), dir_image, images+name_img)
                    # 用问题文本减去文件名文本
                    data = data.replace(str(dir_washed),'')
                # 判断问题类型
                if 'underline' in data:
                    cat = '选择题'
                else:
                    cat = '填空题'
                # 把图片名称列表转化为字符串用来组成字典
                allnames = ','.join(name_img_all)
                # 如果没有存在问题的图片，就生成问题
                if missing == []:
                    question_txt = {
                        "问题类型": cat,
                        "annotation": annotation,
                        "imageName": allnames,
                        "questions": data
                    }
                    # 创建json文件
                    with open(questions+str(j)+"-question.json", 'w', encoding='utf-8') as file:
                        json.dump(question_txt, file, indent=4, ensure_ascii=False)
                    j += 1
            else:
                pass
            i += 1
        app_ori.quit()


    input("exit")