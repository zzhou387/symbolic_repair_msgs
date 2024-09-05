import rospy
from symbolic_repair_msgs.msg import SkillArray, Skill, State, AtomicProposition, FeasibilityArray, Feasibility
from symbolic_repair_msgs.srv import FeasibilityCheck, FeasibilityCheckResponse

if __name__ == '__main__':
  rospy.init_node('fake_repair_node')
  rospy.wait_for_service('fake_feasibility_check')
  feasibility_check = rospy.ServiceProxy('fake_feasibility_check', FeasibilityCheck)
  Skills = SkillArray()
  skill1 = Skill()
  skill1.name = "skill1"
  ap1 = AtomicProposition()
  ap1.atomic_proposition = ["x0", "0"]
  ap2 = AtomicProposition()
  ap2.atomic_proposition = ["x1", "0"]
  skill1.initial_preconditions = [ap1, ap2]
  # intermediate_state = State()
  # intermediate_state.precondition = ["x0", "y0"]
  # intermediate_state.postcondition = ["x1", "y0"]
  # skill1.intermediate_states = [intermediate_state]
  
  ap3 = AtomicProposition()
  ap3.atomic_proposition = ["x0", "1"]
  ap4 = AtomicProposition()
  ap4.atomic_proposition = ["x1", "1"]
  skill1.final_postconditions = [ap3, ap4]
  Skills.skills = [skill1]
  Skills.header.stamp = rospy.Time.now()
  
  rate = rospy.Rate(0.5)
  
  while not rospy.is_shutdown():
    try:
      resp = feasibility_check(Skills)
      print(resp.feasibilities_checked)
    except rospy.ServiceException as e:
      print("Service call failed: %s"%e)
    rate.sleep()
  