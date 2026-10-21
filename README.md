# greenpod
#Orange-ripenes
Image Classification Using CNN

Project Overview

This project implements an image classification system using a Convolutional Neural Network (CNN) and Python. The model processes images, learns visual features, and predicts the corresponding image class.

The dataset currently contains four classes:

- Blackspot
- Canker
- Fresh
- Grenning

Note: Confirm these class names against the original assignment requirements before submission.

Objectives

- Organize images into training and testing datasets.
- Preprocess images by resizing and normalizing pixel values.
- Build and train a CNN model.
- Evaluate model performance on unseen test images.
- Predict the class of a new image.
- Visualize model performance using accuracy graphs and a confusion matrix.

Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- Matplotlib
- Seaborn
- Scikit-learn
- PyCharm

Dataset Structure

project/
├── dataset/
│ ├── train/
│ │ ├── Blackspot/
│ │ ├── Canker/
│ │ ├── Fresh/
│ │ └── Grenning/
│ └── test/
│ ├── Blackspot/
│ ├── Canker/
│ ├── Fresh/
│ └── Grenning/
├── check_dataset.py
├── extract_features.py
├── image_features.py
├── inspect_dataset.py
├── main.py
├── view_image.py
└── README.md

Dataset Information

Based on the initial dataset inspection:

Split| Number of Images
Training| 991
Testing| 99
Total| 1,090

These are the initial reported counts; the final usable image count may differ after image validation.

Installation

Install Python and open a terminal in the project directory.

Install the required packages:

python -m pip install tensorflow numpy pillow matplotlib seaborn scikit-learn

How to Run the Project

Step 1: Prepare the dataset

python prepare_dataset.py

This script resizes images to 128 × 128 pixels, normalizes pixel values, and saves the processed arrays.

Step 2: Train the model

python train_model.py

The CNN learns features from the training images and evaluates its performance on the test dataset.

Step 3: Predict an image

python predict_image.py

The script predicts the class of a selected image and displays the prediction confidence.

Step 4: Evaluate the model

python evaluate_model.py

This generates accuracy, precision, recall, F1-score, and confusion matrix results.

Step 5: Visualize results

python plot_confusion_matrix.py

The confusion matrix is saved as an image for analysis.

Model Architecture

The CNN includes:

1. Image input layer (128 × 128 × 3).
2. Convolutional layers for feature extraction.
3. Max-pooling layers for dimensionality reduction.
4. A classification layer using Softmax activation.
5. Adam optimizer and categorical probability prediction.

The improved model also uses data augmentation, dropout, and early stopping.

Evaluation Metrics

- Accuracy: Percentage of correctly classified test images.
- Precision: Correctness of predictions for each class.
- Recall: Ability to identify images belonging to each class.
- F1-score: Balance between precision and recall.
- Confusion Matrix: Comparison of actual and predicted classes.

Results

The final model accuracy and evaluation metrics should be added after running the complete training and testing pipeline.

- Test accuracy: To be measured
- Precision: To be measured
- Recall: To be measured
- F1-score: To be measured

Future Improvements

- Increase the size and diversity of the dataset.
- Compare CNN results with transfer-learning models such as MobileNetV2.
- Tune hyperparameters to improve generalization.
- Add a simple web interface for image uploads and predictions.
- Test performance on images captured under different lighting conditions.

Conclusion

This project demonstrates an image classification workflow using Python and deep learning, including data preparation, CNN training, image prediction, and model evaluation.

The final conclusions should be based on measured test results and the requirements of the original assignment.

Author

Manimaaran R

GitHub: Add your GitHub profile URL here.

