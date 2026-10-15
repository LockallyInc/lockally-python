# SendEmail202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Lockally identifier; use with GET /v1/messages/{id}. | 
**message_id** | **str** | RFC 5322 Message-ID (with angle brackets). | 
**status** | **str** | \&quot;scheduled\&quot; when send_at is in the future. | 
**warning** | **str** |  | [optional] 

## Example

```python
from lockally.models.send_email202_response import SendEmail202Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmail202Response from a JSON string
send_email202_response_instance = SendEmail202Response.from_json(json)
# print the JSON string representation of the object
print(SendEmail202Response.to_json())

# convert the object into a dict
send_email202_response_dict = send_email202_response_instance.to_dict()
# create an instance of SendEmail202Response from a dict
send_email202_response_from_dict = SendEmail202Response.from_dict(send_email202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


