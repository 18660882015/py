#!usr/bin/python
#使用collections模块defaultdict类来实现该功能
import string
import random
x=string.ascii_letters+string.digits+string.punctuation
y=[random.choice(x)for i in range(1000)]
z=''.join(y)
from collections import defaultdict
frequences=defaultdict(int)
for item in z:
    frequences[item]+=1
frequences.items()
#使用collections模块count类来实现该功能
from collections import Counter
frequences=Counter(z)
frequences.items()
frequences.most_common(1)
frequences.most_common(3)
