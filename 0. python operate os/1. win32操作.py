import win32com.client as client

PPT = client.GetActiveObject("Powerpoint.Application")
PPTPres = PPT.ActivePresentation
# PPT = client.DispatchEx("Powerpoint.Application")
# PPTPres = PPT.Presentations.Open("F:\PhD\\1 nozzle\\different swirl number\\postprocessing\\数值模拟处理-t.pptx")
# print(PPT.OperatingSystem)
# print(PPT.Path)
# print(PPT.ProductCode)
unit_point = 0.03527
PPTSlide1 = PPTPres.Slides(1)

# for PPTSlide in PPTPres.Slides:
#     print(PPTSlide.Name)
#     print(PPTSlide.Shapes.Count)
#     print(PPTSlide.SlideID)

PPTShape1 = PPTSlide1.Shapes(1)
# PPTShape1.Select()
# shprng = PPTApp.ActiveWindow.Selection.ShapeRange
# print(dir(PPTShape1))
PPTShape1.Width = 7/unit_point
PPTShape1.Height = 3.74/unit_point
input("continue")
PPTShape2 = PPTSlide1.Shapes(2)
# PPTShape1.Select()
# shprng = PPTApp.ActiveWindow.Selection.ShapeRange
# print(dir(PPTShape1))
PPTShape2.Width = 7/unit_point
PPTShape2.Height = 3.74/unit_point
input("continue")
PPTShape3 = PPTSlide1.Shapes(3)
# PPTShape1.Select()
# shprng = PPTApp.ActiveWindow.Selection.ShapeRange
# print(dir(PPTShape1))
PPTShape3.Width = 7/unit_point
PPTShape3.Height = 3.74/unit_point
input("continue")