import pandas as pd
from dagster import asset, OpExecutionContext, MetadataValue


@asset(
    group_name="example",
    key_prefix="example",
)
def hello_world_data(context: OpExecutionContext) -> pd.DataFrame:
    df = pd.DataFrame({"hello": ["world"]})
    return df


@asset(
    group_name="example",
    key_prefix="example",
)
def rainbow_data(context: OpExecutionContext, hello_world_data: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame({"hello": ["rainbow"]})
    df = pd.concat([hello_world_data, df], ignore_index=True)

    # Add metadata to the asset
    context.add_output_metadata(
        {
            "num_records": len(df),
            "preview": MetadataValue.md(df.tail(30).to_markdown()),
        }
    )

    return df
