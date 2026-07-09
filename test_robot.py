from Restricted_Robot import Robot
rule = [[2, 1], [1, -2]]
robot = Robot(rule)
robot.find_constants([[4, 2]])

print(robot.constants)
print(robot.movement_generator([[4, 2]]))
