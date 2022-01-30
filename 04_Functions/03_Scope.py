# x = 1
# # y = 2
# # print(x, y)
# #
# #
# # def local_scope():
# #     x = 500
# #     y = 700
# #     return x, y  # pass between my_functions or global variable use return NOT PRINT!
# #
# #
# # x, y = local_scope()
# # z = local_scope()
# # print(x, y)
# # print(z)  # returns tuple

x = 1


def local_scope(a):
    if a == 1:
        print("YES")
        return 2
    else:
        return a


x = local_scope(x)  #
