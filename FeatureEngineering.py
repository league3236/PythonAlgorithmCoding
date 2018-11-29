
import re

content = "현대렌탈케어 관계자는 &quot;과거 황사가 심할 때만 사용하던 공기청정기가 24시간 사용하는 '생활밀착형 가전'으로 자리잡은 데다, 10월 말부터 <b>미세먼지</b> 농도가 연일 나쁨 수준을 보이자 공기청정기를 찾는 고객 수요가"
content = re.sub('[^a-zA-Z0-9 ㄱ-ㅣ가-힣]','',content)
print(content)
content = re.sub('[\ba-zA-Z0-9]','',content)
print(content)
