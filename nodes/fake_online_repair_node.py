import rospy
from symbolic_repair_msgs.msg import AtomicProposition, TerrainState, OnlineRepairResult
from symbolic_repair_msgs.srv import OnlineRepairWithNewTerrain, OnlineRepairWithNewTerrainResponse
from std_msgs.msg import Bool

def terrain_state_callback(req):
  print("Received request")
  print(req.terrain_state_requested)
  res = OnlineRepairWithNewTerrainResponse()
  res.repair_result = OnlineRepairResult()
  res.repair_result.repair_needed = True
  res.repair_result.slugsin_location = "slugsin_test.slugsin"
  print("Sending response")
  print(res)
  return res
  
  
#==============================
#             Main
#==============================
if __name__ == '__main__':
  rospy.init_node('fake_online_repair_node')
  service = rospy.Service('fake_online_repair', OnlineRepairWithNewTerrain, terrain_state_callback)
  print("Ready to take new terrain states for online repair")
  rospy.spin()