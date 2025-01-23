# 🚗 Deep Learning-Based Driving Behavior Analysis

## 📌 Project Overview
This project aims to classify **driving behavior into slow, aggressive, and fast categories** using deep learning techniques. The study leverages **Long Short-Term Memory (LSTM), ConvLSTM, and CNN-LSTM models** to analyze sensor data (accelerometer and gyroscope) collected from a smartphone application. The objective is to enhance road safety, optimize transportation, and predict driver behavior patterns effectively.

## 🔍 Key Features
- **Deep Learning Models**: Implemented LSTM, ConvLSTM, and CNN-LSTM for sequence classification.
- **Sensor Data Processing**: Utilized accelerometer and gyroscope data from an Android device.
- **Data Preprocessing**: Standardized features, removed noise, and applied feature engineering.
- **Performance Evaluation**: Compared model accuracy, precision, and recall for optimal selection.
- **Applications**: Can be integrated into driver assistance systems, insurance risk assessment, and smart transportation analytics.

## 📂 Folder Structure
Deep Learning-Based Driving Behavior Analysis/
│── README.md            # Project documentation
│── data/                # Raw and preprocessed datasets
│── notebooks/           # Jupyter Notebooks for model training & analysis
│── final_report.pdf     # Research paper summarizing methodology & results
│── presentation.pptx    # Slide deck presenting key insights


## 🛠 Tech Stack
- **Languages**: Python
- **Libraries**: TensorFlow, Keras, Scikit-learn, Pandas, Matplotlib, Seaborn
- **Data Collection**: Smartphone accelerometer & gyroscope sensors
- **Modeling Approaches**: LSTM, ConvLSTM, CNN-LSTM for time-series classification

## 📊 Dataset Details
- **Device**: Samsung Galaxy S21 (Accelerometer & Gyroscope Data)
- **Sampling Rate**: 2 samples per second
- **Classes**: Slow, Normal, Aggressive Driving
- **Training Set**: 3644 instances (Balanced across classes)
- **Test Set**: 3084 instances

## 🏆 Model Performance
| Model       | Accuracy | Precision | Recall  |
|------------|----------|----------|--------|
| **LSTM**    | 62.42%   | 68.29%   | 18.79% |
| **ConvLSTM** | 60.40%   | 59.56%   | 54.36% |
| **CNN-LSTM** | 57.05%   | 59.60%   | 39.60% |

- **LSTM Model performed best in terms of accuracy and precision.**
- **ConvLSTM had the highest recall, making it better for detecting aggressive behaviors.**

## 📈 Key Findings
- **Driving behavior can be effectively classified using deep learning.**
- **LSTM models achieve the best accuracy and precision.**
- **Sensor-based data provides valuable insights into road safety & driving styles.**

## 🛑 Limitations
- **Sensor noise and road conditions affect data quality.**
- **Driver conditions (fatigue, distraction) are not explicitly modeled.**
- **More diverse datasets and real-world testing are needed for better generalization.**

## 🔮 Future Enhancements
- **Real-Time Analysis**: Implementing a real-time driving behavior monitoring system.
- **Multi-Sensor Fusion**: Combining accelerometer, GPS, and camera data for higher accuracy.
- **Personalized Driving Feedback**: Integration with rideshare apps like Uber/Lyft to let customers choose a driving style (Normal, Slow, Fast).

## 📜 References
- **Dataset**: [Kaggle Driving Behavior Dataset](https://www.kaggle.com/datasets/outofskills/driving-behavior)
- **Research Papers**:
  - *Driving Style Recognition with Deep Learning* [[IEEE](https://ieeexplore.ieee.org/document/8547731)]
  - *Deep Learning for Driver Behavior Analysis: A Review* [[MDPI](https://www.mdpi.com/1424-8220/19/24/5536/htm)]
  - *A Comparative Study of Deep Learning Techniques for Driver Behavior Analysis* [[IEEE](https://ieeexplore.ieee.org/document/8693267)]

## 📬 Contact
For questions or collaboration, reach out to:
- **Author**: Hrishikesh Balakrishnan
- **GitHub**: [Hunt4code](https://github.com/Hunt4code)
- **Email**: hrishiumb@gmail.com
