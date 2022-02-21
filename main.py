#!/usr/bin/env python3
from rosys.automations import drive_to
from nicegui import ui
import rosys
import rosys.ui
from rosys.world import Point

# setup
runtime = rosys.Runtime()
rosys.ui.configure(ui, runtime)

# keyboard control
print(rosys.ui.keyboard_control.ui)
rosys.ui.keyboard_control()



async def handle_click(msg):
    for hit in msg.hits:
        target = Point(x=hit.point.x, y=hit.point.y)
        runtime.automator.replace(drive_to(runtime.world, runtime.hardware, target))
        await runtime.resume()


# 3d scene
with ui.scene(on_click=handle_click) as scene:
    robot = rosys.ui.robot_object(debug=True)
ui.label('hold SHIFT to steer with the keyboard arrow keys')



# start
ui.run(title='RoSys', port=8090)

