from google_images_download import google_images_download

animals = ['koala', 'monkey', 'pandas', 'bear', 'turtle', 'chicken']

response = google_images_download.googleimagesdownload()

for animal in animals:
    absolute_image_paths = response.download({'keywords':animal, 'limit':1})
    print(absolute_image_paths)

