import json
import os
import googleapiclient.discovery
import pandas as pd

def youtubeETL():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"]='1'

    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = 'AIzaSyA6Lw86c-VQk47nHuhQpszeHrh87kt3Jog'

    youtube = googleapiclient.discovery.build(
        api_service_name,api_version,developerKey=DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(
        part = 'id,snippet,replies',
        videoId = 'q8q3OFFfY6c'
    )
    
    response = request.execute()
    comments = []
    for comment in response['items']:
        author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
        publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
        comment_info = {'author': author, 'comment' : comment_text , 'published_at' : publish_time}
        comments.append(comment_info)
    print(f'Finished Processing {len(comments)} comments.')
    comments_list=comments

    while response.get('nextPageToken',None):
        request = youtube.commentThreads().list(
            part = 'id,snippet,replies',
            videoId = 'q8q3OFFfY6c',
            pageToken = response['nextPageToken']
        )
        response = request.execute()
        comments = []
        for comment in response['items']:
            author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
            publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
            comment_info = {'author': author, 'comment' : comment_text , 'published_at' : publish_time}
            comments.append(comment_info)
        print(f'Finished Processing {len(comments)} comments.')
        comments_list.extend(comments)
    


    with open('s3://airflow-youtube-comments/comments_list_yt.json','w') as f:
        json.dump(comments_list,f)

    df=pd.DataFrame(comments_list)
    df.to_csv('s3://airflow-youtube-comments/comment_list_yt.csv')

youtubeETL()

def process_comments(response_items):
    comments = []
    for comment in response_items:
        author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
        publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
        comment_info = {'author': author, 'comment' : comment_text , 'published_at' : publish_time}
        comments.append(comment_info)
    print(f'Finished Processing {len(comments)} comments.')
    return comments
