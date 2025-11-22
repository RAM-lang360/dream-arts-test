docker build -t your-image-name .
docker run -it --rm -v "$PWD/src:/app/src" your-image-name