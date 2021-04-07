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
    project_name = os.environ["lookoutforvision_project_name"]
    project_model_version = os.environ["lookoutforvision_project_model_version"]

    try:
        running_states = ["HOSTED", "STARTING_HOSTING"]
        response = lookoutforvision_client.describe_model(
            ProjectName=project_name, ModelVersion=project_model_version
        )

        running_status = response["ModelDescription"]["Status"]

        if running_status not in running_states:
            response = lookoutforvision_client.start_model(
                ProjectName=project_name,
                ModelVersion=project_model_version,
                MinInferenceUnits=int(
                    os.environ["minimumInferenceUnitsToUse"]
                ),  # Can be increased upto 5 for running multiple inference units
                ClientToken=os.environ["clientToken"],
            )
            running_status = response["Status"]

        print("Current state is: ", running_status)
        return running_status

    except Exception as e:
        print(e)
