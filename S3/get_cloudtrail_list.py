from datetime import datetime
from common.create_session import SessionMaker

s = SessionMaker()
session = s.makeSession()

s3 = session.client('s3')
trail= session.client('cloudtrail')
start_time=datetime(2022, 1, 19)
end_time=datetime(2022, 4, 19)

bukets = s3.list_buckets()['Buckets']
q = []

for buket in bukets:
    butket_name = buket['Name']
    print(butket_name)
    response = trail.lookup_events(
                LookupAttributes=[
                    {
                        'AttributeKey': 'ResourceName',
                        'AttributeValue': butket_name
                    },
                ],
                StartTime=start_time,
                EndTime=end_time,
            )
    
    if len(response['Events']) > 0 :
        q.append(butket_name)

print(q)
        
    


