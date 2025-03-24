import rospy
from symbolic_repair_msgs.msg import AtomicProposition, TerrainAndRequestStates, OnlineRepairResult
from symbolic_repair_msgs.srv import OnlineRepairWithNewTerrainAndRequest, OnlineRepairWithNewTerrainAndRequestResponse

if __name__ == '__main__':
  rospy.init_node('fake_online_execution_node')
  rospy.wait_for_service('/symbolic_repair/online_repair')
  online_repair = rospy.ServiceProxy('/symbolic_repair/online_repair', OnlineRepairWithNewTerrainAndRequest)
  new_terrain = []
  new_terrain_request = TerrainAndRequestStates()
  # for x in range(3):
  #   for y in range(3):
  #     terrain_ap = AtomicProposition()
  #     if x == 1 and y == 0:
  #       terrain_state = "1"
  #     else:
  #       terrain_state = "0"
  #     terrain_ap.atomic_proposition = ["x_"+str(x)+"_y_"+str(y)+"_terrain",
  #                                       terrain_state]
  #     new_terrain.append(terrain_ap)
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_0_y_0_terrain",
                                   "1"]
  new_terrain.append(terrain_ap)
  
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_0_y_1_terrain",
                                   "8"]
  new_terrain.append(terrain_ap)
  
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_0_y_2_terrain",
                                   "1"]
  new_terrain.append(terrain_ap)
  
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_1_y_0_terrain",
                                   "1"]
  new_terrain.append(terrain_ap)
  
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_1_y_1_terrain",
                                   "4"]
  new_terrain.append(terrain_ap)
  
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_1_y_2_terrain",
                                   "1"]
  new_terrain.append(terrain_ap)
  
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_2_y_0_terrain",
                                   "1"]
  new_terrain.append(terrain_ap)
  
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_2_y_1_terrain",
                                   "1"]
  new_terrain.append(terrain_ap)
  
  terrain_ap = AtomicProposition()
  terrain_ap.atomic_proposition = ["x_2_y_2_terrain",
                                   "1"]
  new_terrain.append(terrain_ap)

  x_request = AtomicProposition()
  x_request.atomic_proposition = ["xrequest", "0"]
  y_request = AtomicProposition()
  y_request.atomic_proposition = ["yrequest", "1"]
  new_request = [x_request, y_request]
  
  invalid_trans_pre_x = AtomicProposition()
  invalid_trans_pre_x.atomic_proposition = ["x", "1"]
  invalid_trans_pre_y = AtomicProposition()
  invalid_trans_pre_y.atomic_proposition = ["y", "1"]
  invalid_trans_pre = [invalid_trans_pre_x, invalid_trans_pre_y]
  
  invalid_trans_post_x = AtomicProposition()
  invalid_trans_post_x.atomic_proposition = ["x", "0"]
  invalid_trans_post_y = AtomicProposition()
  invalid_trans_post_y.atomic_proposition = ["y", "1"]
  invalid_trans_post = [invalid_trans_post_x, invalid_trans_post_y]
  

  new_terrain_request.terrain_state = new_terrain
  new_terrain_request.request_state = new_request
  new_terrain_request.invalid_transition_pre = invalid_trans_pre
  new_terrain_request.invalid_transition_post = invalid_trans_post
  new_terrain_request.header.stamp = rospy.Time.now()
  
  rate = rospy.Rate(0.5)
  
  while not rospy.is_shutdown():
    try:
      resp = online_repair(new_terrain_request)
      if resp.repair_result.repair_needed:
        print(resp.repair_result.slugsin_location)
      else:
        print("No repair needed")
    except rospy.ServiceException as e:
      print("Service call failed: %s"%e)
    rate.sleep()
  