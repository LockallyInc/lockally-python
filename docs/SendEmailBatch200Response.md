# SendEmailBatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BatchResult]**](BatchResult.md) |  | [optional] 

## Example

```python
from lockally.models.send_email_batch200_response import SendEmailBatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailBatch200Response from a JSON string
send_email_batch200_response_instance = SendEmailBatch200Response.from_json(json)
# print the JSON string representation of the object
print(SendEmailBatch200Response.to_json())

# convert the object into a dict
send_email_batch200_response_dict = send_email_batch200_response_instance.to_dict()
# create an instance of SendEmailBatch200Response from a dict
send_email_batch200_response_from_dict = SendEmailBatch200Response.from_dict(send_email_batch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


