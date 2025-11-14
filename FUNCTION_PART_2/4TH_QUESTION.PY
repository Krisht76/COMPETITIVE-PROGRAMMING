#  4.What is the output of this code and tell a variable “lang “ is in local or global
#  scope?
#  def local():
#  lang = "Python"
#  print(lang)
#  local()
N = int(input())
for _ in range(N):
    def local():
        lang = "Python"
        print(lang)
    local()
    