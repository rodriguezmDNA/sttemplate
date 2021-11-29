# Template repo for Streamlit apps

### Instructions

Before running the app create a `secrets.toml` inside the `.streamlit` directory with the AWS access keys for the streamlit with the following format. 

__Important__: <em>If you're creating a repo from scratch don't forget to add `.streamlit/secrets.toml` to  `.gitignore`!</em>

```
[streamlit]
AccessKeyId='xxxxxxxxxxx'
SecretAccessKey='xxxxxxxxxxx'

[default]
aws_access_key_id = 'xxxxxxxxxxx'
aws_secret_access_key = 'xxxxxxxxxxx'
```

Next, create the conda environment, activate, and run the app:

```python
conda env create -f environment.yml
conda activate st 
streamlit run streamlit.py
```
Play around with the `streamlit.py` file and see how the app changes.

---



### Deploy to Streamlit For Teams

1. Upload the code to (private, if possible) repo on GitHub. Gitlab is not supported yet.
2. Go to `share.streamlit.io` and login with GitHub
3. Select `New app` > `From existing repo` and follow the instructions:
   1. Paste the URL for the GitHub repo
   2. Select branch (usually `main`)
   3. If the file is inside a folder, write the path (ie `/scripts/app.py`)
4. Deploy!
5. Once deployed go back to `share.streamlit.io` and add `foodome.co` to the `Allowed email domains` field for the app just deployed.

