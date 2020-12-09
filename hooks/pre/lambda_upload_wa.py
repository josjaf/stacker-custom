from stacker.hooks.aws_lambda import upload_lambda_functions


def custom_lambda_upload(context, provider, **kwargs):
    new_results = {}
    results = upload_lambda_functions(context, provider, **kwargs)
    for name, code_obj in results.items():
        new_results = {
            "s3_key": code_obj.S3Key,
            "s3_bucket": code_obj.S3Bucket
        }
    return new_results


"""
pre_build:
  - path: hooks.pre.lambda_upload_wa.custom_upload_lambda_functions #lambda_upload_wa.custom_upload_lambda_functions
    required: true
    enabled: true
    data_key: alert_lambda
    args:
      bucket: ${stacker_bucket}
      follow_symlinks: false
      prefix: predict_lambda/
      functions:
        predict_lambda:
          path: lambda_function/alert_lambda/
          include:
            - "*.py"
"""