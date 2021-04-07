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

    # State (string) -- The state of the event source mapping.
    # It can be one of: Creating, Enabling, Enabled, Disabling, Disabled, Updating or Deleting.
    disabled_states = ["Disabled", "Disabling"]
    enabled_states = ["Enabling", "Enabled"]

    analyse_lambda_uuid = os.environ["analyze_lambda_uuid"]
    action = event[0]["Action"]
    lambda_client = boto3.client("lambda")

    try:
        response = lambda_client.get_event_source_mapping(UUID=analyse_lambda_uuid)
        current_state = response["State"]
        needs_disabling = action == "disable" and current_state not in disabled_states
        needs_enabling = action == "enable" and current_state not in enabled_states

        if needs_disabling or needs_enabling:
            response = lambda_client.update_event_source_mapping(
                UUID=analyse_lambda_uuid, Enabled=needs_enabling
            )
            current_state = response["State"]

        print("Current state is: ", current_state)
        return current_state

    except Exception as e:
        print(e)
