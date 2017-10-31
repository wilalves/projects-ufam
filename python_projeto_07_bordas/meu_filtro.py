import numpy as np

def my_filter(I,w):

    M, N = I.size

    Tm, Tn = w.size

    Ip = np.zeros((M+2,N+2))

    for i in range(M):
        for j in range(N):
            Ip[i+1,j+1] = I[i,j]

    Ip[1,1:(N+2)] = Ip[2,1:(N+2)]
    Ip[(M+2),1:(N+2)] = Ip[(M+1),1:(N+2)]
    Ip[1:(M+2),1] = Ip[1:(M+2),2]
    Ip[1:(M+2),(N+2)] = Ip[1:(M+2),(N+1)]

    Ifilt = np.zeros(M,N)

    for i in range(M):
        for j in range(N):
            for k in range(Tm):
                for l in range(Tm):
                    Ifilt[i,j] = Ifilt[i,j] + w[k,l]*Ip[i+(k-1),j+(l-1)]

            Ifilt[i,j] = round(Ifilt[i,j])
