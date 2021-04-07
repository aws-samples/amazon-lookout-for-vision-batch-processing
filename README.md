
# Batch Image Processing with Amazon Lookout for Vision

Amazon Lookout for Vision is a machine learning (ML) service that spots defects and anomalies in visual representations using computer vision (CV). With Amazon Lookout for Vision, manufacturing companies can increase quality and reduce operational costs by quickly identifying differences in images of objects at scale. For example, Amazon Lookout for Vision can be used to identify missing components in products, damage to vehicles or structures, irregularities in production lines, miniscule defects in silicon wafers, and other similar problems.

Amazon Lookout for Vision uses ML to see and understand images from any camera as a person would, but with an even higher degree of accuracy and at a much larger scale. Amazon Lookout for Vision allows you to eliminate the need for costly and inconsistent manual inspection, while improving quality control, defect and damage assessment, and compliance. In minutes, you can begin using Amazon Lookout for Vision to automate inspection of images and objects–with no machine learning expertise required.

>Step 1: Collect images that show normal and defective products from your production line and load them in to the Amazon Lookout for Vision console.

>Step 2: Label images as normal or anomalous and Lookout for Vision will automatically build a model for you in minutes. Tune your model to improve defect detection by adding images to the dataset.

>Step 3: Use the Amazon Lookout for Vision dashboard to monitor defects and improve processes.

>Step 4: Automate visual inspection processes real-time or in-batch and receive notifications when defects are detected.

>Step 5: Make continuous improvements by providing feedback on the identified product defects.

In this solution, we show how you can build cost-optimal batch solution with Amazon Lookout for Vision which provision your custom model at scheduled times, process all your images, and then deprovision your resources to avoid incurring extra cost.
In this code sample, we show how you can build cost-optimal batch solution with Amazon Lookout for Vision which provision your custom model at scheduled times, process all your images, and then deprovision your resources to avoid incurring extra cost.

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI or using the Cloudformation links below. It includes the following files and folders:

> - /functions - Code for the application's Lambda functions to check the presence of messages in a Queue, start or stop a Amazon Lookout for Vision Model, Analyse Images using your Model.
> - template.yaml - A template that defines the application's AWS resources.

This application creates a serverless Amazon Lookout for Vision Detection workflow which runs on a pre-defined schedule (note that the schedule is enabled by default at deployment). It demonstrates the power of Step Functions to orchestrate Lambda functions and other AWS resources to form complex and robust workflows, coupled with event-driven development using Amazon EventBridge.

Solution Architecture Diagram: The following architecture diagram shows how you can design a serverless workflow to process images in batches with Amazon Lookout for Vision Model.

<img width="814" alt="Architecture Diagram" src="docs/SA-Amazon Lookout for Vision Batch Image Processing.png">


Step Functions state machine:

The following image show the Step Functions state machine used to orchestrate the solution. 

<img width="514" alt="Architecture Diagram" src="docs/SA-State machine for Amazon Lookout for Vision Batch processing.png">

### Usage

#### Prerequisites

1. To deploy the sample application, you will require an AWS account. If you don’t already have an AWS account, create one at <https://aws.amazon.com> by following the on-screen instructions. Your access to the AWS account must have IAM permissions to launch AWS CloudFormation templates that create IAM roles.

