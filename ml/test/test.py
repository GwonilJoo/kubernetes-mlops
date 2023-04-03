import torch

def test(model, path, data_loader, device):
    model.load_state_dict(torch.load(path))
    model.eval()

    # with torch.no_grad():
    #     X_test = mnist_test.test_data.view(len(mnist_test), 1, 28, 28).float().to(device)
    #     Y_test = mnist_test.test_labels.to(device)

    #     prediction = model(X_test)
    #     correct_prediction = torch.argmax(prediction, 1) == Y_test
    #     accuracy = correct_prediction.float().mean()
    #     print('Accuracy:', accuracy.item(), flush=True)

    #     return accuracy.item()

    with torch.no_grad():
        count_of_correct, count_of_data = 0, 0
        
        for X, Y in data_loader:
            X = X.to(device)
            Y = Y.to(device)

            prediction = model(X)
            correct_prediction = torch.argmax(prediction, 1) == Y
            count_of_correct += correct_prediction.float().sum().item()
            count_of_data += len(correct_prediction)

        accuracy = count_of_correct / count_of_data
        print('Accuracy:', accuracy, flush=True)

        return accuracy