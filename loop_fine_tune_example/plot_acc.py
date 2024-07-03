import matplotlib.pyplot as plt

# parse log.txt to plot train/validation accuracy vs epochs #

path = 'output/log.txt'

epochs = []
train_acc = []
valid_acc = []

with open(path, 'r') as file:
    for line in file:
        parts = line.strip().split(', ')
        epoch = int(parts[0].split(': ')[1])
        train_accuracy = float(parts[5].split(': ')[1])
        valid_accuracy = float(parts[6].split(': ')[1])
        
        epochs.append(epoch)
        train_acc.append(train_accuracy)
        valid_acc.append(valid_accuracy)

plt.figure(figsize=(10, 5))
plt.plot(epochs, train_acc, label='Train Accuracy', marker='o')
plt.plot(epochs, valid_acc, label='Validation Accuracy', marker='o')

plt.title('Epoch vs. Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.show()