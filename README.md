# SatelliteChangeNet
Title of the research proposal
"SatelliteChangeNet: Liquid Neural Network for Detection & Prediction"
Area of Research
Satellite Image Processing, Pattern Recognition, Machine Learning, Deep Learning
Summary of the proposed research and expected deliverables
Change detection and prediction using satellite data have significant applications in various domains such as new build-up area detection, urban development analysis, disaster management, and agriculture.
Traditional methods often struggle to handle the complexity and diversity of satellite data. Liquid Neural Networks (LNNs) provide a novel approach to address these challenges by offering dynamic and adaptive computation. This proposal outlines a research project focused on utilizing LNNs for change detection and prediction tasks using satellite imagery.
LNNs are more dynamic, adaptive, efficient, and robust than traditional neural networks and have many potential use cases for satellite image data analysis.
This research project aims to leverage the applicability of Liquid Neural Networks (LNNs) based deep learning method for change detection and prediction tasks using multi-temporal satellite data. The outcomes of this project have the potential to enhance our capabilities in understanding and managing various environmental and societal changes. By combining the adaptability of LNNs with analysis of satellite imagery, it is proposed to create more accurate and efficient tools for change analysis.
Scope of the Work:
Develop a Liquid Neural Network (LNN) Architecture: Design and implement an LNN architecture suitable for analysing multi-temporal satellite imagery for change detection and prediction.
Dataset Collection and Preprocessing: Gather multi-temporal satellite datasets that encompass various types of changes, such as land cover changes, urban expansion, natural disasters, etc.
Pre-process the data to ensure consistency, alignment, and suitability for training LNNs.
Change Detection: Train the LNN model to identify changes between pairs of satellite images taken at different times. The model should be capable of highlighting regions with significant alterations.
Change Prediction: Extend the LNN's capabilities to predict potential changes in future satellite images based on historical data. This involves training the model to learn patterns and trends in changes over time.
Evaluation Metrics: Define appropriate evaluation metrics for both change detection and change prediction tasks. Common metrics like precision, recall, F1-score, and accuracy can be used.
Linkages to Space Programme:
LNN is an emerging technology for reducing the turnaround time to detect any changes in the spectral and temporal progression of biophysical and physical phenomena.
This work will enable us to address some of the existing gap areas of satellite data analysis using LNN architecture, its suitability, feature extraction, change detection and change prediction. It will be used for the detection of change in land, road, build-up area, de-forestation etc., and its change prediction.
Expected Deliverables:
A novel Liquid Neural Network architecture optimized for change detection and prediction tasks using multi-temporal satellite data.
Detailed Methodology & Algorithms/Techniques.
Trained models capable of accurately detecting changes in satellite imagery and predicting potential changes in future images.
Strengths in LNN approach for satellite data analysis and Inventory of dynamic change classes
 
References:

“Liquid” machine-learning system adapts to changing conditions
Authors: Daniel Ackerman, Ramin Hasani, Daniela Rus, Alexander Amini, Mathias Lechner, Radu Grosu
Publication Date: January 28, 2021
Findings:
MIT researchers developed LNNs that learn on the job, continuously adapting to new data inputs.
These flexible algorithms change their underlying equations, making them suitable for analyzing time series data.
The potential applications include medical diagnosis, autonomous driving, and more1.
“Land use/land cover change classification and prediction using deep convolutional spiking neural network (DCSNN) and enhanced Elman spike neural network (EESNN) (LU/LC-DCSNN-EESNN)”
Authors: Not specified
Publication Date: September 2023
Findings:
The paper proposes a method for land use/land cover change classification and prediction using deep convolutional spiking neural networks.
The approach aims to improve the quality of change maps in remote sensing images2.
“An Approach Automatic Change Detection Method for Satellite Images”
Authors: Not specified
Publication Date: Not specified
Findings:
The work presents a supervised Deep Learning (DL)-based change detection technique for generating accurate change maps.
Enhancing the quality of binary change detection maps is crucial in remote sensing applications3.
“A Review of Deep-Learning Methods for Change Detection in Multispectral Remote-Sensing Images”
Authors: Not specified
Publication Date: April 16, 2023
Findings:
The review focuses on deep learning models applied to change detection tasks in multispectral remote-sensing images.
It discusses supervised, semi-supervised, and unsupervised approaches for detecting changes over time4.
“Liquid Neural Networks: Definition, Applications, & Challenges”
Authors: Not specified
Publication Date: Not specified
Findings:
LNNs are purpose-built for time series data processing and forecasting.
They address challenges such as temporal dependencies, non-stationarity, and noise in time series data5.
These studies contribute to advancing our understanding of LNNs and their impact on satellite image analysis. Researchers worldwide continue to explore innovative approaches to enhance our ability to detect and predict changes in our dynamic world. 🌍🛰️
1: MIT News 2: Springer 3: Propulsion Technology Journal 4: MDPI 5: Unite.AI


