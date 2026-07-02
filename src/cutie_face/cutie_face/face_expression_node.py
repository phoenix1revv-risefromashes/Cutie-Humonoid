import rclpy
from rclpy.node import Node

from cutie_interfaces.msg import ExpressionCommand

import time

class FaceExpressionNode(Node):
    def __init__(self):
        super().__init__('face_expression_node')

        
        self.face_expression_subsriber = self.create_subscription(
            msg_type=ExpressionCommand,
            topic="cutie/expression/command",
            callback=self.handle_expression_command,
            qos_profile=10,
        )

        self.expression_names={
            ExpressionCommand.IDLE: "IDLE",
            ExpressionCommand.LISTENING: "LISTENING",
            ExpressionCommand.SPEAKING: "SPEAKING",
            ExpressionCommand.THINKING: "THINKING",
            ExpressionCommand.HAPPY: "HAPPY",
            ExpressionCommand.CONFUSED: "CONFUSED",
            ExpressionCommand.ERROR: "ERROR",
            ExpressionCommand.SLEEPY: "SLEEPY",
            ExpressionCommand.CURIOUS: "CURIOUS",
            ExpressionCommand.EXCITED: "EXCITED",
            ExpressionCommand.SMUG: "SMUG"
        }
        
        # The parameters for this node are declared here :
        self.declare_parameter("default_duration_sec", 2.0)
        self.declare_parameter("state_timer_period_sec",0.1 )
        self.declare_parameter("default_idle_priority",0)
        self.declare_parameter("allow_full_body_commands", True)

        self.default_duration_sec :float = self.get_parameter("default_duration_sec").value
        self.state_timer_period_sec : float = self.get_parameter("state_timer_period_sec").value
        self.default_idle_priority: int = self.get_parameter("default_idle_priority").value
        self.allow_full_body_commands: bool = self.get_parameter("allow_full_body_commands").value

        # This defines the cutie's active default face state on screen
        self.current_expression_id : int = ExpressionCommand.IDLE
        self.current_priority : int = self.default_idle_priority
        self.current_intensity : float = 0.0
        self.current_source : str = "startup"
        self.current_detail : str = "default idle state"
        self.expression_expire_time : float = 0.0
        
        # This timer will revert back every temporary facial expression to default expression: IDLE
        self.state_timer = self.create_timer(timer_period_sec=self.state_timer_period_sec,
                                             callback=self.update_expression_state)
        
        self.get_logger().info("Cutie Face Expression Node has iniated. Listening on /cutie/expression/command")


    def update_expression_state(self) -> None:
        '''
        This method reverts every temporary facial expressions to default IDLE face after expression_expire_time
        '''
        if self.current_expression_id == ExpressionCommand.IDLE:
            return
        
        current_time = time.monotonic()
        if current_time < self.expression_expire_time:
            return
        
        expired_expression = self.get_expression_name(self.current_expression_id)
        
        self.current_expression_id = ExpressionCommand.IDLE
        self.current_priority = self.default_idle_priority
        self.current_intensity = 0.0
        self.current_source = "face_state_timer"
        self.current_detail = "expression duration expired"
        self.expression_expire_time = 0.0
        
        self.get_logger().info(
            f"Expression Expired: {expired_expression} | Returning to IDLE"
        )



    def get_expression_name(self, expression_id:int)->str:
        return self.expression_names.get(expression_id, f"Unknown ID: {expression_id}")

   
    def handle_expression_command(self, msg:ExpressionCommand) -> None:
        """
        Handle an incoming face expression command.

        This callback only routes the command:
        it decides whether Cutie should accept the expression,
        then applies it only if the command passes the decision rules.
        """
        if not self.should_cutie_accept_face_expression_command(msg=msg):
            self.get_logger().info("The cutie did not accept the expression command")
            return
        
        self.apply_face_expression_command(msg=msg)


    # This checks if the incoming expression command is meant for and accepted by cutie face. 
    def should_cutie_accept_face_expression_command(self, msg:ExpressionCommand) -> bool:
        ''' The cutie_face accepts the face expression when:
                1. Target Id is 0 (i.e. meant for face as defined in ExpressionCommand) or Full-body if full body
                    participation is enabled
                
                AND

                2. Priority of the command is higher than the current cutie_face_state_priority 
        '''
        
        allowed_targets = [ExpressionCommand.TARGET_FACE]

        if self.allow_full_body_commands:
            allowed_targets.append(ExpressionCommand.TARGET_FULL_BODY)

        if msg.target_id not in allowed_targets:
            return False
        if msg.priority<self.current_priority:
            return False
        
        return True
    
    
    def apply_face_expression_command(self, msg:ExpressionCommand) -> None:
        expression_name = self.get_expression_name(expression_id=msg.expression_id)

        self.current_expression_id = msg.expression_id
        self.current_priority = msg.priority
        self.current_intensity = msg.intensity
        self.current_detail = msg.detail
        self.current_source = msg.source
        
        duration_sec = msg.duration_sec

        if duration_sec<=0:
            duration_sec = self.default_duration_sec
        
        self.expression_expire_time = time.monotonic() + duration_sec

        self.get_logger().info(
            "Expression command accepted | "
            f"expression={expression_name}, "
            f"intensity={self.current_intensity}, "
            f"duration_sec={duration_sec}, "
            f"priority={self.current_priority}, "
            f"source={self.current_source}, "
            f"detail={self.current_detail}"
        )

        

        
def main(args=None):
    rclpy.init(args=args)
    node= FaceExpressionNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__=="__main__":
    main()


