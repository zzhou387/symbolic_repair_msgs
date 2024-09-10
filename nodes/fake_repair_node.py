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
  ap2.atomic_proposition = ["x1", "1"]
  ap3 = AtomicProposition()
  ap3.atomic_proposition = ["x2", "0"]
  ap4 = AtomicProposition()
  ap4.atomic_proposition = ["y0", "0"]
  ap5 = AtomicProposition()
  ap5.atomic_proposition = ["y1", "1"]
  ap6 = AtomicProposition()
  ap6.atomic_proposition = ["y2", "0"]
  skill1.initial_preconditions = [ap1, ap2, ap3, ap4, ap5, ap6]
  for x in range(3):
    for y in range(3):
      if x == 1 and y == 0:
        terrain_state = 1
      else:
        terrain_state = 0
      for t in range(2):
        if t == terrain_state:
          ap_state = "1"
        else:
          ap_state = "0"
        ap = AtomicProposition()
        ap.atomic_proposition = ["x_"+str(x)+"_y_"+str(y)+"_terrain"+str(t),
                                 ap_state]
        skill1.initial_preconditions.append(ap)
      
  
  # intermediate_state = State()
  # intermediate_state.precondition = ["x0", "y0"]
  # intermediate_state.postcondition = ["x1", "y0"]
  # skill1.intermediate_states = [intermediate_state]
  
  ap7 = AtomicProposition()
  ap7.atomic_proposition = ["x0", "0"]
  ap8 = AtomicProposition()
  ap8.atomic_proposition = ["x1", "1"]
  ap9 = AtomicProposition()
  ap9.atomic_proposition = ["x2", "0"]
  ap10 = AtomicProposition()
  ap10.atomic_proposition = ["y0", "1"]
  ap11 = AtomicProposition()
  ap11.atomic_proposition = ["y1", "0"]
  ap12 = AtomicProposition()
  ap12.atomic_proposition = ["y2", "0"]
  skill1.final_postconditions = [ap7, ap8, ap9, ap10, ap11, ap12]
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
  