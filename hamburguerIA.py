import json
import watson_developer_cloud

conversation = watson_developer_cloud.ConversationV1(
    username='{3742702-5bc2-479c-b92a-d9ea77ef46d1}',
    password='{Sr1A8CI3fS2U}',
    version='2018-02-16'
)

response = conversation.list_workspaces()

print(json.dumps(response, indent=2))