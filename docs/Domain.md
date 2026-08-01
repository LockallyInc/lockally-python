# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**domain** | **str** |  | 
**verification_token** | **str** |  | 
**verified** | **bool** |  | 
**verified_at** | **datetime** |  | [optional] 
**dkim_selector** | **str** |  | 
**dkim_public_record** | **str** |  | 
**created_at** | **datetime** |  | 
**records** | [**List[DNSRecord]**](DNSRecord.md) | DNS records the tenant must publish under their own DNS. | [optional] 

## Example

```python
from lockally.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


