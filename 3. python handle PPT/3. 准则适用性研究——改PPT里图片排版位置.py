# -encoding utf-8-

import win32com.client as client




PPT = client.GetActiveObject("Powerpoint.Application")
PPTPres = PPT.ActivePresentation
print("共有" + str(len(PPTPres.Slides)) + "张slide")
unit_point = 0.03527
slide_count = 22
while 22 < slide_count < 23:
    PPTSlide = PPTPres.Slides[slide_count]
    lines = 1
    TopStart = 0
    LeftStart = 0
    for PPTShape in PPTSlide.Shapes:
        PPTShape.Width = 7/unit_point
        PPTShape.Height = 3.74/unit_point
        PPTShape.Top = TopStart
        PPTShape.Left = LeftStart
        LeftStart += 7/unit_point
        if lines%2 == 0:
            TopStart += 3.74/unit_point
            LeftStart = 0
        lines += 1
    slide_count += 1