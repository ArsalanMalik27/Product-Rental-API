import json
import pydantic.json

def _custom_json_serializer(*args, **kwargs) -> str:
    return json.dumps(*args, default=pydantic.json.pydantic_encoder, **kwargs)