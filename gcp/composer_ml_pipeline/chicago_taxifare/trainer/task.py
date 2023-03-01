Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@thecodemancer 
GoogleCloudPlatform
/
training-data-analyst
Public
Fork your own copy of GoogleCloudPlatform/training-data-analyst
Code
Issues
106
Pull requests
202
Actions
Projects
Security
Insights
Beta Try the new code view
training-data-analyst/courses/data-engineering/demos/composer_ml_pipeline/chicago_taxifare/trainer/task.py /
@maabel0712
maabel0712 Added files for end-to-end ML pipeline with Cloud Composer demo.
Latest commit ea52c3e on Apr 29, 2020
 History
 1 contributor
42 lines (36 sloc)  1015 Bytes

import argparse

from . import model


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--train_data_path",
        help="GCS or local path to training data",
        required=True
    )
    parser.add_argument(
        "--train_epochs",
        help="Steps to run the training job for (default: 5)",
        type=int,
        default=10
    )
    parser.add_argument(
        "--eval_data_path",
        help="GCS or local path to evaluation data",
        required=True
    )
    parser.add_argument(
        "--output_dir",
        help="GCS location to write checkpoints and export models",
        required=True
    )
    parser.add_argument(
        "--log_dir",
        help="GCS location to write Tensorboard logs",
        required=True
    )
    parser.add_argument(
        "--job-dir",
        help="This is not used by our model, but it is required by gcloud",
    )
    hparams = parser.parse_args().__dict__

    model.train_and_evaluate(hparams)
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
training-data-analyst/task.py at master · GoogleCloudPlatform/training-data-analyst
