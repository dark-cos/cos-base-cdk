import aws_cdk as core
import aws_cdk.assertions as assertions

from cos_base_cdk.cos_base_cdk_stack import CosBaseCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cos_base_cdk/cos_base_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CosBaseCdkStack(app, "cos-base-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
