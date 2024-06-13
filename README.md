# Symbolic repair messages
This repo includes the ROS message types used by the symbolic suggestions in the symbolic repair process. It also includes the feasibility checking feedback messages.

## Usage
A unitest can be run.
1. Start the roscore
```bash
roscore
```

2. Run the fake feasibility checker
```bash
rosrun symbolic_repair_msgs fake_feasibility_check_node.py
```

3. Run the fake repair suggestion
```bash
rosrun symbolic_repair_msgs fake_repair_suggestion_node.py
```