import rospy
from symbolic_repair_msgs.msg import SkillArray, Skill, State, AtomicProposition, FeasibilityArray, Feasibility
from symbolic_repair_msgs.srv import FeasibilityCheck, FeasibilityCheckResponse
from std_msgs.msg import Bool

def symbolic_suggestion_callback(req):
  print("Received request")
  print(req.skills_requested)
  res = FeasibilityCheckResponse()
  fea = FeasibilityArray()
  for skill in req.skills_requested.skills:
    fea.feasibilities.append(Feasibility(skill.name, True))
  res.feasibilities_checked = fea
  print("Sending response")
  print(res.feasibilities_checked)
  return res
  
  
#==============================
#             Main
#==============================
if __name__ == '__main__':
  rospy.init_node('fake_feasibility_check_node')
  service = rospy.Service('fake_feasibility_check', FeasibilityCheck, symbolic_suggestion_callback)
  print("Ready to take symbolic suggestions")
  rospy.spin()