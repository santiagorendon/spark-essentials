# The official repository for the Rock the JVM Spark Essentials with Scala course

This repository contains the code we wrote during  [Rock the JVM's Spark Essentials with Scala](https://rockthejvm.com/course/spark-essentials) (Udemy version [here](https://udemy.com/spark-essentials)) Unless explicitly mentioned, the code in this repository is exactly what was caught on camera.

## How to install

- install [Docker](https://docker.com)
- either clone the repo or download as zip
- open with IntelliJ as an SBT project
- Windows users, you need to set up some Hadoop-related configs - use [this guide](/HadoopWindowsUserSetup.md)
- in a terminal window, navigate to the folder where you downloaded this repo and run `docker compose up` to build and start the PostgreSQL container - we will interact with it from Spark
- in another terminal window, navigate to `spark-cluster/` 
- Linux/Mac users: build the Docker-based Spark cluster with
```
chmod +x build-images.sh
./build-images.sh
```
- Windows users: build the Docker-based Spark cluster with
```
build-images.bat
```
- when prompted to start the Spark cluster, go to the `spark-cluster` directory and run `docker compose up --scale spark-worker=3` to spin up the Spark containers with 3 worker nodes

### Run the Python lessons in Docker

If you want to avoid installing Java locally, you can run the PySpark examples inside a container instead.

Run the default lesson script:
```
docker compose -f docker-compose.pyspark.yml run --rm pyspark-runner
```

Run a different Python file from this repo:
```
docker compose -f docker-compose.pyspark.yml run --rm pyspark-runner python src/main/python/your_script.py
```

### Run the joins notebook in Docker

Start Jupyter Lab:
```
docker compose -f docker-compose.pyspark.yml up --build pyspark-notebook
```

Or use the shortcut script:
```
start-pyspark-notebook.bat
```
on Windows, or:
```
./start-pyspark-notebook.sh
```
on Linux/Mac.

Keep that terminal running while you use the notebook. The notebook server stops when you stop the container.

Then open this URL in your browser or connect VS Code to it:
```
http://localhost:8888/lab?token=spark-essentials
```

The notebook version of the joins lesson lives at:
```
src/main/python/joins.ipynb
```

To stop the notebook server:
```
docker compose -f docker-compose.pyspark.yml down
```

This container includes Python 3.11, OpenJDK 17, PySpark 3.5.0, and Jupyter Lab, and mounts the repo into `/workspace` so your code and data stay on the host machine.

### Open the notebook from VS Code

1. Start the notebook server with one of the commands above.
2. Open `src/main/python/joins.ipynb` in VS Code.
3. If VS Code asks how to connect, choose `Existing Jupyter Server`.
4. When VS Code asks for the server URL, paste:
```
http://localhost:8888/lab?token=spark-essentials
```
5. Run cells normally.

If VS Code says it cannot connect, check the terminal running Docker first. A healthy server keeps running and does not exit back to the prompt.

### VS Code workspace integration

This repo includes workspace-only VS Code launch and task entries for running Python files in Docker.

In the Run and Debug panel, select:
```
Python: Current File in Docker
```

Or from the Command Palette, run:
```
Tasks: Run Task -> Run Current Python File in Docker
```

These settings live under `.vscode/` in this repository, so they only affect this workspace and do not change your global VS Code Python configuration.

### Spark Cluster Troubleshooting

#### Windows users - '\r' command not found

When triggering the Docker Compose command, some Windows users have reported errors that look like this:

```
spark-worker-1  | /start-worker.sh: line 2: $'\r': command not found
: No such file or directoryrker.sh: line 3: /spark/sbin/spark-config.sh
: No such file or directoryrker.sh: line 4: /spark/bin/load-spark-env.sh
spark-worker-1  | /start-worker.sh: line 5: $'\r': command not found
spark-worker-1  | /start-worker.sh: line 7: $'\r': command not found
spark-worker-1  | /start-worker.sh: line 9: $'\r': command not found
spark-worker-1  | ln: failed to create symbolic link '/spark/logs/spark-worker.out'$'\r': No such file or directory
spark-worker-1  | /start-worker.sh: line 11: $'\r': command not found
spark-worker-1  | /start-worker.sh: line 12: /spark/logs/spark-worker.out: No such file or directory
spark-worker-1 exited with code 1
```

The problem is with line endings (`\r`) that have not been converted automatically by GitHub in some situations. Clean the images you've created and explicitly run the `dos2unix` command on all `.sh` files, then recreate the images and the cluster again.

## How to use the code

Clone this repository and checkout the `start` tag by running the following in the repo folder:

```
git checkout start
```

### How to see the final code

Udemy students: checkout the `udemy` branch of the repo:
```
git checkout udemy
```

Rock the JVM students: checkout the master branch:
```
git checkout master
```

### For questions or suggestions

If you have changes to suggest to this repo, either
- submit a GitHub issue
- tell me in the course Q/A forum
- submit a pull request!
