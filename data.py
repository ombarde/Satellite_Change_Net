import datetime
from sentinelhub import WebFeatureService, BBox, CRS, DataCollection, SHConfig, SentinelHubRequest, MimeType

# Set up Sentinel Hub configuration
config = SHConfig()

# Add your Sentinel Hub API credentials to config
config.sh_client_id = 'fd06797c-d171-4acf-8c28-03f92a7280bb'
config.sh_client_secret = 'lbfkwdDxd7LhXvyPpCX4UABsOrLJ59nb'

# Define your bounding box coordinates
xmin, ymin, xmax, ymax = 10.0, 20.0, 30.0, 40.0

# Create a BBox object
bbox = BBox(bbox=[xmin, ymin, xmax, ymax], crs=CRS.WGS84)
time_interval = ('2024-02-07T00:00:00', '2024-02-08T23:59:59')  # Include time component

# Specify other request parameters
layer = 'TRUE-COLOR-S2-L1C'  # e.g., 'TRUE-COLOR-S2-L1C'
resolution = 10  # Spatial resolution in meters (adjusted to a common value)


# Default evalscript for RGB bands
evalscript = """
    // Default evalscript for RGB bands
    // It returns the True Color (RGB) image

    function setup() {
        return {
            input: ["B02", "B03", "B04"],
            output: { bands: 3 }
        };
    }

    function evaluatePixel(sample) {
        return [sample.B04, sample.B03, sample.B02];
    }
"""

# Specify the absolute path to the data folder
data_folder = '/absolute/path/to/save/data'

# Specify other request parameters
layer = 'TRUE-COLOR-S2-L1C'  # e.g., 'TRUE-COLOR-S2-L1C'
resolution = 10  # Spatial resolution in meters (adjusted to a common value)

# Create a Sentinel Hub request
request = SentinelHubRequest(
    data_folder=data_folder,
    evalscript=evalscript,
    input_data=[
        SentinelHubRequest.input_data(data_collection=DataCollection.SENTINEL2_L1C, time_interval=time_interval),
    ],
    responses=[
        SentinelHubRequest.output_response('default', MimeType.TIFF),
    ],
    bbox=bbox,
    size=(resolution, resolution),  # Adjust resolution to a common value
    config=config
)

# Make the request and download data
data = request.get_data(save_data=True)
