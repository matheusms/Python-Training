def right_justify(s):
    final_st=''
    st=''
    for i in range(1,71-len(s)):
        st+=' '
    for j in s:
        st+=j
        
    print(st)
    print(len(st))#para verificar o tamanho da string


def main():
    x='abc'
    right_justify(x)
main()