Objectives: 

Integration with Space Programme:

Establish a seamless integration of the developed Liquid Neural Network with existing satellite data processing pipelines within space programs.

Evaluate the feasibility of deploying the model in satellite observation systems for real-time monitoring and decision support.

Validation and Generalization:

Conduct extensive cross-validation experiments to validate the robustness and reliability of the Liquid Neural Network across different geographical regions and environmental conditions.

Explore transfer learning techniques to enhance the model's generalization capabilities, allowing it to adapt to new datasets with minimal retraining.


Flow: 

Data Collection:
Gather multi-temporal satellite imagery covering different time points.
Ensure alignment and consistency in data acquisition.
Preprocessing:
Clean and preprocess the satellite images.
Align them spatially and temporally.
Normalize pixel values.
LNN Architecture Design:
Develop a specialized LNN architecture.
Consider the adaptability required for analyzing time series data.
Model the LNN based on principles inspired by C. elegans neurons.




Training:
Train the LNN using labeled data.
Use pairs of satellite images taken at different times.
Optimize the LNN’s parameters dynamically during training.




Change Detection:
Apply the trained LNN to identify changes between image pairs.
Highlight regions with significant alterations (e.g., land cover changes, urban growth).
Change Prediction:
Enhance the LNN’s capabilities to predict future changes.
Utilize historical data to learn patterns and trends.
Anticipate alterations in upcoming satellite images.
Evaluation:
Define appropriate evaluation metrics (precision, recall, F1-score, accuracy).
Assess the LNN’s performance in both change detection and prediction tasks.
Application:
Deploy the trained LNN for real-time analysis of multi-temporal satellite data.
Support decision-making in fields like environmental monitoring, disaster response, and urban planning.





https://app.eraser.io/workspace/VrB6Tf91CmkiGfUxuCN9?origin=share


Innovative works

Dynamic Region-of-Interest (ROI) Adjustment:
Develop a mechanism within the LNN to dynamically adjust the size and location of the region-of-interest (ROI) based on the significance of changes. This can improve the model's efficiency by focusing computational resources on areas with potential alterations.

Incremental Learning for Adaptive Changes:
Implement an incremental learning strategy to allow the model to adapt to gradual changes over time. This approach could enable the model to continuously update its knowledge and adapt to evolving environments without requiring retraining from scratch.

Explainability and Uncertainty Estimation:
Incorporate techniques for model explainability and uncertainty estimation, providing insights into why the model predicts certain changes and indicating its confidence level. This is crucial for building trust in the model's predictions, especially in decision-critical applications.
Federated Learning for Decentralized Training:
Explore federated learning approaches to train the Liquid Neural Network across multiple distributed sources of satellite data. This decentralized training strategy respects data privacy while still allowing the model to learn from diverse datasets.

Hyperdimensional Computing for Feature Extraction:
Investigate the use of hyperdimensional computing techniques for feature extraction from satellite data. This unconventional approach could capture complex patterns in the data and enhance the model's ability to discern subtle changes.



