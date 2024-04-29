import uuid
import pandas as pd




def add_uuid_to_article(data_frame):
    data_frame['uuid'] = [uuid.uuid4() for _ in range(len(data_frame.index))]
    return data_frame 

data_frame = pd.read_csv('post-sitemap-1.csv')

add_uuid_to_article(data_frame).to_csv('post-sitemap-1.csv', index=False)


# Test line to commit