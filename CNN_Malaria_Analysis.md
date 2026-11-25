# Custom CNN Evaluation -- Malaria RBC Classification

## 1. Project objective

The custom Convolutional Neural Network (CNN) was trained to classify
microscopic red blood cell (RBC) images into two categories:

-   **Uninfected (class 0):** RBC images labelled as uninfected.
-   **Parasitized (class 1):** RBC images labelled as parasitized.

This document records the test-set evaluation results and explains how
to interpret them.

> **Important:** This is an academic image-classification experiment,
> not a clinically validated diagnostic system. These results must not
> be used to diagnose malaria or guide treatment.

## 2. Test-set classification report

The model was evaluated on **4,134 test images**, with 2,067 images in
each class.

  Class                    Precision     Recall   F1-score     Support
  ---------------------- ----------- ---------- ---------- -----------
  Uninfected                    0.95       0.94       0.94       2,067
  Parasitized                   0.94       0.95       0.94       2,067
  **Macro average**         **0.94**   **0.94**   **0.94**   **4,134**
  **Weighted average**      **0.94**   **0.94**   **0.94**   **4,134**

**Overall test accuracy: 0.94 (94%)**

### What the metrics mean

-   **Precision:** Of the images predicted as a particular class, the
    proportion that truly belongs to that class.
-   **Recall:** Of all images that truly belong to a class, the
    proportion correctly identified by the model.
-   **F1-score:** The harmonic mean of precision and recall. It balances
    the two metrics.
-   **Support:** The number of actual test examples belonging to that
    class.
-   **Macro average:** The unweighted average across the classes.
-   **Weighted average:** The average across classes weighted by their
    support.

### Interpretation

-   For the **Parasitized** class, recall is 0.95. The model correctly
    identified approximately 95% of the parasitized test images.
-   For the **Uninfected** class, recall is 0.94. The model correctly
    identified approximately 94% of the uninfected test images.
-   Both classes have an F1-score of approximately 0.94, indicating
    similar overall precision-recall performance.

The displayed report is rounded to two decimal places. More precise
values can be calculated from the original predictions if needed.

## 3. Confusion matrix

The confusion matrix uses actual classes as rows and predicted classes
as columns.

  Actual class        Predicted Uninfected   Predicted Parasitized
  ----------------- ---------------------- -----------------------
  **Uninfected**                 **1,944**                 **123**
  **Parasitized**                  **111**               **1,956**

### How to read it

-   **1,944 true negatives:** Uninfected images correctly classified as
    Uninfected.
-   **123 false positives:** Uninfected images incorrectly classified as
    Parasitized.
-   **111 false negatives:** Parasitized images incorrectly classified
    as Uninfected.
-   **1,956 true positives:** Parasitized images correctly classified as
    Parasitized.

For this project, the 111 false negatives deserve particular attention:
these are infected-cell images that the model classified as uninfected.
In a medical screening context, missed positive cases are an important
error type to investigate.

The confusion matrix contains 3,900 correct predictions (1,944 + 1,956)
out of 4,134 test images, which is approximately 94.34% accuracy. The
classification report displays accuracy rounded to 0.94.

## 4. ROC curve and AUC

The test-set ROC curve was plotted using the model's predicted
probabilities.

**Reported ROC-AUC: 0.9826**

### What ROC and AUC mean

-   The **ROC curve** plots the true positive rate (sensitivity/recall)
    against the false positive rate at different classification
    thresholds.
-   **AUC** is the area under the ROC curve.
-   An AUC of 0.5 represents chance-level ranking, while an AUC of 1.0
    represents perfect separation on the evaluated data.

An AUC of **0.9826** indicates that the model has strong ability to rank
parasitized images above uninfected images on this test set. AUC
measures ranking performance across thresholds; it does not mean that
the model is 98.26% accurate.

## 5. Overall interpretation

The custom CNN achieved the following reported test results:

  Evaluation measure                      Result
  ----------------------- ----------------------
  Accuracy ->                 94% (rounded report) <br>
  Uninfected precision ->                      0.95 <br>
  Uninfected recall ->                         0.94 <br>
  Parasitized precision ->                    0.94 <br>
  Parasitized recall ->                     0.95 <br>
  Macro F1-score ->                           0.94 <br>
  ROC-AUC ->                       0.9826 <br>

The results are promising for this dataset split. The model correctly
classified most images in both categories, and the ROC-AUC indicates
strong class-separation performance.

However, performance on this test set alone does not establish that the
model will generalize to images from different laboratories,
microscopes, staining procedures, or patient populations.

## 6. Important limitations and checks

1.  **Image-level versus patient-level split:** If multiple images from
    the same patient are present, a random image-level split can place
    images from one patient in both training and test sets. This can
    make performance appear better than it would be on entirely unseen
    patients. If patient identifiers or grouping information are
    available, use a patient-level split.
2.  **Independent test set:** The test set should remain untouched
    during model training and model selection. Use the validation set
    for tuning.
3.  **Class threshold:** The confusion matrix above uses the stated
    probability threshold of 0.5. Different thresholds change
    false-positive and false-negative counts. Threshold selection should
    be based on a justified validation procedure, not by repeatedly
    optimizing on the test set.
4.  **Clinical validation:** These image-level metrics do not establish
    clinical safety or diagnostic readiness. External validation and
    expert review would be required before any real-world medical use.

## 7. Conclusion

The custom CNN achieved approximately **94% test accuracy** and a
**ROC-AUC of 0.9826** on the evaluated dataset split. Its class-wise
F1-scores were both approximately 0.94. The confusion matrix shows 111
false negatives and 123 false positives.

These results provide a baseline for comparison with the next model,
such as ResNet50 using transfer learning. For a fair comparison, both
models should use the same training, validation, and test partitions and
the same evaluation procedure.

------------------------------------------------------------------------

*Prepared as a project-results summary from the CNN evaluation outputs
recorded during the experiment.*
