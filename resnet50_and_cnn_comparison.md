# Malaria Cell Image Classification
## ResNet50 Results and CNN Comparison

### 1. ResNet50 Evaluation

ResNet50 was evaluated on **4,134 test images**: 2,067 Uninfected and 2,067 Parasitized.

| Metric | Score |
|---|---:|
| Accuracy | 93% |
| ROC-AUC | 0.9845 |
| Macro precision | 0.94 |
| Macro recall | 0.93 |
| Macro F1-score | 0.93 |

### 2. ResNet50 Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Uninfected | 0.91 | 0.97 | 0.94 | 2,067 |
| Parasitized | 0.96 | 0.90 | 0.93 | 2,067 |
| **Overall accuracy** |  |  | **0.93** | **4,134** |

### 3. ResNet50 Confusion Matrix

| Actual / Predicted | Uninfected | Parasitized |
|---|---:|---:|
| Uninfected | 1,995 | 72 |
| Parasitized | 203 | 1,864 |

- 1,995 Uninfected images were correctly classified.
- 1,864 Parasitized images were correctly classified.
- 72 Uninfected images were incorrectly classified as Parasitized.
- 203 Parasitized images were incorrectly classified as Uninfected.

### 4. CNN vs ResNet50 Comparison

The following comparison uses the reported test results from both models.

| Evaluation metric | Custom CNN | ResNet50 |
|---|---:|---:|
| Accuracy | 94% | 93% |
| ROC-AUC | 0.9826 | 0.9845 |
| Test images | 4,134 | 4,134 |

**Key observations**

- The custom CNN achieved the higher reported accuracy.
- ResNet50 achieved the slightly higher ROC-AUC, indicating marginally stronger overall class-separation performance across thresholds.
- ResNet50 had higher precision for the Parasitized class (0.96), but lower recall (0.90). It missed 203 Parasitized test images.
- The custom CNN's reported Parasitized recall was 0.95, compared with 0.90 for ResNet50.

### 5. Conclusion

Both models performed well on this malaria cell-image classification task. The custom CNN achieved higher accuracy and better recall for detecting Parasitized images in the reported results. ResNet50 achieved a slightly higher ROC-AUC and higher precision for the Parasitized class.

Based on these results, the custom CNN performed better at the default classification threshold in terms of accuracy and Parasitized-class recall, while ResNet50 had a marginal advantage in ROC-AUC.

### Important Note

For a fair comparison, confirm that both models were evaluated on the **same test images**, with the same preprocessing and class-label mapping. The test-set sizes are equal, but equal sizes alone do not prove that the images were identical.

These results describe performance on the provided dataset; they do not establish clinical diagnostic reliability.
