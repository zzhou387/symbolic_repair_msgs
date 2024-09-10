import rospy
from symbolic_repair_msgs.msg import AtomicProposition, TerrainState
from symbolic_repair_msgs.srv import OnlineRepairWithNewTerrain, OnlineRepairWithNewTerrainResponse

if __name__ == '__main__':
  rospy.init_node('fake_online_execution_node')
  rospy.wait_for_service('fake_online_repair')
  online_repair = rospy.ServiceProxy('fake_online_repair', OnlineRepairWithNewTerrain)
  new_terrain = TerrainState()
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
        new_terrain.terrain_state.append(ap)
      
  new_terrain.header.stamp = rospy.Time.now()
  
  rate = rospy.Rate(0.5)
  
  while not rospy.is_shutdown():
    try:
      resp = online_repair(new_terrain)
      if resp.repair_result.repair_needed:
        print(resp.repair_result.slugsin_location)
      else:
        print("No repair needed")
    except rospy.ServiceException as e:
      print("Service call failed: %s"%e)
    rate.sleep()
  