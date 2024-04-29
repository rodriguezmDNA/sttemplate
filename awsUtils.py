##### Prepare for S3
import pandas as pd
import boto3
from botocore.config import Config
import awswrangler as wr #install with pip, conda doesn't work very well
import s3fs as s3fsm #install with pip
import time as time

def startSession(profile):
    session_dev = boto3.Session(profile_name=profile)
    s3fs = s3fsm.S3FileSystem(
                anon=False,
                profile = profile
            )
    return session_dev,s3fs
    


# session_dev = boto3.Session(profile_name='joel')
# client = boto3.client('sts')

##### For when using streamlit
# response = client.assume_role(RoleArn=st.secrets["dev"]["role_arn"],
#                               RoleSessionName='dev')

# session_dev = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
#                       aws_secret_access_key=response['Credentials']['SecretAccessKey'],
#                       aws_session_token=response['Credentials']['SessionToken'],
#                       region_name='us-east-1')

##### Set profile
#s3fs = s3fsm.S3FileSystem(  anon=False, session = session_dev,
#                 client_kwargs ={
#                     'aws_access_key_id':response['Credentials']['AccessKeyId'],
#                     'aws_secret_access_key':response['Credentials']['SecretAccessKey'],
#                     'aws_session_token':response['Credentials']['SessionToken'],
#                     "region_name":'us-east-1'}
#)

def read_s3(s3Path,s3fs,sep=None):    
    """
    Read a delimited file from S3
    """
    df = pd.read_csv(s3fs.open(s3Path, 'rb'), header=0, sep=sep, engine='python',error_bad_lines=False,encoding='latin1')
    return df

def saveS3(df,toS3path,session_dev,verbose=False):
    """
    If the inchikey hasn't been stored in the Data Lake save it
    Input: a formatted inchikey -> CAS data frame with version (date of query) and name (first block of inchikey)
    Output: Saves tsv file to S3/Data Lake. Nothing gets returned.
    """
    
    try:
        if not wr.s3.does_object_exist(toS3path,boto3_session=session_dev):
            wr.s3.to_csv(df=df,path=toS3path,sep='\t',index=None,boto3_session=session_dev)
            if verbose: print(f'Ok saving to to {toS3path}')
        else:
            pass
            if verbose: print(f'Already in S3')
    except:
        if verbose: print(f'Error saving to {toS3path}')
        return None    

def runAthenaQuery(query,session_dev,verbose=False):
    if verbose: s = time.time()
    resultsQuery = wr.athena.read_sql_query(query, 
                   database=None, #tables are specified in the query
                   ctas_approach=False,
                   boto3_session=session_dev)

    if verbose: e = time.time()
    if verbose: runningtime('athena query',e,s)
    return resultsQuery


if __name__ == '__main__':
    print('Running main')
    
else:
    print('loading aws utils')
