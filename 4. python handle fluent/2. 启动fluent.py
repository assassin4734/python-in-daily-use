import ansys.fluent.core as pyFluent
from ansys.fluent.parametric import ParametricProject, ParametricStudy
session = pyFluent.launch_fluent(meshing_mode = False,version='3d',precision='double', show_gui=False, processor_count=1)
session.solver.tui.file.read_case_data(file_name = r'F:\PhD\1 nozzle\re\postprocessing\z-40.5\40.5-0.5.cas.h5')
session.solver.tui.file.read_journal(file_name = r'F:\PhD\1 nozzle\data export journal.txt')
tui = session.solver.tui
session.solver.root.setup.boundary_conditions.mass_flow_inlet['inlet'].mass_flow={
    "option": "constant or expression",
    "constant": 1,
}
# session.solver.tui.file.export.tecplot(file_name=r'F:\PhD\1 nozzle\re\postprocessing\z-40.5\40.5-0.5.plt')
input("all done, input enter to exit")