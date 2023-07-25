# NOTE: THIS IS NO LONGER USED

import os

from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = "handyguide"
    account_key = os.environ["AZURE_ACCOUNT_KEY"]
    azure_container = "handouts"
    expiration_secs = None
    
