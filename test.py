from bigquery_helper import BigQueryHelper

if __name__ == "__main__":
    # Create an instance of the helper
    helper = BigQueryHelper(
        project_id="trim-field-444020-g8",
        dataset_id="todo_demo",
        table_id="tasks"
    )

    # Get and print the schema
    schema = helper.get_schema()
    print("Table Schema:")
    for field in schema:
        print(f"Name: {field.name}, Type: {field.field_type}, Mode: {field.mode}")

    # Run a sample query
    query = f"SELECT * FROM `{helper.project_id}.{helper.dataset_id}.{helper.table_id}` LIMIT 5;"
    output = helper.run_query(query)
    print("Query Results:")
    print(output)
