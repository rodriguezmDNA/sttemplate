#### AWS
import boto3
from botocore.config import Config
import awswrangler as wr #install with pip, conda doesn't work very well
import s3fs as s3fsm #install with pip

import pandas as pd
import streamlit as st


###########################
#### Connect to S3

session_dev = boto3.Session(aws_access_key_id=st.secrets["streamlit"]['AccessKeyId'],
                      aws_secret_access_key=st.secrets["streamlit"]['SecretAccessKey'],
                      region_name='us-east-1')
# Set profile
s3fs = s3fsm.S3FileSystem(  anon=False, session = session_dev,
                client_kwargs ={
                   'aws_access_key_id':st.secrets["streamlit"]['AccessKeyId'],
                   'aws_secret_access_key':st.secrets["streamlit"]['SecretAccessKey'],
                   "region_name":'us-east-1'
                }
                )
         

def read_s3(s3Path,s3fs=s3fs):
    """
    Read a delimited file from S3
    """
    df = pd.read_csv(s3fs.open(s3Path, 'rb'), header=0, sep=None, engine='python',error_bad_lines=False,encoding='latin1')
    return df         