from bilibili_api import video, Verify
import os
verify = Verify(sessdata="810758c5%2C1606366695%2C35df9*51", csrf="ab39f9fb709768893fc3767c80869736")
# info = video.get_video_info(bvid='BV1Py4y1r7FL')
# print(info)
# comment = video.get_comments(bvid="BV1Py4y1r7FL", order='like')
# print(comment)
danmu = video.get_danmaku(bvid='BV1Py4y1r7FL')
for i in danmu:
    print(i.text)

# for root, dirs, files in os.walk('txts/'):
#     for i in files:
#         os.remove(root+i)
#     print(files)
