# # # Part 1
# # The Diamond Problem

# class BaseClass:
#     num_base_calls = 0
#     def call_me(self):
#         print("Calling method on Base Class")
#         self.num_base_calls += 1
#
# class LeftSubclass(BaseClass):
#     num_left_calls = 0
#     def call_me(self):
#         BaseClass.call_me(self)
#         print("Calling method on Left Subclass")
#         self.num_left_calls += 1
#
# class RightSubclass(BaseClass):
#     num_right_calls = 0
#     def call_me(self):
#         BaseClass.call_me(self)
#         print("Calling method on Right Subclass")
#         self.num_right_calls += 1
#
# class Subclass(LeftSubclass, RightSubclass):
#     num_sub_calls = 0
#     def call_me(self):
#         LeftSubclass.call_me(self)
#         RightSubclass.call_me(self)
#         print("Calling method on Subclass")
#         self.num_sub_calls += 1
#
# s = Subclass()
# s.call_me()
#
# print('s.num_sub_calls: ', s.num_sub_calls)
# print('s.num_left_calls: ', s.num_left_calls)
# print('s.num_right_calls: ', s.num_right_calls)
# print('s.num_base_calls: ', s.num_base_calls)

## ---------------------------------------------------------------------------------------------##
# # # Part 2 
# # Using Super
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1

s = Subclass()
s.call_me()
print('s.num_sub_calls: ', s.num_sub_calls)
print('s.num_left_calls: ', s.num_left_calls)
print('s.num_right_calls: ', s.num_right_calls)
print('s.num_base_calls: ', s.num_base_calls)