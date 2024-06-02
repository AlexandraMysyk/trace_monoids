from algorithm import ElementOfMonoid
import typing as tp

'''element = ElementOfMonoid(["a","b","c"],{"a":"a","b":"b","c":"c"})
list=["aa","b","cc","aab","caac","cbc"]
print(element.reconstruction(list))'''
'''element = ElementOfMonoid(["a","b","c"],{"a":"a","b":"b","c":"c"})
list=["aa","bb","cc","abab","aacc","bbcc"]
print(element.reconstruction(list))'''
'''element = ElementOfMonoid(["a","b","c"],{"a":"a","b":"b","c":"c"})
list=["aa","b","cc","aab","aacc","bcc"]
print(element.reconstruction(list))'''
'''el=ElementOfMonoid(["a","b","c","d"],{"a":"d","b":"c","a":"b","a":"a","b":"b","c":"c","d":"d"})
list=["aa","bb","c","dd","aac","dbdb","ddc"]
print(el.reconstructionPartiallyCommutative(list))'''
'''el=ElementOfMonoid(["a","b","c","d"],{"a":"d","b":"c","a":"b","a":"a","b":"b","c":"c","d":"d"})
list=["aa","bb","cc","d","acac","bdb","cdc"]
print(el.reconstructionPartiallyCommutative(list))'''
el=ElementOfMonoid(["a","b","c","d"],{"c":"d","b":"d","a":"a","b":"b","c":"c","d":"d"})
list=["aa","bb","cc","dd","acac","adad","abab","bcbc"]
print(el.reconstructionPartiallyCommutative(list))