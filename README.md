# Symbolic repair messages
This repo includes the ROS message types used by the symbolic suggestions in the symbolic repair process. It also includes the feasibility checking and online repair services.

## Usage (test symbolic repair feasibility checking)
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
rosrun symbolic_repair_msgs fake_repair_node.py
```

## Usage (test online repair with new terrain and request states)
A unitest can be run.
1. Start the roscore
```bash
roscore
```

2. Run the fake online repair
```bash
rosrun symbolic_repair_msgs fake_online_repair_node.py
```

3. Run the fake online execution that updates the terrain state
```bash
rosrun symbolic_repair_msgs fake_online_execution_node.py
```