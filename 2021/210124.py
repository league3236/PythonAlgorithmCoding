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

def func(arg1: str, arg2: 1+2, arg3: '')


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        