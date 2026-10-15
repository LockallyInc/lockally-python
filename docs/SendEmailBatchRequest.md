# SendEmailBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[SendMessage]**](SendMessage.md) |  | 

## Example

```python
from lockally.models.send_email_batch_request import SendEmailBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailBatchRequest from a JSON string
send_email_batch_request_instance = SendEmailBatchRequest.from_json(json)
# print the JSON string representation of the object
print(SendEmailBatchRequest.to_json())

# convert the object into a dict
send_email_batch_request_dict = send_email_batch_request_instance.to_dict()
# create an instance of SendEmailBatchRequest from a dict
send_email_batch_request_from_dict = SendEmailBatchRequest.from_dict(send_email_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


