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

    # Check if already running
    try:
        is_running = lookoutforvision_client.describe_model(
            ProjectName=projectname, ModelVersion=projectmodelversion
        )
    except Exception as e:
        print(e)

    running_status = is_running["ModelDescription"]["Status"]
    if running_status == "HOSTED":
        # Do nothing
        return "HOSTED"
    if running_status == "STARTING_HOSTING":
        # Do nothing
        return "STARTING_HOSTING"
    else:
        # If not running - Start
        try:
            running_status = lookoutforvision_client.start_model(
                ProjectName=projectname,
                ModelVersion=projectmodelversion,
                MinInferenceUnits=int(
                    os.environ["minimumInferenceUnitsToUse"]
                ),  # Can be increased upto 5 for running multiple inference units
                ClientToken=os.environ["clientToken"],
            )
            print("running_status: ", running_status["Status"])
        except Exception as e:
            print(e)
        return running_status["Status"]
