# /*
#  * Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  * SPDX-License-Identifier: MIT-0
#  *
#  * Permission is hereby granted, free of charge, to any person obtaining a copy of this
#  * software and associated documentation files (the "Software"), to deal in the Software
#  * without restriction, including without limitation the rights to use, copy, modify,
#  * merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
#  * permit persons to whom the Software is furnished to do so.
#  *
#  * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#  * PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#  * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#  * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#  * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#  */

import os
import boto3


def lambda_handler(event, context):

    lookoutforvision_client = boto3.client("lookoutvision")

    projectname = os.environ["lookoutforvision_project_name"]
    projectmodelversion = os.environ["lookoutforvision_project_model_version"]
    client_token = os.environ["clientToken"]
    # running_states = ['HOSTED']

    # Check if already running
    try:
        isrunning_response = lookoutforvision_client.describe_model(
            ProjectName=projectname, ModelVersion=projectmodelversion
        )
    except Exception as e:
        print(e)

    running_status = isrunning_response["ModelDescription"]["Status"]
    if running_status == "HOSTED":
        # Stop Model
        try:
            running_status = lookoutforvision_client.stop_model(
                ProjectName=projectname,
                ModelVersion=projectmodelversion,
                ClientToken=client_token,
            )
        except Exception as e:
            print(e)
        # print('Model Status: %s' % running_status['Status'])
    else:
        # If not running - Do Nothing
        print("Model Start Status: %s" % running_status["Status"])
    return running_status["Status"]
