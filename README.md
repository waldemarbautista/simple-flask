# simple-flask
Simple Flask application to test ECS Blue/Green deployment

## How to Use

Prepare the environment variables in `taskdef.json`.

- `zip -r code.zip .`
- `aws s3 cp code.zip s3://<source bucket>`

## Known Issues

- No trigger. Use GitHub Actions to zip and upload the code.
- Use env file instead?