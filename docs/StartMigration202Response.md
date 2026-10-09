# StartMigration202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**mailboxes_queued** | **int** |  | 

## Example

```python
from lockally.models.start_migration202_response import StartMigration202Response

# TODO update the JSON string below
json = "{}"
# create an instance of StartMigration202Response from a JSON string
start_migration202_response_instance = StartMigration202Response.from_json(json)
# print the JSON string representation of the object
print(StartMigration202Response.to_json())

# convert the object into a dict
start_migration202_response_dict = start_migration202_response_instance.to_dict()
# create an instance of StartMigration202Response from a dict
start_migration202_response_from_dict = StartMigration202Response.from_dict(start_migration202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


