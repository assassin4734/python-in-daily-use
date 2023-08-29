# -encoding utf-8-

import win32com.client as client




PPT = client.GetActiveObject("Powerpoint.Application")
PPTPres = PPT.ActivePresentation
print("共有" + str(len(PPTPres.Slides)) + "张slide")
unit_point = 0.03527
slide_count = 0
while slide_count < len(PPTPres.Slides):
    PPTSlide = PPTPres.Slides[slide_count]
    for PPTShape in PPTSlide.Shapes:
        PPTShape.PictureFormat.CropLeft = 3/unit_point
    slide_count += 1
input("done")