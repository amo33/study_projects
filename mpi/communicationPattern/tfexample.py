'''
distributed training을 위한 MPI 통신 방법을 tensorflow에서 소개해보겠다.
여기선 tf.distribute.experimental.MultiWorkerMirroredStrategy 를 쓰겠다.
간단한 예시로 mnist를 살펴보자.
'''
# TODO 실제로 다중 노드로 학습 진행시켜보기
# https://csm-kr.tistory.com/89
# https://github.com/18520339/ml-distributed-training
import tensorflow as tf
import json, os
from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    
    def create_model(): # Define a simple sequential model
        return tf.keras.models.Sequential([
            tf.keras.layers.Dense(16, activation='relu', input_shape=(784,)),
            tf.keras.layers.Dense(10)
        ])

    # 'TF_CONFIG' environment variable for each worker 
    tf_config = {
        'cluster': {
            'worker': ["localhost:12345", "localhost:23456"] # 여기서 worker들은 실제 worker의 주소여야 한다.

        },
        'task': {'type': 'worker', 'index': rank}
    }
    os.environ['TF_CONFIG'] = json.dumps(tf_config)

    # Choose the right strategy for multi-worker training
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()

    # Load the dataset
    (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
    x_train = x_train / 255.0

    # Batch the dataset
    BUFFER_SIZE = len(x_train)
    BATCH_SIZE_PER_REPLICA = 64
    GLOBAL_BATCH_SIZE = BATCH_SIZE_PER_REPLICA * size
    train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(BUFFER_SIZE).batch(GLOBAL_BATCH_SIZE)

    # Open a strategy scope and define and compile the model inside it
    with strategy.scope():
        model = create_model()
        model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      optimizer=tf.keras.optimizers.Adam(),
                      metrics=['accuracy'])

    # Train the model
    model.fit(train_dataset, epochs=3)

if __name__ == "__main__":
    main()