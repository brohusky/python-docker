# Python Docker

An ubuntu base docker image:
- Python 3.7.2
- FFMPEG 4.1

## Why this base image?
This base image is going to help running opencv on production.

## Important
** In opencv, VideoCapture, always pass non secure (http) url to VideoCapture**
For some reasons opencv is not able to handle https urls and it doesn't read the file
You can check your opencv build info by running the following command:
```
python3 -c "import cv2; print(cv2.getBuildInformation())"
```

## Something is missing
We are always looking for more contributors so just [create an issue](https://github.com/brohusky/python-docker/issues/new).

## Push to Docker
```
docker login
cd <version> # cd v3.7.2
# Build the image
docker build . -t brohusky/python:3.7.2
# Push the image
docker push brohusky/python:3.7.2
```
