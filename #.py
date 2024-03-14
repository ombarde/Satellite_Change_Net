# prompt: Gather multi-temporal land satellite imagery datasets. These should include pairs of images taken at different time points.

# Import the necessary libraries.
import ee
import logging

# Initialize Earth Engine.
ee.Initialize()

# Set the start and end dates for the image collection.
start_date = '2015-01-01'
end_date = '2015-12-31'

# Define the image collection parameters.
image_collection_params = {
  'start_date': start_date,
  'end_date': end_date,
  'bands': ['B3', 'B2', 'B1'],
  'scale': 500
}

# Define the filter parameters for each image pair.
filter_params = [
  {'before': '2015-06-01', 'after': '2015-05-01'},
  {'before': '2015-09-01', 'after': '2015-08-01'},
  {'before': '2015-12-01', 'after': '2015-11-01'}
]

# Gather the image pairs.
def gather_image_pairs(image_collection_params, filter_params):
  image_collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA')
  image_pairs = []

  for filter_param in filter_params:
    before_date = filter_param['before']
    after_date = filter_param['after']

    # Filter the image collection for images acquired before and after the specified dates.
    image_before = ee.Image(image_collection.filterDate(start_date, before_date).sort('system:time_start').first())
    image_after = ee.Image(image_collection.filterDate(after_date, end_date).sort('system:time_start').first())

    # Add the image pair to the list.
    image_pairs.append([image_before, image_after])

  return image_pairs

image_pairs = gather_image_pairs(image_collection_params, filter_params)

# Print the image pairs.
for image_pair in image_pairs:
  print(image_pair[0].getInfo(), image_pair[1].getInfo())
