# File-Uploader

Dockerized Flask application that allows the user to upload a file

## Usage

Build the image (in the root of the project)

```bash
docker build . -t <image_name>
```

Run the image -- publish the hardcoded port 5006, and mount the volume to a folder that you want to save your files to inside the container

```bash
docker run -d -p 5006:5000 -v upload-dir:/app/data <image_name>
```

Done! Test out the app. You can then stop and remove the container, and any new containers will still contain the files that were uploaded with previous app iterations (as long as the volume is mounted to the same named volume "upload-dir" -- see Dockerfile)
