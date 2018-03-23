# Works without tuples

# class MathDojo(object):
#     def __init__(self):
#         self.result = 0
#     def add(self, *num):
#         for count in range(len(num)):
#             if isinstance(num[count], list):
#                 temp = 0
#                 # print num[count]
#                 for val in num[count]:
#                     temp += val
#                     # print temp
#                 self.result += temp
#             elif isinstance(num[count], int):
#                 self.result += num[count]
#         # print self.result
#         return self
#     def subtract(self, *num):
#         for count in range(len(num)):
#             if isinstance(num[count], list):
#                 temp = 0
#                 # print num[count]
#                 for val in num[count]:
#                     temp += val
#                     # print temp
#                 self.result -= temp
#             elif isinstance(num[count], int):
#                 self.result -= num[count]
#         # print self.result
#         return self


# Works with tuples
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *num):
        for count in range(len(num)):
            for val in num[count]:
                if isinstance(val, list):
                    self.result += sum(val)
                elif isinstance(val, int):
                    self.result += val
                else:
                    self.result += sum(val)
        return self
    def subtract(self, *num):
        for count in range(len(num)):
            for val in num[count]:
                if isinstance(val, list):
                    self.result -= sum(val)
                elif isinstance(val, int):
                    print val
                    self.result -= val
                else:
                    self.result -= sum(val)
        return self        

md = MathDojo()
print md.add([(1, 2), (3, 4), (5, 6)]).add((1, 3, 5)).subtract([(1, 3), (4, 5)]).result