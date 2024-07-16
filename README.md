# Data Breakdown

**IMPORTANT:** This competition presents a unique structure to determine eligible models for winning. It is extremely important that participants read the rules carefully before continuing. In particular, sections 7-9 should be very well understood before embarking on this challenge.

## Welcome to The NASA Breath Diagnostics Challenge

The objective of this challenge is to develop a classification model that can accurately diagnose patients with COVID-19 based on data captured using NASA's own E-Nose device.

The total number of patients, and therefore examples, is 63. As you can probably tell, this is a very limited dataset, so making efficient use of the provided data is of extreme importance in this challenge. We encourage creativity in dealing with the data in order to make the best use of it. Also, for this reason, it is very important to understand the rules governing this event and how this will be ultimately scored to ensure that the best models win.

The data consists of 63 txt files representing the 63 patients, numbered 1 to 63. Each file contains the Patient ID, the COVID-19 Diagnosis Result (POSITIVE or NEGATIVE), and numeric measurements for 64 sensors D1 to D64. These sensors are evenly distributed inside the E-Nose device and measure different biochemical signals that can be present in the breath of the patients.

All sensor data is indexed by a timestamp with the format Min:Sec, which represents the minute of the hour and the second of that minute in which that sensor was sampled. The hour is left out, but when the minute counter resets, it means that the next hour has begun. Keep this in mind when working with this time axis.

To achieve maximum consistency across patients, the data was exposed to the E-Nose device using a pulsation bag that had previously collected a patient's breath. The E-Nose device also reads from an ambient air signal that can be used to normalize the exposed breaths. The data was exposed to the E-Nose device for all patients using windows of exposure through the following process:

1. 5 min baseline measurement using ambient air
2. 1 min breath sample exposure and measurement, using the filled breath bag
3. 2 min sensor “recovery” using ambient air
4. 1 min breath sample exposure and measurement, using the filled breath bag
5. 2 min sensor “recovery” using ambient air
6. 1 min breath sample exposure and measurement, using the filled breath bag
7. 2 min sensor “recovery” using ambient air

Total time = 14 mins

The data is distributed like this:
- Train: 45 patients
- Test: 18 patients

Within the dataset, there are also 2 other files: `submission_example.csv` and `train_test_split_order.csv`. The first file represents how all submission files should look. The values should be 0 for NEGATIVE and 1 for POSITIVE. Failing to follow this format will result in an error or lower score.

The second file (`train_test_split_order.csv`) represents which patient IDs are considered for Train (i.e., are labeled) and which ones are for Test (not labeled), and the order in which they should be put inside the submission files.

The order of the predictions in the submission file should be the same as in the TEST indicated rows in `train_test_split_order.csv` file. The index column of this submission file is NOT the ID of the patient, but the order of values in the Result column should follow the one in the `train_test_split_order.csv` file. This is very important.

The evaluation metric is **Accuracy**.

The leaderboard will be split into a Public and Private leaderboard, where the preliminary results to advance to the final evaluation stage will be determined by the Private Leaderboard, which will be revealed at the end of the competition period. Again, please refer to the rules, in particular sections 7 to 9 to understand the particular evaluation criteria for this challenge.

Please note that the goal of the Public Leaderboard will be mostly for reference, as it will represent only a very rough assessment of a model's performance. The final score may deviate substantially from this score. Any attempt to try to "game" this score or artificially inflate it will not result in any benefit accounting for the final score and could end in disqualification if the model is found to be purposely overfitting this value.

We wish you good luck in this challenge. If there are questions, please refer to the FAQ, Rules, or send an email to info@bitgrit.net.
