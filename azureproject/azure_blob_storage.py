from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def initialize_blob_service_client():
    connection_string = "DefaultEndpointsProtocol=https;AccountName=learningstor;AccountKey=e+5a4V5IvC0q+q/phGvA1wHP3e5JSBZGAuf9FIPN7PXAFgTcCA1jP+lbhCr4meLbxLQhceS9ZoPO+AStFI5ZFQ==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    return blob_service_client

def upload_file_to_blob_storage(blob_service_client, container_name, file_path, blob_name):
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

def retrieve_file_from_blob_storage(blob_service_client, container_name, blob_name, local_file_path):
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    with open(local_file_path, "wb") as data:
        data.write(blob_client.download_blob().readall())


# Replace 'C:\\Users\\Sfundo Nondwatyu\\OneDrive\\Documents\\Mashauri\\Isixhosa Book.pdf' with the actual file path
file_path = "C:\\Users\\Sfundo Nondwatyu\\OneDrive\\Documents\\Mashauri\\Isixhosa Book.pdf"

blob_service_client = initialize_blob_service_client()
container_name = "elearningcontent"

blob_name = "books"


# Call the upload_file_to_blob_storage function
upload_file_to_blob_storage(blob_service_client, container_name, file_path, blob_name)