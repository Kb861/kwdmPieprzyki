from keras.preprocessing.image import ImageDataGenerator
from cnn_model import CNN
from moleimages import MoleImages
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import sys

def plot_roc(y_test, y_score, title='ROC Curve'):
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.savefig(title + '.png')
    plt.show()



if __name__ == '__main__':
    train_data_dir = 'datasets/train/'
    validation_data_dir = 'datasets/val/'
    nb_train_samples = 1400
    nb_validation_samples = 1400
    epochs = 100
    batch_size = 100

    # mimg = MoleImages()
    # X_test, y_test = mimg.load_test_images(train_data_dir,
    #                                        validation_data_dir)

    mycnn = CNN()
    train_datagen = ImageDataGenerator(
    vertical_flip=True,
    horizontal_flip=True)
    test_datagen = ImageDataGenerator()

    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(128, 128),
        batch_size=batch_size,
        class_mode='binary')

    validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(128, 128),
        batch_size=batch_size,
        class_mode='binary')

    model = mycnn.fit_generator(train_generator,validation_generator,
        nb_train_samples, nb_validation_samples, epochs, batch_size)

    model.save(sys.argv[1])
