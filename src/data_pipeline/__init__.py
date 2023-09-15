from dagster_aws.s3.resources import s3_resource
from dagster_aws.s3.io_manager import s3_pickle_io_manager
from dotenv import load_dotenv
from dagster import Definitions, define_asset_job, load_assets_from_package_module, ExperimentalWarning
from data_pipeline import assets
import os
import warnings

# Ignore "AutoMaterialization" ExperimentalWarning from Dagster
warnings.filterwarnings("ignore", category=ExperimentalWarning)

load_dotenv()


resources = {
    # With this I/O manager in place, your job runs will store data passed between assets
    # on S3 in the location s3://<bucket>/dagster/storage/<asset key>.
    "io_manager": s3_pickle_io_manager.configured({"s3_bucket": {"env": "S3_BUCKET"}}),
    "s3": s3_resource,
}

defs = Definitions(
    assets=load_assets_from_package_module(assets),
    jobs=[],
    # The AWS resources use boto under the hood, so if you are accessing your private
    # buckets, you will need to provide the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
    # environment variables or follow one of the other boto authentication methods.
    # Read about using environment variables and secrets in Dagster:
    #   https://docs.dagster.io/guides/dagster/using-environment-variables-and-secrets
    resources=resources,
)
