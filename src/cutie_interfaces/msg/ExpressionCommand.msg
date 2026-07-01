std_msgs/Header header

#Expression target IDs
uint8 TARGET_FACE=0
uint8 TARGET_HEAD=1
uint8 TARGET_BODY=2
uint8 TARGET_VOICE=3
uint8 TARGET_FULL_BODY=4

#FaceExpressions IDs
uint8 IDLE=0
uint8 LISTENING=1
uint8 SPEAKING=2
uint8 THINKING=3
uint8 HAPPY=4
uint8 CONFUSED=5
uint8 ERROR=6
uint8 SLEEPY=7
uint8 CURIOUS=8
uint8 EXCITED=9
uint8 SMUG=10

#which expression system should respond
uint8 target_id

#which expression to express
uint8 expression_id


#Expression Strength
#0.0=no expression, 1.0=full expression
float32 intensity

#Duration of expression
#0.0 means the receiving node choses its default duration
float32 duration_sec

#higher priority expressions can override the lower priority action expressions
uint8 priority

#Node requesting this expression
string source



