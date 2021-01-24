# https://bluese05.tistory.com/78

# function annotation

# function annotation은 python3 이상에서 사용 가능하다.
# annotation 문법을 사용해 function을 정의하는 예제

# ```
# def func(arg1: str, arg2: 1+2, arg3: 'this is annotation') -> bool
# ```

# 위와 같이 파라미터에 : expression 형태로 매개변수마다 annotation을 쓸 수 있다.
# annotation에는 arg1 처럼 매개변수의 type을 써놓을 수도 있고,
# arg2의 annotation처럼 덧셈과 같은 간단한 연산 표현도 작성가능하며,
# arg3처럼 string 형태로도 작성 가능하다.

# 또한, function의 return 값에 대해서는 -> expression 형태로 사용한다.
# return 또한 매개변수와 사용 방법은 동일하다.

# function annotation의 특징
# annotation의 가장 큰 특징은 바로 강제성이 없다는 것이다.
# 즉, annotation이라는 말그대로 주석일 뿐이며 해당 code 자체에는 어떠한 영향도 미치지 않는다.

def func(arg1: str, arg2: 1+2, arg3: 'this is annotation') -> bool:
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    print(f'arg3 = {arg3}')
    return True

result = func('test1', 3, 'this is test')
print(f'result = {result}')

# annotation에 적혀 있는 내용은 주석이므로 실제로는 이와 상관없이 실행되게 된다.

def func1(arg1: str, arg2: 1+2, arg3: 'this is annotation') -> bool:
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    print(f'arg3 = {arg3}')
    return 'melong'

result = func1('test1', 'test2', 'test3')
print(f'result = {result}')

# function annotation의 장점
# annotation의 장점이라고 한다면, 함수의 매개변수와 반환값을 명시적으로 보여준다는데 있다.
# python은 언어의 특성상 변수의 자료형을 명시적으로 지정하지 않기 때문에 사용성이 간편하고 유연한 대신 코드의 명확성은 떨어지는 단점이 있다.
# 보통 그래서 function을 작성할때 아래와 같이 주석(comment)를 달아 개발자간 커뮤니케이션에 쓰이긴 하지만 이것 또한 지속적으로 작성하기 쉽지 않기 때문이다.


# Function with comments

def func(arg1, arg2, arg3):
    ```
    :param arg1: str
    :param arg2: str
    :param arg3: list
    :retgurn: bool
    ```

# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
sol1 = Solution()

result = sol1.twoSum([2,7,11,15], 9)
print(f'result = {result}')

    