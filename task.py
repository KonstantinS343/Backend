# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 
# 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—',
#  'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—',
#   'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 
#   'x': '—••—', 'y': '—•——', 'z': '——••'}
# morze_version= []
# letter_version = input("Input the world:")
# letter_version = letter_version.lower()
# for i in letter_version:
#     key = morze.get(i)
#     if key==None:
#         morze_version.append(" ")
#     else:
#         morze_version.append(key)
# print(''.join(morze_version))
#--------------------------------------------

# def main():
#     first_number=1
#     second_number=1
#     result=0
#     print(first_number,second_number, end=' ')
#     for i in range(0,100):
#         result=second_number+first_number
#         first_number=second_number
#         second_number=result
#         print(second_number,end=' ')
#     return 0
# main()
#--------------------------------------------

# def main():
#     first_list=[]
#     first_list=input("Enter the items of the first list:").split()
#     second_list=[]
#     second_list=input("Enter the items of the second list:").split()
#     final_list=[]
#     index=0
#     if len(first_list)>len(second_list):
#         lenth=len(second_list)
#         add_lenth=len(first_list)-len(second_list)
#         first_lenth=True
#     else:
#         lenth=len(first_list)
#         add_lenth=len(second_list)-len(first_list)
#         first_lenth=False
#     for i in range(lenth):
#         final_list.insert(index,first_list[i])
#         index+=1
#         final_list.insert(index,second_list[i])
#         index+=1
#     for i in range(lenth,lenth+add_lenth):
#         if first_lenth==True:
#             final_list.insert(index,first_list[i])
#             index+=1
#         elif first_lenth==False:
#             final_list.insert(index,second_list[i])
#             index+=1
#     print(final_list)    
#     return 0
# main()
#-----------------------------------------------------

# def main(old_list):
#     new_odd_llist=[]
#     for i in range(len(old_list)):
#         if i%2==1:
#             new_odd_llist.append(old_list[i])
#     return new_odd_llist

# user_list=[]
# user_list=input("Enter the items of  the list:").split()
# return_odd_position=[]
# return_odd_position=main(user_list) 
# print(return_odd_position)  
#=============================================

# def main(old_list):
#     new_list=[]
#     new_list=list(reversed(old_list))
#     for i in range(len(new_list)):
#         new_list[i]=list(reversed(new_list[i]))
#         new_list[i]=''.join(new_list[i])
#     return new_list
# user_list=[]
# user_list=input("Enter the items of the list:").split()
# rev_list=main(user_list)
# print(rev_list)
#----------------------------------------------

# def main(user_list):
#     return user_list[::-1]
# user_list=[]
# user_list=input("Enter the items of the list:").split()
# rev_list=main(user_list)
# print(rev_list)