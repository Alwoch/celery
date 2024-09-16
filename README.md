### CELERY AND RABBIT-MQ

1. start the rabbit mq container if its not already running
    ```
    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

    ```
2. Access the RabbitMQ container:
    ```
    docker exec -it rabbitmq /bin/bash

    ```
3. Run the RabbitMQ commands inside the container
    - create a RabbitMQ user and password
        ```
        rabbitmqctl add_user myuser mypassword

        ```
    - create a virtual host (Hosts are isolated environments where exchanges, queues and bindings are managed separately.It allows logical separation between different applications or services using the same RabbitMQ instance.)
        ```
        rabbitmqctl add_vhost myvhost
        ```
    - Assign tags to the user: Tags are used to define the user's role or permission levels in RabbitMQ. the common tags include; administrator - gives the user administrative priviledges like adding users, modifying vhosts, etc, management: Provides access to the RabbitMQ management UI
        ```
        rabbitmqctl set_user_tags myuser mytag
        ```
    - Set permissions for the user on the virtualhost
        ```
        rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
        ```
4. Running the worker
    ```
    celery -A tasks worker --loglevel=INFO
    ```
