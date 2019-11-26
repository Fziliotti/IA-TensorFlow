import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Importando a base de dados das imagens dos dígitos escritos à mão (60000 de treino e 10000 de teste)
mnist = tf.keras.datasets.mnist

# Separando os dados
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print("x" , x_train[12]) -> printa a matriz 18x18
# print("y" , y_train[12]) -> printa qual o numero digitado na matriz

# Fazendo a Normalização dos dados, para que fiquem entre 0 e 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Criando o modelo da rede neural
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# Gerando/compilando a rede neural
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Aqui ocorre o treinamento da rede, nesse caso com 5 epochs/rodadas
model.fit(x_train, y_train, epochs=5)

# Avaliação da performance, utilizando as variaveis de teste (10000 imagens testadas)
print(model.evaluate(x_test, y_test))

# numero da imagem que se deseja prever (até indice 9999)
indexImage = 100

# imprime a predicao feita
print("Predicao:", np.argmax(model.predict(np.array([x_test[indexImage]]))))

# desenha imagem com matplotlib
plt.imshow(x_test[indexImage])
