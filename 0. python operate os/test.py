from PIL import Image

test = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing-transport\\eq=0.55\\eq=0.55-无量纲径向速度-1.png'
image_cut = Image.open(test)
image_cut.show()
cut = image_cut.crop((0, 0, 1000, 1000))
cut.show()
input()
