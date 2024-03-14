import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from PIL import Image
import io

# Your Sentinel Hub client ID and client secret
client_id = 'fd06797c-d171-4acf-8c28-03f92a7280bb'
client_secret = 'lbfkwdDxd7LhXvyPpCX4UABsOrLJ59nb'

# Function to create an OAuth session for Sentinel Hub
def create_sentinel_session(client_id, client_secret):
    """
    Creates an OAuth session for Sentinel Hub.

    Parameters:
    - client_id: Your Sentinel Hub client ID.
    - client_secret: Your Sentinel Hub client secret.
    
    Returns:
    An OAuth2Session object.
    """
    auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://services.sentinel-hub.com/oauth/token', auth=auth)
    return oauth

# Function to fetch Sentinel-2 data using the Process API with additional parameters
def fetch_sentinel_data(oauth, bbox, time_range, max_cloud_coverage=20, bands=["B02", "B03", "B04"], format="image/tiff"):
    """
    Fetches Sentinel-2 data using the Process API with additional parameters.

    Parameters:
    - oauth: The OAuth session.
    - bbox: The bounding box for the area of interest (format: [minX, minY, maxX, maxY]).
    - time_range: The time range for which to fetch data (format: ('YYYY-MM-DD', 'YYYY-MM-DD')).
    - max_cloud_coverage: Maximum cloud coverage percentage (0-100).
    - bands: List of Sentinel-2 band names to include in the output.
    - format: Output format of the image.
    
    Returns:
    The response from the Process API.
    """
    process_api_url = 'https://services.sentinel-hub.com/api/v1/process'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {oauth.access_token}'
    }
    
    payload = {
        "input": {
            "bounds": {
                "bbox": bbox
            },
            "data": [{
                "type": "S2L1C",
                "dataFilter": {
                    "timeRange": {
                        "from": time_range[0],
                        "to": time_range[1]
                    },
                    "maxCloudCoverage": max_cloud_coverage
                }
            }]
        },
        "output": {
            "responses": [
                {
                    "identifier": "default",
                    "format": {
                        "type": format
                    }
                }
            ]
        },
        "evalscript": f"""
            //VERSION=3
            function setup() {{
                return {{
                    input: [{{
                        bands: {bands},
                        units: "DN"
                    }}],
                    output: {{
                        bands: {len(bands)},
                        sampleType: "UINT16"
                    }}
                }};
            }}
            
            function evaluatePixel(sample) {{
                return [{', '.join(['sample.' + band for band in bands])}];
            }}
        """
    }
    
    response = oauth.post(process_api_url, json=payload, headers=headers)
    
    return response

# Function to save the fetched image data to a file
def save_image_data(response, file_path):
    """
    Saves the fetched image data to a file.

    Parameters:
    - response: The response from the Process API.
    - file_path: The path where the image will be saved.
    
    Returns:
    None
    """
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Image saved to {file_path}")
    else:
        print("Failed to fetch image data:", response.content)

# Function to process the saved image data
def process_image_data(file_path):
    """
    Processes the saved image data.

    Parameters:
    - file_path: The path of the saved image file.
    
    Returns:
    None
    """
    # Open and process the image using PIL
    with Image.open(file_path) as img:
        # Perform image processing here
        # For example, convert to grayscale
        grayscale_img = img.convert('L')

        # Save or display the processed image as needed
        grayscale_img.save('processed_image.tif')
        grayscale_img.show()

# Example usage
session = create_sentinel_session(client_id, client_secret)
response = fetch_sentinel_data(session, [13.822174, 45.850803, 13.828681, 45.853935], ('2024-03-10', '2024-03-10'))

# Specify the path where you want to save the image
image_file_path = 'path/to/your/image.tif'

# Save the fetched image data
save_image_data(response, image_file_path)

# Process the saved image data
process_image_data(image_file_path)