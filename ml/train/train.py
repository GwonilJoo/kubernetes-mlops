
def train(model, data_loader, criterion, optimizer, epochs, device):
    total_batch = len(data_loader)

    print('Learning started. It takes sometime.')
    for epoch in range(epochs):
        avg_cost = 0

        for X, Y in data_loader:
            # image is already size of (28x28), no reshape
            # label is not one-hot encoded
            X = X.to(device)
            Y = Y.to(device)

            optimizer.zero_grad()
            hypothesis = model(X)
            cost = criterion(hypothesis, Y)
            cost.backward()
            optimizer.step()

            avg_cost += cost / total_batch

        print('[Epoch: {:>4}] cost = {:>.9}'.format(epoch + 1, avg_cost))

    print('Learning Finished!')