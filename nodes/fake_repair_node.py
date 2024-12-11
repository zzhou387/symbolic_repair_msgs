import rospy
from symbolic_repair_msgs.msg import SkillPrimitiveArray, SkillPrimitive, State, AtomicProposition, FeasibilityArray, Feasibility
from symbolic_repair_msgs.srv import PrimitiveFeasibilityCheck, PrimitiveFeasibilityCheckResponse

if __name__ == '__main__':
  rospy.init_node('fake_repair_node')
  rospy.wait_for_service('fake_feasibility_check')
  feasibility_check = rospy.ServiceProxy('fake_feasibility_check', PrimitiveFeasibilityCheck)
  Skills = SkillPrimitiveArray()
  skill1 = SkillPrimitive()
  skill1.name = "skill1"
  skill1.dir = [1,0]
  skill1.current_terrain_type = 0
  skill1.next_terrain_type = 1
  
  Skills.primitives = [skill1]
  Skills.header.stamp = rospy.Time.now()
  
  rate = rospy.Rate(0.5)
  
  while not rospy.is_shutdown():
    try:
      resp = feasibility_check(Skills)
      print(resp.feasibilities_checked)
    except rospy.ServiceException as e:
      print("Service call failed: %s"%e)
    rate.sleep()
  