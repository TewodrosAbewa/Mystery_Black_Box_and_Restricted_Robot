from Restricted_Robot import Robot
rule = [[2, 1], [1, -2]]
robot = Robot(rule)
print(robot.find_constants([[4, 2]]))
mov = robot.movement_generator([[4, 2]])
print(mov)