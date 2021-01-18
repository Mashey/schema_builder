# Schema Builder :: Database

This pull request adds several modules that enable `JSON Schemas` to be created from a `ddl.txt` file, or from a SQL `DESCRIBE FORMATTED table_name` query.

- The `ddl.txt` file used for testing was exported from [DBeaver](https://dbeaver.io/).
- The `DESCRIBE FORMATTED table_name` query used for testing was obtained using [PEP 249](https://www.python.org/dev/peps/pep-0249/).

## Use

The application is structured for ease of use as a PyPi package. The `JSON Schemas` are created at the following path:

- `current_project/json_schemas`

Only a single function needs to be imported to use the Schema Builder:

```python
from schema_builder import build_json_schema
```

Currently the `build_json_schema()` function supports 2 source types:

- `ddl`
- `table`

### Create a `JSON Schema` from a `ddl.txt` file:

```python
# The .txt file should be in the project root directory

build_json_schema('ddl', file='ddl_file_name.txt')
```

### Create a `JSON Schema` from a SQL `DESCRIBE FORMATTED table_name` query:

```python
build_json_schema('table', data=query, table_name='table_name')
```
