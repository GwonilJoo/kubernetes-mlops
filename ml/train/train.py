import math
import torch
import os
from config import config


def train(model, data_loader, criterion, optimizer, config: config, experiment_id):
    total_batch = len(data_loader)

    save_dir = os.path.join(config.save_dir, str(experiment_id))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        os.chmod(save_dir, 0o777)

    last_path = os.path.join(save_dir, "last.pt")
    best_loss_path = os.path.join(save_dir, "best_loss.pt")
    best_acc_path = os.path.join(save_dir, "best_acc.pt")

    last_loss, last_acc, best_loss, best_acc = math.inf, 0, math.inf, 0
    print('Learning started. It takes sometime.', flush=True)
    for epoch in range(config.epochs):
        avg_loss = 0
        count_of_data = 0
        count_of_correct = 0

        for X, Y in data_loader:
            # image is already size of (28x28), no reshape
            # label is not one-hot encoded
            X = X.to(config.device)
            Y = Y.to(config.device)

            optimizer.zero_grad()
            hypothesis = model(X)
            loss = criterion(hypothesis, Y)
            loss.backward()
            optimizer.step()

            correct_prediction = torch.argmax(hypothesis, 1) == Y
            correct = correct_prediction.float().sum()
            count_of_data += len(correct_prediction)

            avg_loss += loss / total_batch
            count_of_correct += correct
        
        last_loss = avg_loss
        last_acc = count_of_correct / count_of_data
        
        torch.save(model.state_dict(), last_path)

        if last_loss < best_loss:
            best_loss = last_loss
            torch.save(model.state_dict(), best_loss_path)
        
        if last_acc > best_acc:
            best_acc = last_acc
            torch.save(model.state_dict(), best_acc_path)

        print('[Epoch: {:>4}] loss = {:>.9} acc = {:>.9}'.format(epoch + 1, last_loss, last_acc), flush=True)

    print('Learning Finished!', flush=True)
    print('best loss = {:>.9} best acc = {:>.9}'.format(best_loss, best_acc), flush=True)

    return {
        "last_loss": {
            "value": last_loss.item(),
            "path": last_path,
        },
        "last_acc": {
            "value": last_acc.item(),
            "path": last_path,
        },
        "best_loss": {
            "value": best_loss.item(),
            "path": best_loss_path,
        },
        "best_acc": {
            "value": best_acc.item(),
            "path": best_acc_path,
        },
    }