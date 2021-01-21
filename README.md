# z-qml

**Our Quantum Machine Learning docker image.**

For more details, see [orquestra.io/docs/qe/machine-learning/ml](https://www.orquestra.io/docs/qe/machine-learning/ml).

## Info

* This image has [z-ml](https://github.com/zapatacomputing/z-ml) (and [qe-tools-base](https://github.com/zapatacomputing/qe-tools/blob/master/docker/qe-tools-base.Dockerfile)) as the base image.
* Purpose is for installing QML libraries.
* Rigetti `qvm` and `quilc` (and [dependencies](http://docs.rigetti.com/en/stable/start.html)) are installed. More info [here](https://github.com/rigetti/qvm).

## Testing locally

Build the image:

```bash
docker build -t z-qml .
```
If it finished without errors, your image is ready for production.

Check whether your image is there:

```bash
docker images
```

If you would like to inspect your docker container (i.e. go inside your container, inspect dir structure, run things, etc), you can run:

```bash
docker run -it z-qml sh
```
