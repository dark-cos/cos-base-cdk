from aws_cdk import (
    Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as lambda_
)
from constructs import Construct

class CosBaseCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        lambda_function = lambda_.Function(
            self,
            "generic_function",
            code=lambda_.Code.from_asset('functions/generic_lambda'),
            handler="index.lambda_handler",
            timeout=Duration.seconds(10),
            runtime=lambda_.Runtime.PYTHON_3_9
        )

        # example resource
        # queue = sqs.Queue(
        #     self, "CosBaseCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
