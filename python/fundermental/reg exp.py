## regular expression
## . ^ $ * + ? { } [ ] \ | ( )
import re
# a|b : a 혹은 b
# ^ : 맨처음 일치 "^start"
# $ : 마지막 일치 "end$"    ^$는 공백없는 빈칸
# . : 모든문자 a.b는 a와b 사이에 어떤 문자라도 된다는 뜻 (한글자)
# ? : 있어도 되고 없어도 됨. (ab?c) b가 있어도 없어도 됨

# + : 반복확인 ((ABC)+)는 ABC 문자열이 반복되는지 확인한다. (그루핑)
# * : 반복확인은 동일한데 0번 반복되어도 일치한다.
# 반복은 + 혹은 *의 앞문자를 확인한다. 뒷문자가 아님
# {1,5} : 반복횟수 제한 1에서 5회 반복이라는 뜻 

# 문자 클래스 [ ] 아래 6개 [ ] 안의 어떤 문자든 매치 확인
# [abc] 는 a,b,c중 어떤 문자든 일치가능하다.
# [a-z] a에서 z중 어떤 문자든 가능
# [^] ^가 들어가면 반대의 의미를 가진다 ** 중요
# [ ] 안에 들어가는 문자만 꼭 매치된다. [.]는 .를 일치한다. 모든문자가 아님

# \d : 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D : 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s : whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S : whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w : 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W : 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.


# match()	문자열의 처음부터 정규식과 매치되는지 조사한다.
# search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall()	정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer()	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
# x.compile(" ") 적용문

check = re.compile("a?b.c$")
print(check.match("bbc")) # re.Match object; span=(0, 3), match='bbc'>

# DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다. /n 등도 매치
check2 = re.compile('a.b', re.DOTALL)
print(check2.match("a\nb")) # <re.Match object; span=(0, 3), match='a\nb'>

# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
check3 = re.compile('[a-z]', re.I) # a-z 는 소문자만 일치하지만 여기서 대문자도 일치

# MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
check4 = re.compile("soul$", re.M)
data = """"this is our soul
    and my soul"""        
print(check4.findall(data))    ## soul이 줄마다 한개씩이니까 2개를 출력한다. 

# VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. 
# (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

