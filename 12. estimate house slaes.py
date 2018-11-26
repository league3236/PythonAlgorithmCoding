def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood) :
    price = 0

# 담당 지역 내 평균 주택 가격은 평방 피트 당 200  달러
    price_per_sqft = 200

if neighborhood == "hipsterton":
    #하지만 다른 지역은 조금 더 비싸다
    price_per_sqft = 400

elif neighborhood == "skid row":
    #그리고 다른 몇몇 지역은 싸다
    price_per_sqft = 100

# 주택의 크기를 기반으로 주택 가격을 추정하는 것으로 시작
price = price_per_sqft * sqft

#침실의 개수로 추정치를 조정
if num_of_bedrooms == 0:
    #원룸형 아파트는 가격이 싸다
    price = price-20000
else:
    #일반적으로 많은 침실이 있는 주택이 더 비싸다
    price = price + (num_of_bedrooms * 1000)

return price