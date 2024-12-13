import rospy
from symbolic_repair_msgs.msg import AtomicProposition, TerrainAndRequestStates, OnlineRepairResult
from symbolic_repair_msgs.srv import OnlineRepairWithNewTerrainAndRequest, OnlineRepairWithNewTerrainAndRequestResponse
from std_msgs.msg import Bool

def terrain_state_callback(req):
  print("Received request")
  print(req.terrain_request_states)
  res = OnlineRepairWithNewTerrainAndRequestResponse()
  res.repair_result = OnlineRepairResult()
  res.repair_result.repair_needed = True
  res.repair_result.slugsin_location = "/home/zzhou387/code/trajopt_ws/src/reactive_gait_planner/scripts/5x5_go2_with_obstacle_8_terrain_specs/5x5_go2_with_obstacle_8_terrain_modulo_0.slugsin"
  print("Sending response")
  print(res)
  return res
  
  
#==============================
#             Main
#==============================
if __name__ == '__main__':
  rospy.init_node('fake_online_repair_node')
  service = rospy.Service('/symbolic_repair/online_repair', OnlineRepairWithNewTerrainAndRequest, terrain_state_callback)
  print("Ready to take new terrain states for online repair")
  rospy.spin()