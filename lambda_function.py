# Audio Flash Briefing Generator - JSON v1.4

import boto3
import os
import json
import uuid

# User Settings
frugality = True
single_item_feed = True

# Lambda Environment Variables
feed_bucket = os.environ['feed_bucket'] # Example: flash-briefing-skill-assets
feed_key = os.environ['feed_key'] # Example: feed/breaking_news.json
redirection_url = os.environ['redirection_url'] # Example: https://amazon.com

# Boto3 Objects
s3 = boto3.resource('s3')
bucket = s3.Bucket(feed_bucket)

def build_feed(feed, update_date, title_text, bucket, key, redirection_url):
    new_item = {
        'uid': str(uuid.uuid4()),
        'updateDate': update_date,
        'titleText': title_text,
        'mainText': '',
        'streamUrl': 'https://s3.amazonaws.com/' + bucket + '/' + key,
        'redirectionUrl': redirection_url
    }
    feed.insert(0, new_item)
    return feed

def change_storage_class(bucket, key, storage_class):
    copy_source = {
        'Bucket': bucket,
        'Key': key
    }
    s3.meta.client.copy(copy_source, bucket, key, ExtraArgs = {'StorageClass': storage_class, 'MetadataDirective': 'COPY'})

def feed_already_exists(bucket, key):
    keys =[]
    for s3_object in bucket.objects.all():
        keys.append(s3_object.key)
    if key in keys:
        return True
    else:
        return False

def make_object_public(bucket, key):
    s3_object = s3.Object(bucket, key.replace('+', ' '))
    s3_object.Acl().put(ACL = 'public-read')

def make_title_text(key):
    title_text = key[key.rfind('/')+1:] # Parse key to save only the file name at end
    title_text = title_text.replace('.mp3', '') # Removes ".mp3" file extension
    title_text = title_text.replace('+', ' ') # Replace "+" with space. Spaces are converted to "+" in S3 trigger
    return title_text

def lambda_handler(event, context):
    update_date = event['Records'][0]['eventTime']
    mp3_bucket = event['Records'][0]['s3']['bucket']['name']
    mp3_key = event['Records'][0]['s3']['object']['key']

    # Main
    feed_pointer = '/tmp/feed.json'
    if feed_already_exists(bucket, feed_key) and not single_item_feed:
        s3.Bucket(feed_bucket).download_file(feed_key, feed_pointer)
        with open(feed_pointer, 'r', encoding = 'utf-8') as rf:
            feed = json.loads(rf.read())
    else:
        feed = []

    feed = build_feed(feed, update_date, make_title_text(mp3_key), mp3_bucket, mp3_key, redirection_url)

    if frugality:
        change_storage_class(mp3_bucket, mp3_key.replace('+', ' '), 'INTELLIGENT_TIERING')

    make_object_public(mp3_bucket, mp3_key)

    with open(feed_pointer, 'w', encoding = 'utf-8') as wf:
        wf.write(json.dumps(feed, indent = 4, sort_keys = True, ensure_ascii = False))

    s3.meta.client.upload_file(feed_pointer, feed_bucket, feed_key, ExtraArgs = {'ACL': 'public-read','ContentType': 'application/json'})