2. Please refer [here](https://docs.aws.amazon.com/lookout-for-vision/) for instructions on getting started with Amazon Lookout for Vision. When deploying this application you will need to provide the following two parameters for your Lookout for Vision Project.
   - Amazon Lookout for Vision Project Name: The name of the Amazon Lookout for Vision project that contains the models you want to use. This project should be in the same region where you are deploying the solution.
   - Amazon Lookout for Vision Model Version: The number (or latest) of the model version that you want to use.


#### Deployment

The demo application is deployed as an [AWS CloudFormation](https://aws.amazon.com/cloudformation) template.

> **Note**  
> You are responsible for the cost of the AWS services used while running this sample deployment. There is no additional cost for using this sample. For full details, see the following pricing pages for each AWS service you will be using in this sample. Prices are subject to change.
>
> - [Amazon Lookout for Vision Pricing](https://aws.amazon.com/lookout-for-vision/pricing/)
> - [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)
> - [Amazon SQS Pricing](https://aws.amazon.com/sqs/pricing/)
> - [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/)
> - [AWS Step Functions Pricing](https://aws.amazon.com/step-functions/pricing/)

1. Deploy the latest CloudFormation template by following the link below for your preferred AWS region:

| Region                                | Launch Template                                                                                                                                                                                                                                                                                     |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **US East (N. Virginia)** (us-east-1) | [![Launch the AnomalyDetection Stack with CloudFormation](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=AnomalyDetection&templateURL=https://solution-builders-us-east-1.s3.us-east-1.amazonaws.com/amazon-lookout-for-vision-batch-processing/latest/template.yaml) |
| **US East (Ohio)** (us-east-2)        | [![Launch the AnomalyDetection Stack with CloudFormation](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=AnomalyDetection&templateURL=https://solution-builders-us-east-2.s3.us-east-2.amazonaws.com/amazon-lookout-for-vision-batch-processing/latest/template.yaml) |
| **US West (Oregon)** (us-west-2)      | [![Launch the AnomalyDetection Stack with CloudFormation](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=AnomalyDetection&templateURL=https://solution-builders-us-west-2.s3.us-west-2.amazonaws.com/amazon-lookout-for-vision-batch-processing/latest/template.yaml) |
| **EU (Ireland)** (eu-west-1)          | [![Launch the AnomalyDetection Stack with CloudFormation](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=AnomalyDetection&templateURL=https://solution-builders-eu-west-1.s3.eu-west-1.amazonaws.com/amazon-lookout-for-vision-batch-processing/latest/template.yaml) |

2. If prompted, login using your AWS account credentials.
3. You should see a screen titled "_Create Stack_" at the "_Specify template_" step. The fields specifying the CloudFormation template are pre-populated. Click the _Next_ button at the bottom of the page.
4. On the "_Specify stack details_" screen you may customize the following parameters of the CloudFormation stack:

   - **Stack Name:** (Default: AnomalyDetection) This is the name that is used to refer to this stack in CloudFormation once deployed.
   - **lookoutforvisionProjectName:** The Amazon Lookout for Vision Model Project Name
   - **lookoutforvisionProjectModelVersion:** The Amazon Lookout for Vision Model Project Version
   - **minimumInferenceUnitsToUse:** Minimum number of inference units to use
   - **clientToken:** Optional idempotency token string that ensures a call to StartModel completes only once

   When completed, click _Next_

5. [Configure stack options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.html) if desired, then click _Next_.
6. On the review you screen, you must check the boxes for:

   - "_I acknowledge that AWS CloudFormation might create IAM resources_"
   - "_I acknowledge that AWS CloudFormation might create IAM resources with custom names_"
   - "_I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND_"

   These are required to allow CloudFormation to create a Role to allow access to resources needed by the stack and name the resources in a dynamic way.

7. Click _Create Change Set_
8. On the _Change Set_ screen, click _Execute_ to launch your stack.
   - You may need to wait for the _Execution status_ of the change set to become "_AVAILABLE_" before the "_Execute_" button becomes available.
9. Wait for the CloudFormation stack to launch. Completion is indicated when the "Stack status" is "_CREATE_COMPLETE_".
   - You can monitor the stack creation progress in the "Events" tab.
10. Note the _url_ displayed in the _Outputs_ tab for the stack. This is used to access the application.

#### Testing the workflow

To test your workflow, complete the following steps:
1. Upload sample images to the input S3 bucket that was created by the solution (Example: xxxx-sources3bucket-xxxx).
2. Go to AWS Step Function console and select the state machine created by the solution (Example: CustomCVStateMachine-xxxx). You will see an execution triggered by the EventBridge at every hour.
3. To test the solution, you can also manually start the workflow by clicking on the “Start execution” button.
4. As images are processed you can go to the output S3 bucket (Example: xxxx-finals3bucket-xxxx) to see the JSON output for each image. The Final S3 bucket holds the images that have been processed along with the inferenced anomaly detection json. As the images get processed, they will be deleted from the source bucket.


### Removing the application

To remove the application open the AWS CloudFormation Console, click on the name of the project, right-click and select "_Delete Stack_". Your stack will take some time to be deleted. You can track its progress in the "Events" tab. When it is done, the status will change from "_DELETE_IN_PROGRESS_" to "_DELETE_COMPLETE_". It will then disappear from the list. 

**Note:** Please note that the provided configuration will ensure that the Amazon S3 buckets and their contents are retained when removing the application via the AWS Cloudformation console. This is to ensure that no data is accidently lost while removing the application. The buckets can be deleted from the S3 console.


## License
     
This library is licensed under the MIT-0 License. See the LICENSE file.
