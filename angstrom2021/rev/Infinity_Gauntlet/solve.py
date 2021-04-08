import angr
import claripy

BASE = 0x400000
DEST = BASE + 0x1504
FAIL = BASE + 0x1430

flag = claripy.BVS("flag", 8 * 0x30)
p = angr.Project("./infinity_gauntlet", load_options={"auto_load_libs": False})
state = p.factory.entry_state(stdin=flag)
simgr = p.factory.simulation_manager(state)
simgr.explore(find=DEST, avoid=FAIL)

try:
    found = simgr.found[0]
    print(found.solver.eval(flag, cast_to=bytes))
except IndexError:
    print("Not Found")