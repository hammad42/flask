
import io
from io import BytesIO
from google.cloud import storage



storage_client = storage.Client.from_service_account_json("fourth-elixir-273216-06b58e3308db.json")



bucket= storage_client.get_bucket("greenertronics-42")

filename = "%s/%s" % ('',"ha42ms.txt")
blob =bucket.blob(filename)

with open('hams.txt','rb') as f:
    blob.upload_from_file(f)
print("upload")
