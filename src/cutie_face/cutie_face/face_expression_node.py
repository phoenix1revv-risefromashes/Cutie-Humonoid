import rclpy
from rclpy.node import Node

from cutie_interfaces.msg import ExpressionCommand

class FaceExpressionNode(Node):
    def __init__(self):
        super().__init__('face_expression_node')
        
        self.face_expression_subsriber = self.create_subscription(
            msg_type=ExpressionCommand,
            topic="cutie/expression/command",
            callback=self.handle_expression_command,
            qos_profile=10,
        )

        self.get_logger().info("Cutie Face Expression Node has iniated. Listening on /cutie/expression/command")

   
    def handle_expression_command(self, msg):
        """
        The communication format used will be the one we custom-built: 
                "cutie_interfaces/msg/Expressioncommand"
        """

        self.get_logger().info("Expression command received: | "
                               f"target_id={msg.target_id}, "
                               f"expression_id={msg.expression_id}, "
                               f"intensity={msg.intensity}, "
                               f"duration_sec={msg.duration_sec}, "
                               f"priority={msg.priority}, "
                               f"source={msg.source}, "
                               f"detail: {msg.detail}, "
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


